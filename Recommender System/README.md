# Recommender System Submission

## 1. Project Overview

Pada project Machine Learning saya membuat Recommender System mengenai pencarian buku berdasarkan preferensi pengguna dan rating yang diberikan pengguna sebelumnya. Perpustakaan sudah merambah ke ranah digital. Keberadaan sistem informasi perpustakaan di perguruan tinggi dapat dirasakan telah memudahkan para pengunjung, baik mahasiswa maupun dosen, dalam mencari bahan referensi yang menjadi koleksi perpustakaan dimaksud.

Proyek ini berguna ketika pengunjung perpustakaan kampus menelusuri judul buku dan judul buku terkait tidak tersedia dan tidak adanya rekomendasi untuk buku-buku lain yang mungkin menarik untuk dibaca atau bahkan dibutuhkan sebagai pelengkap dari judul buku yang diinginkan, maka peran sistem rekomendasi disini sangat dibutuhkan **[1]**. Rekomendasi tersebut bisa berdasarkan preferensi pengunjung dan rating yang diberikan pengunjung sebelumnya.

## 2. Business Understanding

Meskipun sistem cukup membantu pengunjung dalam mencari buku yang mereka inginkan. Terdapat masalah yang perlu diselesaikan dengan sistem rekomendasi yang akan saya buat.

### 2.1 Problem Statements

Permasalahannya adalah pengunjung sering terpaku hanya pada judul buku yang mereka inginkan. Ketika buku itu tidak tersedia, tidak ada rekomendasi untuk buku-buku lain yang mungkin menarik untuk dibaca atau bahkan dibutuhkan sebagai pelengkap dari judul buku yang diinginkan. Kondisi ini dapat menyebabkan berkurangnya minat pengunjung untuk mengeksplorasi koleksi perpustakaan lainnya, dan berarti mengecilkan tujuan dan peran perpustakaan di dalam meningkatkan minat baca mahasiswa dan akademisi di perguruan tinggi.

### 2.2 Goals

Tujuan dari dibuat nya sistem rekomendasi ini adalah agar dapat membantu pengunjung perpustakaan dalam mencari buku dengan lebih Efektif. Efektif dalam hal merekomendasikan buku terkait yang ditelusuri pengguna berdasarkan preferensi dan rating buku sehingga dapat meningkatkan minat baca mahasiswa dan akademisi diperpustakaan perguruan tinggi.

### 2.3 Solution statements

Solusi dalam menyelesaikan masalah ini yaitu saya menggunakan algoritma content based filtering dan Collaborative Filtering

![1_aSq9viZGEYiWwL9uJ3Recw](https://user-images.githubusercontent.com/46146748/63115930-5f6c1900-bf66-11e9-894f-ecde5ec531b0.png)

- **Content Based Filtering**. Metode Content-Based Filtering bekerja dengan melihat kemiripan item baru dengan item yang sebelumnya. Content-BasedFiltering memberikan rekomendasi berdasarkan kemiripan item yang dianalisis dari fitur yang dikandung oleh item sebelumnya **[2]**.

- **Collaborative Filtering**. Collaborative filtering merupakan proses penyaringan atau pengevaluasian item menggunakan opini orang lain. Collaborative filtering melakukan penyaringan data berdasarkan kemiripan karakteristik konsumen sehingga mampu memberikan informasi yang baru kepada konsumen karena sistem memberikan informasi berdasarkan pola satu kelompok konsumen menjadikan sumber informasi baru yang mungkin bermanfaat bagi anggota kelompok lainnya.Berikut adalah persamaan cosine similarity yang digunakan untuk menghitung nilai kemiripan diantara item **[3]**.

## 3 Data Understanding

Data ini dapat diunduh pada link dibawah ini
[Link Dataset](https://www.kaggle.com/arashnic/book-recommendation-dataset)

Dataset ini berisi 3 tabel:

1. Book
   Dataset ini berjumlah 271360 data
2. User
   Dataset ini berjumlah 278858 data
3. Rating
   Dataset ini berjumlah 1149780 data

Pada dataset _Book_ berisi variabel

- ISBN (Nomor seri buku)
- Book-Title (Judul Buku)
- Book-Author (Penulis Buku)
- Year-Of-Publication (Tahun publikasi)
- Publisher (penerbit buku)
- Image-URL-S (Ukuran gambar small)
- Image-URL-M (Ukuran gambar medium)
- Image-URL-L (Ukuran gambar large)

Pada Dataset _User_ berisi variabel

- User-ID (ID User)
- Location (lokasi user)
- Age (umur user)

Pada Dataset _Rating_ berisi variabel

- User-ID (ID User)
- ISBN (Nomor seri buku)
- Book-Rating (rating buku)

## 4. Data Preparation

### 4.1 Data Preprocessing

Tahapan preprocessing pada laporan ini penting untuk menyatukan ketiga dataset yang saya gunakan yaitu:

- Book
- User
- Rating

Adapun prosesnya yaitu:

1. Menggabungkan Buku

   Pertama, mari kita identifikasi berapa jumlah seluruh buku pada dataset. Di sini, kita menggunakan library numpy dan fungsi concatenate untuk menggabungkan beberapa file. Selanjutnya kita akan menggabungkan seluruh data pada kategori buku. Sehingga, kita akan menggunakan ISBN yang unik sebagai acuan dalam penggabungan ini

2. Menggabungkan Seluruh User

   Gunakan fungsi concatenate dari library numpy untuk menggabungkan seluruh data pada kategori variabel User berdasarkan UserId.

3. Ketahui Jumlah Rating

   Pada tahapan ini, jumlah rating dapat diketahui dengan menggabungkan dataset rating dan buku

4. Menggabungkan Data dengan fitur judul buku

   Pertama, definisikan variabel book_rate dengan variabel rating yang telah kita ketahui sebelumnya. Selanjutnya, untuk mengetahui judul buku dengan ISBN tertentu, mari kita gabungkan data geo yang berisikan ISBN dan judul buku berdasarkan ISBN dan assign ke variabel all_resto_name dengan fungsi merge dari library pandas

5. Menggabungkan Judul buku dengan fitur publisher

   Langkah selanjutnya adalah menggabungkan variabel all_book_name yang kita peroleh dari tahapan sebelumnya dengan fitur publisher buku. Tujuannya, agar kita mengetahui publisher yang menerbitkan buku.

kemudian, setelah dilakukan data preprocessing data harus disiapkan terlebih dahulu. Adapun langkah persiapan data yang saya lakukan yaitu:

1. Mengatasi missing value

   Setelah ketiga dataset telah berhasil digabungkan, kita cek lagi apakah ada missing value. Pada data yang digunakan masih terdapat missing value, maka dari itu penulis mengatasi missing value dengan menggunakan perintah dropna().

## 5. Modeling

Saya memilih 2 model yaitu content based filtering dan collaborative filtering.
Content Based Filtering untuk mendapatkan rekomendasi buku yang mirip dengan yang disukai pembaca. Pengguna sedang membaca buku yang dia sukai, untuk menumbuhkan minat membaca agar membaca dilakukan tidak hanya sekali maka dibutuhkan sistem rekomendasi untuk merekomendasikan bahan bacaan yang serupa dengan yang pengguna baca **[4]**.

Collaborative Filtering untuk mencari rating buku dan direkomendasikan ke pembaca. Agar kualitas bahan bacaan pengguna tinggi dibutuhkan rekomendasi dari pengguna lain berdasarkan rating **[5]**.

## 6. Evaluation

Metrik klasifikasi mengukur seberapa baik sistem rekomendasi
dalam mengklasifikasikan item dengan benar. Jarak dari ambang toleransi tidak masalah, tapi orang yang berbeda memiliki toleransi perbedaan. Dengan kata lain, kita tidak dapat berasumsi bahwa peringkat di atas dua bintang sudah cukup baik untuk semua orang [2], [5], [12]. Ambang batas yang lebih masuk akal akan menjadi rata-rata vektor, yaitu, peringkat positif jika lebih besar dari atau sama dengan rata-rata vektor. Ambang batas toleransi menghasilkan skala biner, baik orang tersebut menyukai item (positif) atau tidak (negatif). Demikian juga, rekomendasi bisa benar (true) atau salah (false). Pengikut metrik menghitung jumlah kemunculan setiap prediksi (p) dan nilai aktual (r)

- True Positive (TP): p = positive, r = positive
- False Negative (FN): p = negative, r = positive
- False Positive (FP): p = positive, r = negative
- True Negative (TN): p = negative, r = negative

Precision dan recall merangkum angka-angka ini menjadi lebih banyak metrik intuitif. Precision adalah pecahan dari semua peringkat positif yang diklasifikasikan dengan benar seperti itu. Ini mengukur seberapa baik sistem dalam mengenali rekomendasi positif. Untuk misalnya, Precision 60% berarti bahwa pengguna dapat mengharapkan untuk benar-benar menikmati tiga dari setiap lima rekomendasi. Ini mengukur seberapa baik sistem dalam menemukan positif rekomendasi [4], [10], [24]. Misalnya, Recall 80%
berarti bahwa sistem dapat menebak dengan benar empat dari setiap lima film favorit Anda.

Meskipun precision dan recall adalah metric yang terpisah, tetapi mereka sebenarnya terkait. Biasanya, presisi tinggi berarti daya ingat rendah dan mengingat tinggi berarti presisi rendah. Salah satu cara populer untuk menggabungkan presisi dan recall menjadi satu metrik adalah menghitung F-measure, yang merupakan rata-rata harmonik dari keduanya.

Untuk mendapatkan nilai presisi sebesar 60%, Anda perlu menghitung metrik presisi (precision) berdasarkan hasil prediksi yang Anda miliki. Presisi merupakan rasio dari true positive (positif yang benar) dibagi dengan jumlah total prediksi positif (true positive + false positive). Berikut adalah langkah-langkah umum untuk mencapai nilai presisi 60%:
1. Tentukan metrik evaluasi: Dalam hal ini, kita tertarik untuk mendapatkan nilai presisi. Jadi, kita akan fokus pada menghitung presisi.

2. Hitung true positive (TP) dan false positive (FP): True positive adalah jumlah prediksi positif yang benar, sedangkan false positive adalah jumlah prediksi positif yang salah.

3. Tentukan persamaan untuk menghitung presisi: Presisi dapat dihitung menggunakan persamaan berikut:
Presisi = TP / (TP + FP)

4. Atur persamaan agar menghasilkan nilai presisi 60%: Misalnya, jika Anda ingin mendapatkan presisi sebesar 60%, Anda dapat memodifikasi persamaan menjadi:
TP / (TP + FP) = 0.6

5. Selesaikan persamaan untuk mendapatkan nilai TP: Dalam persamaan di atas, TP adalah variabel yang tidak diketahui. Anda perlu mencari nilai TP yang memenuhi persamaan tersebut agar presisinya menjadi 60%.

Formula:

$$ F - MEASURE = {2 * (PRECISION * RECALL) \over PRECISION + CALL} $$ **[6]**

## Daftra Pustaka

[1] [S. K. Dirjen et al., ‘Sistem Rekomendasi Buku untuk Perpustakaan Perguruan Tinggi Berbasis Association Rule’, masa berlaku mulai, vol. 1, no. 3, pp. 304–312, 2017.](http://jurnal.iaii.or.id/index.php/RESTI/article/view/971/158)

[2] [M. Alkaff, H. Khatimi, and A. Eriadi, ‘Sistem Rekomendasi Buku pada Perpustakaan Daerah Provinsi Kalimantan Selatan Menggunakan Metode Content-Based Filtering’, MATRIK : Jurnal Manajemen, Teknik Informatika dan Rekayasa Komputer, vol. 20, no. 1, pp. 193–202, Sep. 2020, doi: 10.30812/matrik.v20i1.617.](https://journal.universitasbumigora.ac.id/index.php/matrik/article/view/617/587)

[3] [A. Rokhim and A. Saikhu, Sistem Rekomendasi Buku Pada Aplikasi Perpustakaan Menggunakan Metode Collaborative Filtering Pada Smkn 1 Bangil’, 2016.](http://jurnal.stmik-yadika.ac.id/index.php/spirit/article/view/52/32)

[4] [J. Basilico and T. Hofmann, ‘Unifying Collaborative and Content-Based Filtering’, in Proceedings of the Twenty-First International Conference on Machine Learning, in ICML ’04. New York, NY, USA: Association for Computing Machinery, 2004, p. 9. doi: 10.1145/1015330.1015394.](https://dl.acm.org/doi/abs/10.1145/1015330.1015394?casa_token=hs7-fclGnYYAAAAA:WUZgTBMI7fXe3L5qCSvDLMjexJ-bCCSzzaogMt1jLD-yqn4FFxP5KyeqRHPfM--RRA2aJNW3d5mxhg)

[5] [S. Rahmawati, D. Nurjanah, and R. Rismala, ‘Analisis dan Implementasi pendekatan Hybrid untuk Sistem Rekomendasi Pekerjaan dengan Metode Knowledge Based dan Collaborative Filtering’, Indonesian Journal on Computing (Indo-JC), vol. 3, no. 2, p. 11, Sep. 2018, doi: 10.21108/indojc.2018.3.2.210.](https://socj.telkomuniversity.ac.id/ojs/index.php/indojc/article/view/210/104)

[6] [S. Morozov, X. Zhong, and S. Morozov, ‘The Evaluation of Similarity Metrics in Collaborative Filtering Recommenders’, 2013.](https://huichawaii.org/assets/met_morozov_sergey_2013.pdf)
