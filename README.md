<h1 align="center">Tubes Stigma RD WreCooking</h1>
Diamonds merupakan suatu programming challenge yang mempertandingkan bot yang anda buat dengan bot dari para pemain lainnya. Setiap pemain akan memiliki sebuah bot dimana tujuan dari bot ini adalah mengumpulkan diamond sebanyak-banyaknya. Cara mengumpulkan diamond tersebut tidak akan sesederhana itu, tentunya akan terdapat berbagai rintangan yang akan membuat permainan ini menjadi lebih seru dan kompleks. Untuk memenangkan pertandingan, setiap pemain harus mengimplementasikan strategi tertentu pada masing-masing bot-nya. 

## Algoritma Greedy
Tiga strategi greedy Density, Weight, dan Profit menawarkan pendekatan berbeda untuk memandu bot dalam permainan mengumpulkan diamond. Strategi Density bekerja dengan menganalisis semua diamond di papan permainan dan mengurutkannya berdasarkan metrik kepadatan nilai, yang dihitung dengan membagi poin diamond dengan jarak Manhattan dari bot; diamond dengan rasio poin per jarak tertinggi menjadi target utama. Bot ini memutuskan kembali ke base jika inventory penuh, jika waktu yang dibutuhkan untuk mencapai base hampir sama dengan sisa waktu permainan, atau jika targetnya adalah diamond merah (2 point) dan inventory hanya kurang satu slot.

Strategi Weight memprioritaskan kembali ke markas jika bot telah mengumpulkan lima diamond. Jika belum, bot akan mencari diamond yang jaraknya terdekat dari bot. Bot tidak memikirkan point dari diamond dan hanya fokus mencari terdekat.

Strategi Profit mengidentifikasi semua objek game dan mengevaluasi diamond berdasarkan jumlah poinnya. Bot akan bergerak ke arah diamond dengan poin tertinggi. Kondisi kembali ke base meliputi inventory penuh, sisa waktu yang hanya cukup untuk perjalanan ke base, atau jika targetnya diamond merah sementara inventory sudah berisi empat diamond.

## Requirement

https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0

https://nodejs.org/en

https://www.docker.com/products/docker-desktop/

## Langkah 

| npm install --global yarn|
|---------------------------|
| cd tubes1-IF2211-game-engine-1.1.0
| yarn
| ./scripts/copy-env.bat
| docker compose up -d database
| ./scripts/setup-db-prisma.bat
| npm run build
| npm run start
| cd tubes1-IF2211-bot-starter-pack-1.0.1
| ./run-bots.bat

## Pembuat

| WerCooking|
|---------------------------|
| Muhammad Ghama Al Fajri
| Taufik Hidayat NST
| Abi Sholihan
