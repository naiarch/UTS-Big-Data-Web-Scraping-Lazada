# UTS-Big-Data-Web-Scraping-Lazada
Tugas UTS Mata Kuliah Big Data: Web Scraping Lazada


# Analisis Komparatif Nilai Konsumen pada Watsons dan Dan+Dan dalam Industri Ritel Kecantikan

Projek ini merupakan analisis data mata kuliah Big Data yang bertujuan untuk membandingkan strategi harga, promosi, dan performa penjualan antara dua toko ritel kecantikan di Indonesia, yaitu Watsons dan Dan+Dan, melalui platform e-commerce Lazada.


# Project Overview

Projek ini mengintegrasikan teknik web scraping, pembersihan data (data cleaning), dan visualisasi data untuk mengeksplorasi bagaimana perbedaan strategi antara kedua toko memengaruhi nilai konsumen (consumer value). Analisis ini memberikan gambaran mendalam mengenai tren pasar kecantikan di ekosistem digital.


# Latar Belakang

Industri ritel kecantikan dan perawatan diri di Indonesia berkembang pesat seiring meningkatnya kesadaran masyarakat terhadap perawatan diri. Hal ini mendorong tingginya permintaan produk seperti skincare, makeup, dan personal care, serta meningkatkan persaingan antar toko, terutama dalam hal harga, variasi produk, dan strategi promosi.

Perkembangan e-commerce seperti Lazada juga memberikan kemudahan dalam mengakses data pasar. Informasi seperti harga, rating, jumlah review, dan produk terjual dapat dimanfaatkan untuk memahami perilaku konsumen serta dinamika persaingan tanpa bergantung pada data internal perusahaan.

Watsons dan Dan+Dan merupakan dua toko ritel yang menawarkan produk sejenis dan berada dalam pasar yang sama. Meskipun demikian, keduanya memiliki strategi yang berbeda dalam memberikan nilai kepada konsumen, baik dari segi harga, kelengkapan produk, maupun popularitas.

Oleh karena itu, diperlukan analisis berbasis data untuk membandingkan kedua toko tersebut guna mengetahui perbedaan nilai yang ditawarkan serta menentukan toko yang lebih unggul dalam memenuhi kebutuhan konsumen.


# Tujuan

1. Mengidentifikasi karakteristik toko Watsons dan Dandan dalam industri ritel kecantikan.

2. Menganalisis aspek-aspek yang ditawarkan oleh kedua toko, seperti variasi produk, harga, dan pelayanan.

3. Menganalisis karakteristik 5V (Volume, Velocity, Variety, Veracity, dan Value) terhadap toko Watsons dan Dan+Dan.

4. Mengetahui keunggulan dan kekurangan masing-masing toko berdasarkan hasil analisis.

5. Menarik kesimpulan mengenai preferensi konsumen terhadap kedua toko tersebut.


# Deskripsi Data

**Metode Pengambilan Data**

Data diperoleh melalui teknik Web Scraping secara mandiri pada platform Lazada Indonesia. Proses pengambilan data berfokus pada toko resmi (official store) Watsons dan Dan+Dan untuk memastikan validitas sumber.


**Spesifikasi Data**

1. Toko Watsons

- Sumber: Lazada Indonesia

- Waktu Pengambilan: 2 April 2026

- Jumlah Data: 2000 baris dan 14 kolom

- Atribut Data: toko, nama_produk, harga, harga_original, diskon, rating, jumlah_review, jumlah_terjual, nama_toko_lazada, lokasi, brand, url_produk, url_gambar, tanggal_scraping

2. Toko Dan+Dan

- Sumber: Lazada Indonesia

- Waktu Pengambilan: 7 April 2026

- Jumlah Data: 1.666 baris

- Atribut Data: toko, nama_produk, harga, harga_origin, diskon, rating, jumlah_review, jumlah_terjual, lokasi, kategori, brand, url_produk, url_gambar, tanggal_scraping

3. Dataset FInal yang Sudah Di Merge

- Sumber: Lazada Indonesia

- Jumlah Data: 3.666 baris

- Atribut Data: toko, nama_produk, harga, harga_original, diskon, rating, jumlah_review, jumlah_terjual, lokasi, url_produk, url_gambar, tanggal_scraping


# Insight Analisis

**A. Global Analysis (Karakteristik Umum Dataset Final)**

- Distribusi Harga Produk: Berdasarkan histogram harga, mayoritas produk berada di rentang Rp10.000 hingga Rp150.000. Kurva distribusi menunjukkan kemiringan positif (right-skewed), yang mengonfirmasi bahwa produk dengan harga terjangkau jauh lebih mendominasi pasar dibandingkan produk premium.

- Statistik Deskriptif Utama: Data menunjukkan adanya nilai ekstrem (outlier) pada harga produk yang mencapai angka jutaan, namun median harga berada di angka yang jauh lebih rendah (sekitar Rp40.000 - Rp60.000). Rata-rata diskon yang diberikan berkisar di angka 20% hingga 50%.

- Produk Terlaris (Top Selling): Produk dengan label penjualan "10RB+" didominasi oleh kategori kebutuhan harian (daily essentials) seperti kapas, cotton buds, dan masker wajah. Hal ini menunjukkan volume penjualan tertinggi tidak datang dari produk kosmetik mahal, melainkan barang konsumsi cepat (fast-moving).

- Hubungan Antara Variabel Harga dengan Penjualan: Scatter plot menunjukkan pola di mana produk dengan harga di bawah Rp50.000 memiliki sebaran titik penjualan (jumlah_terjual) yang paling padat dan tinggi.

- Hubungan Antara Variabel Diskon dengan Penjualan: Terdapat korelasi positif di mana produk dengan diskon di atas 30% cenderung memiliki angka penjualan yang lebih stabil dan tinggi dibandingkan produk dengan harga normal.

-  Korelasi Antar Variabel: Analisis matriks korelasi menunjukkan bahwa Rating dan Jumlah Review memiliki hubungan yang sangat kuat dengan angka penjualan, mengindikasikan bahwa kepercayaan konsumen digital sangat bergantung pada testimoni pembeli sebelumnya.

**B. Comparative Analysis (Watsons vs Dandan)**

- Perbandingan Distribusi Harga: Melalui visualisasi Boxplot, terlihat bahwa toko Dan+Dan memiliki sebaran harga yang lebih rapat di kategori rendah hingga menengah. Sebaliknya, Watsons memiliki jangkauan harga yang lebih luas dengan banyak titik outlier di harga tinggi, menandakan koleksi produk dari toko Watsons lebih bervariasi hingga ke segmen high-end.

- Perbandingan Penjualan: Watsons memiliki frekuensi produk dengan penjualan "RB+" yang lebih banyak secara total, namun Dan+Dan menunjukkan performa yang sangat kompetitif pada kategori produk lokal dan kebutuhan dasar.

- Perbandingan Diskon: Watsons secara konsisten memberikan label diskon pada hampir seluruh produknya di platform Lazada, sementara Dan+Dan menggunakan strategi diskon besar pada produk-produk tertentu secara selektif.

- Perbandingan Rating: Rata-rata rating di kedua toko berada di angka 4.8 - 4.9. Ini membuktikan bahwa dari sisi Veracity (keaslian produk), kedua toko memiliki tingkat kepercayaan yang sangat tinggi di mata konsumen. 

**C. Add-Ons Insight**

- Hidden Gem Products: Ditemukan produk dengan harga di bawah Rp20.000 yang secara konsisten terjual ribuan unit setiap bulannya. Produk ini menjadi "magnet" traffic bagi toko.

- Outlier Detection: Terdeteksi beberapa produk kategori skincare tertentu yang memiliki harga tinggi namun tetap memiliki angka penjualan yang fantastis, mematahkan teori bahwa hanya barang murah yang laku di e-commerce.

- Produk Diskon Tinggi tapi Tidak Laku: Analisis menemukan beberapa item dengan diskon mencapai 60% namun jumlah penjualannya rendah. Hal ini membuktikan bahwa strategi harga saja tidak cukup jika produk tersebut tidak memiliki relevansi tren atau kebutuhan di pasar saat ini.


# Analisis 5V

- Volume: Mengolah ribuan entri data produk (3666 baris) kecantikan dari dua kompetitor secara simultan untuk membandingkan performanya.

- Velocity: Aspek velocity tercermin dari dinamika platform Lazada yang mengubah data harga, diskon, dan stok produk secara cepat dalam hitungan detik. Kecepatan ini ditangkap melalui kolom tanggal_scraping serta fluktuasi angka penjualan dan rating yang menggambarkan arus transaksi riil secara instan. 

- Variety: Menangani keragaman format data yang mencakup data terstruktur, semi-terstruktur, dan teks. Dataset ini terdiri dari 12 kolom dengan tipe data yang bervariasi:

> Data Kategorikal & Teks (object): toko, nama_produk, lokasi, dan tanggal_scraping.

> Data Numerik Presisi (Int64): harga, harga_original, jumlah_review, dan jumlah_terjual.

> Data Numerik Desimal (float64): diskon dan rating.

> Data Unstructured/Link (object): url_produk dan url_gambar.

- Veracity: Keakuratan data dijamin melalui proses cleaning data, seperti:

> Normalisasi karakter encoding pada nama kolom toko, dan harga_original.

> Konversi tipe data dari teks mentah ke format numerik (Int64 dan float64) agar bisa dihitung secara statistik.

> Penanganan missing value (Non-Null Count) pada kolom sensitif seperti harga_original dan rating.

- Value: Mengubah data mentah hasil scraping menjadi informasi strategis mengenai perbandingan harga, efektivitas promosi, dan loyalitas konsumen di industri ritel kecantikan. 


# Kesimpulan

Analisis komparatif antara toko Watsons dan Dan+Dan di platform Lazada ini mengintegrasikan prinsip Big Data 5V dengan mengolah 3.666 baris data yang mencakup 12 atribut beragam, mulai dari informasi tekstual hingga data numerik. Aspek veracity dijaga melalui pembersihan terhadap gangguan encoding serta normalisasi tipe data, sementara velocity tercermin dari pengambilan data dinamis pasar e-commerce. Hasil analisis menunjukkan bahwa pasar kecantikan didominasi oleh produk terjangkau di bawah Rp50.000, dengan toko Watsons unggul di segmen premium-variatif dan Dan+Dan kuat pada segmen ekonomis-stabil. Insight yang ditemukan membuktikan bahwa kepercayaan konsumen melalui rating dan ulasan (social proof) memiliki pengaruh lebih signifikan terhadap volume penjualan dibandingkan sekadar besaran diskon, mengingat adanya produk diskon tinggi yang tetap rendah peminat jika tidak sesuai tren. Inti dari projek ini terletak pada keberhasilan mengubah data mentah menjadi insight yang memetakan kekuatan kedua ritel dalam memenangkan perilaku belanja digital.
