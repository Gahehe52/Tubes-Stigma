from typing import Optional, Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position

#Greedy By Weight
class WeightBot(BaseLogic):
    def __init__(self):
        self.goal_position: Optional[Position] = None
        self.last_teleporter_used: Optional[Position] = None

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        bot = board_bot.properties
        pos = board_bot.position
        base = bot.base
        diamonds = board.diamonds

        if not diamonds:
            return 0, 0

        teleporters = [obj for obj in board.game_objects if obj.type == "TeleportGameObject"]
        tele1, tele2 = (teleporters + [None, None])[:2]

        def distance(a: Position, b: Position) -> int:
            return abs(a.x - b.x) + abs(a.y - b.y)

        def distance_with_teleport(a: Position, b: Position) -> int:
            if tele1 and tele2:
                via_tele1 = distance(a, tele1.position) + distance(tele2.position, b)
                via_tele2 = distance(a, tele2.position) + distance(tele1.position, b)
                return min(distance(a, b), via_tele1, via_tele2)
            return distance(a, b)

        target = min(diamonds, key=lambda d: distance_with_teleport(pos, d.position))

        time = int(bot.milliseconds_left / 1000)

        should_return = (
            bot.diamonds == bot.inventory_size or
            distance_with_teleport(pos, base) >= time or
            (target.properties.points == 2 and bot.diamonds == bot.inventory_size - 1)
        )

        dest = base if should_return else target.position

        def should_use_teleporter(from_pos: Position, to_pos: Position) -> Optional[Position]:
            if not (tele1 and tele2):
                return None
            direct = distance(from_pos, to_pos)
            via_1 = distance(from_pos, tele1.position) + distance(tele2.position, to_pos)
            via_2 = distance(from_pos, tele2.position) + distance(tele1.position, to_pos)

            if via_1 < direct and tele1.position != self.last_teleporter_used:
                return tele1.position
            elif via_2 < direct and tele2.position != self.last_teleporter_used:
                return tele2.position
            return None

        tele_jump = should_use_teleporter(pos, dest)

        if tele_jump:
            self.last_teleporter_used = tele_jump
            move_target = tele_jump
        else:
            if pos in [tele1.position if tele1 else None, tele2.position if tele2 else None]:
                self.last_teleporter_used = pos
            move_target = dest

        delta_x = max(min(move_target.x - pos.x, 1), -1)
        delta_y = max(min(move_target.y - pos.y, 1), -1)
        if delta_x != 0:
            delta_y = 0

        return delta_x, delta_y