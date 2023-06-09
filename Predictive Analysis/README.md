# *Predictive Analysis Submission*
## *Business Understanding*
### **Latar Belakang**
Harga diamonds yang terlalu mahal akan membuat seseorang berpikir berkali-kali untuk memutuskan untuk membeli diamonds. Sebaliknya, harga diamonds yang terlalu murah, akan menyebabkan perusahaan tidak dapat memaksimalkan keuntungan bagi perusahaan, hal ini akan menyebabkan kerugian bagi perusahaan.

Oleh sebab itu, maka perlu dibuat aplikasi yang dapat memprediksi harga ideal diamonds, untuk menjadi bahan pengambilan keputusan dalam penerapan harga diamonds ideal, sehingga harga tiket akan seimbang (tidak terlalu mahal, juga tidak terlalu murah). Harga diamonds ideal adalah harga yang sesuai dengan berdasarkan tingkat kualitas dari diamonds tersebut.

### **Problem Statements**
Berdasarkan penjelasan yang telah disampaikan sebelumnya, maka problem statements (rumusan masalah), yaitu sebagai berikut:
Apa faktor-faktor yang dapat mempengaruhi harga diamonds?

### **Goals**
Tujuan yang ingin dicapai dari pembuatan aplikasi prediksi harga diamonds, yaitu sebagai berikut:
Mengetahui faktor-faktor yang mempengaruhi harga diamonds?
Membuat aplikasi yang dapat memprediksi harga diamonds secara akurat, sebagai bahan pengambilan keputusan dalam penerapan harga diamonds ideal.

### **Solution statements**
Solusi yang dapat dilakukan untuk menangani permasalahan sebagaimana terdapat dalam problem statements, yaitu dengan membuat aplikasi prediksi harga diamonds. Adapun aplikasi tersebut dibuat dengan menerapkan teknologi machine learning serta bahasa pemrograman python.
Algoritma machine learning yang akan digunakan, yaitu Extra Trees Regressor, Lasso Regression, Lasso Least Angle Regression dan Elastic Net.
Untuk mengukur keakuratan/keidealan prediksi harga diamonds yang dilakukan oleh aplikasi yang dibuat, maka metrik yang digunakan adalah Mean Squared Error (MSE).

## *Data Understanding*
Data yang digunakan adalah dataset yang bersumber dari situs Github yang berisi dataset terkait Diamonds Price. Dataset yang digunakan dapat didownload pada link berikut ini:(https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv). Jumlah data yang terdapat didalam file tersebut sebanyak 53940 data.

### Variabel-variabel yang terdapat dalam dataset Diamonds:
- carat = merupakan tingkat kadar karat pada diamonds
- cut = merupakan jenis potongan pada diamonds
- color = merupakan warna pada diamonds
- clarity = merupakan tingkat kejernihan pada diamonds
- depth = variabel ini bertipe data float
- table = variabel ini bertipe data float
- price = merupakan harga diamonds
- x = variabel ini bertipe data float
- y = variabel ini bertipe data float
- z = variabel ini bertipe data float

## *Data Preparation*
Teknik *data preparation* yang dilakukan, yaitu sebagai berikut:
1. Mengubah dataset *diamonds* menjadi *dataframe* dengan menggunakan *pandas*.
2. Melakukan *exploratory data analysis* untuk memahami variabel-variabel yang terdapat dalam dataset.
4. Memvisualisasikan data dengan menggunakan *boxplot* untuk mencari *outlier*.
5. Menggunakan IQR *(Interquartile Range)* untuk mengeliminasi outlier.
6. Melakukan *univariative analysis* untuk memahami sebaran data variabel.
7. Melakukan *multivariative analysis* untuk memahami korelasi variabel kategorikal dan numberikal terhadap variabel *price*.  
8. Membuat *correlation matrix* untuk fitur numerik.
9. Mengeliminasi variabel numerik yang memiliki korelasi rendah terhadap variabel *price*.
### *Exploratory Data Analysis*
#### *Exploratory Data Analysis - Data Cleansing*
#### *Exploratory Data Analysis - Univariate Analysis*

![image](https://user-images.githubusercontent.com/81604461/244475132-73c27ede-0132-4b89-ba81-0fc51939493a.png?raw=true)

Gambar 1: visualisasi variabel cut dengan menggunakan histogram

Berdasarkan hasil visualisasi, kategori ideal pada kolom cut memiliki nilai terginggi dibandingkan dengan kategori lainnya.

![image](https://user-images.githubusercontent.com/81604461/244475761-84745941-0b64-44ee-9b2b-25aaad6a385f.png?raw=true)

Gambar 2: visualisasi variabel color dengan menggunakan histogram

Berdasarkan hasil visualisasi, kategori G pada kolom color memiliki nilai terginggi dibandingkan dengan kategori lainnya.

![image](https://user-images.githubusercontent.com/81604461/244476079-66eba612-bf52-48c2-be9d-a517a91084b8.png?raw=true)

Gambar 3: visualisasi numerik variabel dengan menggunakan histogram

#### *Exploratory Data Analysis - Multivariate Analysis*

![image](https://user-images.githubusercontent.com/81604461/244476751-276e4658-75ef-4481-8d9f-bcd0c680b095.png?raw=true)

Gambar 4: multivariate analysis antara variabel cut dengan price

![image](https://user-images.githubusercontent.com/81604461/244477024-fd4bcaa1-d573-4dba-94bf-4036c9889214.png?raw=true)

Gambar 5: multivariate analysis antara variabel color dengan price

![image](https://user-images.githubusercontent.com/81604461/244477030-ff8ab1f5-ae2b-4af4-8afa-7e446685cbc5.png?raw=true)

Gambar 6: multivariate analysis antara variabel clarity dengan price

![correlation matrix](https://user-images.githubusercontent.com/81604461/244479558-98e283e1-2e41-45da-a742-ac47e8d81da1.png?raw=true)

Gambar 7: Correlation Matrix

Bila kita lihat, bahwa korelasi variabel depth terhadap price = 0.01 dan korelasi variabel table terhadap price = 0.14.

## *Modeling*
Model machine learning yang digunakan adalah Extra Trees Regressor, Lasso Regression, Lasso Least Angle Regression dan Elastic Net.

**Extra Trees Regressor** adalah algoritma yang digunakan untuk masalah regresi dalam machine learning. Algoritma ini merupakan variasi dari algoritma Decision Tree yang menggunakan teknik ensemble learning. Ensemble learning menggabungkan beberapa model pembelajaran untuk meningkatkan kinerja dan kestabilan prediksi.

Berikut adalah langkah-langkah utama dalam algoritma Extra Trees Regressor:
1. Random Subspace: Pada setiap langkah pembentukan pohon keputusan, subset acak fitur dari dataset dilakukan. Ini berarti setiap pohon hanya menggunakan sebagian kecil fitur yang tersedia. Tujuannya adalah untuk mencegah pohon menjadi sangat serupa satu sama lain dan meningkatkan variasi dalam ensemble.
2. Random Split Points: Ketika membangun setiap node dalam pohon, beberapa titik pemisahan (split points) yang acak dipertimbangkan untuk setiap fitur. Ini memungkinkan algoritma untuk menemukan titik pemisahan yang optimal secara acak, yang dapat mengurangi overfitting dan meningkatkan kestabilan prediksi.
3. Voting: Ketika melakukan prediksi, setiap pohon memberikan prediksi berdasarkan struktur pohon dan fitur yang dipertimbangkan pada saat itu. Prediksi dari setiap pohon kemudian diakumulasikan menggunakan teknik voting, seperti rata-rata atau mayoritas, untuk menghasilkan prediksi akhir.

Keuntungan dari Extra Trees Regressor adalah sebagai berikut:
* Mengurangi overfitting: Dengan menggunakan teknik random subspace dan random split points, Extra Trees Regressor mengurangi risiko overfitting pada data pelatihan dan meningkatkan generalisasi pada data uji.
* Stabilitas: Karena keputusan dalam membangun pohon dilakukan secara acak, model ini lebih tahan terhadap variasi dalam data pelatihan dan dapat memberikan hasil yang lebih stabil.
* Komputasi paralel: Karena setiap pohon independen, algoritma ini dapat dengan mudah diimplementasikan dalam komputasi paralel untuk meningkatkan efisiensi pemrosesan.

- Parameter yang digunakan dalam model **Extra Trees Regressor**, yaitu sebagai berikut:
    - ExtraTreesRegressor = function yang digunakan untuk melakukan proses training model dengan menggunakan Extra Trees Regressor. Function ini berada pada library / modul sklearn.ensemble.
    - n_estimators = jumlah pohon keputusan (decision tree) yang akan dibuat pada model Extra Trees Regressor yang digunakan. Pada model ini n_estimators yang di buat, yaitu 100.
    - random_state = mengatur status random dari model Extra Trees Regressor. Pada model ini random state yang digunakan adalah 42.
    - ETree_regressor.fit(X_train, y_train) = menentukan data yang akan digunakan pada proses training model Extra Trees Regressor.
    - mean_squared_error = Mean Squared Error (MSE) adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat.

Demi mendapatkan hasil yang terbaik, selain menggunakan Extra Trees Regressor, digunakan algoritma lain, yaitu Lasso Regression, Lasso Least Angle Regression dan Elastic Net sebagai algoritma pembanding untuk mengukur manakah algoritma yang lebih baik dalam menghasilkan prediksi harga diamonds.

**Lasso Regression (Least Absolute Shrinkage and Selection Operator Regression)** adalah sebuah algoritma dalam machine learning yang digunakan untuk pemodelan regresi dengan regularisasi. Tujuan utama Lasso Regression adalah untuk melakukan seleksi fitur dan mengurangi overfitting dalam model regresi.

Berikut adalah beberapa poin penting tentang Lasso Regression:
1. Regularisasi L1: Lasso Regression menggunakan regularisasi L1 yang ditambahkan ke fungsi objektif yang akan dioptimalkan. Regularisasi L1 merupakan penjumlahan nilai absolut dari koefisien yang digunakan dalam model regresi. Dengan menggunakan regularisasi L1, Lasso Regression mendorong beberapa koefisien menjadi nol, sehingga secara efektif melakukan seleksi fitur dan mempersempit model.
2. Variabel Seleksi: Salah satu keunggulan utama Lasso Regression adalah kemampuannya untuk melakukan seleksi fitur secara otomatis. Dengan menempatkan penalti yang cukup tinggi pada fitur yang kurang penting, Lasso Regression akan mengatur koefisien fitur yang tidak relevan menjadi nol. Ini membantu dalam menghilangkan fitur yang tidak memberikan kontribusi signifikan terhadap prediksi dan menghasilkan model yang lebih sederhana dan terinterpretasi dengan baik.
3. Sparsity: Lasso Regression sering menghasilkan solusi sparse, yaitu solusi di mana sebagian besar koefisien adalah nol. Hal ini terjadi karena regularisasi L1 cenderung "mendorong" beberapa koefisien menjadi nol, menghasilkan model yang hanya menggunakan subset fitur yang penting untuk prediksi.
4. Tuning Parameter: Lasso Regression memiliki parameter alpha yang mengendalikan kekuatan regularisasi. Semakin besar nilai alpha, semakin tinggi tingkat penalti yang diterapkan pada koefisien, sehingga lebih banyak koefisien yang cenderung menjadi nol. Nilai alpha yang optimal dapat ditentukan melalui validasi silang atau teknik tuning parameter lainnya.

Keuntungan Lasso Regression meliputi kemampuannya untuk melakukan seleksi fitur secara otomatis, menghasilkan model yang lebih sederhana dan terinterpretasi, serta mengurangi risiko overfitting pada data pelatihan.

Namun, ada beberapa catatan yang perlu diperhatikan saat menggunakan Lasso Regression:
* Jika ada korelasi tinggi antara fitur-fitur, Lasso Regression cenderung memilih satu fitur dan mengabaikan yang lain.
* Pada dataset dengan jumlah fitur yang sangat besar, komputasi Lasso Regression bisa menjadi lebih lambat.
* Jika ada fitur yang saling dependen secara kuat, Lasso Regression bisa mengalami masalah dalam memilih fitur yang tepat.

- Parameter yang digunakan dalam **Lasso Regression**, yaitu sebagai berikut:
    - Lasso = function yang digunakan untuk melakukan proses training model dengan menggunakan Lasso Regression. Function ini berada pada library / modul sklearn.linear_model.
    - alpha = Parameter alpha mengontrol kekuatan penalti L1. Semakin besar nilai alpha, semakin besar penalti L1 yang diterapkan, dan semakin banyak koefisien yang akan ditekan menjadi 0. Pada model ini alpha yang dibuat bernilai 0.1.
    - random_state = mengatur status random dari model Extra Trees Regressor. Pada model ini random state yang digunakan adalah 42.
    - mean_squared_error = Mean Squared Error (MSE) adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat.

**Lasso Least Angle Regression (LARS)** adalah sebuah algoritma yang digunakan dalam machine learning untuk pemodelan regresi dengan regularisasi Lasso. LARS dikembangkan dengan tujuan untuk mengatasi keterbatasan komputasi dari algoritma Lasso standar ketika jumlah fitur sangat besar atau bahkan lebih besar daripada jumlah sampel yang tersedia.

Berikut adalah beberapa poin penting tentang Lasso Least Angle Regression:
1. Stepwise Forward Selection: LARS menggunakan pendekatan "stepwise forward selection" untuk membangun model regresi. Pada setiap langkahnya, LARS memilih fitur yang memiliki korelasi paling kuat dengan variabel target dan sejajar dengan arah solusi optimal. Dalam langkah-langkah berikutnya, LARS bergerak sepanjang jalur solusi dengan mengontrol besarnya koefisien yang ditambahkan ke model.
2. Pathwise Algorithm: LARS menghitung solusi Lasso untuk semua nilai alpha secara simultan, menghasilkan jalur solusi lengkap dari model regresi. Algoritma ini menghindari proses pelatihan yang memakan waktu secara berulang dengan memanfaatkan sifat linier dalam solusi Lasso.
3. Koefisien Berkembang: LARS memperkenalkan konsep "koefisien berkembang" (evolving coefficients) untuk mengontrol bagaimana setiap fitur berkontribusi pada model saat fitur-fitur baru diperkenalkan. Koefisien berkembang memungkinkan interpretasi yang lebih baik dan memberikan wawasan tentang pentingnya setiap fitur dalam model.
4. Regularisasi L1: LARS menggunakan regularisasi L1 (Lasso) dalam fungsi objektif yang dioptimalkan. Regularisasi L1 membantu menghasilkan model yang sparse, yaitu dengan sebagian besar koefisien yang nol. Ini memungkinkan LARS untuk melakukan seleksi fitur secara otomatis dan menghasilkan model yang lebih sederhana dan terinterpretasi.

Keuntungan dari Lasso Least Angle Regression termasuk kemampuan untuk mengatasi masalah komputasi yang terkait dengan dataset berfitur besar, kemampuan untuk membangun jalur solusi lengkap, dan interpretasi yang baik dari koefisien berkembang.

- Parameter yang digunakan dalam **Lasso Least Angle Regression**, yaitu sebagai berikut:
    - LassoLars = function yang digunakan untuk melakukan proses training model dengan menggunakan Lasso Least Angle Regression. Function ini berada pada library / modul sklearn.linear_model.
    - alpha = Parameter alpha mengontrol kekuatan penalti L1. Semakin besar nilai alpha, semakin besar penalti L1 yang diterapkan, dan semakin banyak koefisien yang akan ditekan menjadi 0. Pada model ini alpha yang dibuat bernilai 0.1.
     - mean_squared_error = Mean Squared Error (MSE) adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat.

**Elastic Net** adalah sebuah algoritma yang digunakan dalam machine learning untuk pemodelan regresi dengan regularisasi. Algoritma ini dikembangkan dengan tujuan untuk mengatasi beberapa keterbatasan yang dimiliki oleh algoritma Lasso dan Ridge Regression.

Berikut adalah beberapa poin penting tentang algoritma Elastic Net:
1. Kombinasi L1 dan L2 Regularisasi: Elastic Net mengkombinasikan regularisasi L1 (Lasso) dan regularisasi L2 (Ridge) dalam fungsi objektif yang dioptimalkan. Regularisasi L1 mendorong beberapa koefisien menjadi nol, sehingga melakukan seleksi fitur, sementara regularisasi L2 mencegah koefisien menjadi terlalu besar. Dengan memadukan keduanya, Elastic Net dapat mengatasi kelemahan Lasso yang cenderung memilih satu fitur dalam kasus korelasi tinggi antara fitur dan kelemahan Ridge Regression yang tidak dapat melakukan seleksi fitur.
2. Penalti Hiperparameter: Elastic Net memiliki dua hiperparameter utama, yaitu alpha dan l1_ratio. Alpha mengendalikan kekuatan regularisasi secara keseluruhan, dengan nilai yang lebih tinggi menghasilkan model yang lebih teregularisasi. L1_ratio mengontrol proporsi regularisasi L1 dan L2, dengan nilai 1 menghasilkan regularisasi L1 penuh dan nilai 0 menghasilkan regularisasi L2 penuh. Pemilihan hiperparameter yang tepat melalui validasi silang dapat membantu menghasilkan model yang optimal.
3. Penanganan Multikolinearitas: Elastic Net dapat mengatasi masalah multikolinearitas, yaitu adanya korelasi tinggi antara fitur-fitur. Dalam kasus multikolinearitas, Elastic Net cenderung memilih kelompok fitur yang saling terkait secara konsisten daripada memilih satu fitur secara acak seperti yang dilakukan oleh Lasso. Dengan demikian, Elastic Net menghasilkan model yang lebih stabil dan konsisten dalam kasus multikolinearitas.
4. Trade-off antara Sparsity dan Stabilitas: Elastic Net menawarkan trade-off antara sparsity (kehadiran fitur yang lebih sedikit) dan stabilitas dalam model. Dengan menggunakan kombinasi regularisasi L1 dan L2, Elastic Net dapat menghasilkan model yang lebih teregularisasi daripada Lasso, sehingga dapat mempertahankan fitur-fitur yang saling berkorelasi secara signifikan.

Keuntungan dari Elastic Net meliputi kemampuannya untuk mengatasi masalah multikolinearitas, melakukan seleksi fitur secara otomatis, dan menghasilkan model yang lebih stabil.

- Parameter yang digunakan dalam **Elastic Net**, yaitu sebagai berikut:
    - ElasticNet = function yang digunakan untuk melakukan proses training model dengan menggunakan Elastic Net. Function ini berada pada library / modul sklearn.linear_model.
    - alpha = Parameter Alpha adalah parameter penalti yang mengontrol kekuatan regularisasi. Pada model ini alpha yang dibuat bernilai 0.1.
    - l1_ratio = rasio L1 terhadap total regularisasi. Pada model ini rasio L1 yang dibuat bernilai 0.5.
    - random_state = random_state adalah parameter yang digunakan untuk memastikan reproduktibilitas hasil. Pada model ini random state yang digunakan adalah 42.
    - mean_squared_error = Mean Squared Error (MSE) adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat.

## *Evaluation*
Tabel 1: Hasil Evaluasi Model dengan Menggunakan Mean Squared Error
Model                        | train        | test	       |
---------------------------- | -----------  | ------------ |
Extra Trees Regressor        | 0.054081 	| 149.967816   |
Lasso Regression             | 558.32874	| 555.515268   |
Lasso Least Angle Regression | 558.328177   | 555.515686   |
Elastic Net                  | 837.14892    | 831.40399    |
- Metrik yang digunakan untuk mengukur hasil *training* adalah *mean squared error (MSE)*. 
- Berdasarkan hasil training, bahwa model *Extra Trees Regressor* menghasilan nilai MSE pada saat *training* = 0.054081 dan pada saat tes = 149.967816. 
- Berdasarkan hasil training model, maka ditetapkan bahwa algoritma yang terbaik diantara *Extra Trees Regressor* sedangkan *Lasso Regression* dan *Lasso Least Angle Regression* memiliki performa yang tidak terpaut jauh dalam memprediksi harga diamonds, yaitu algoritma *Extra Trees Regressor*.
- karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.

Model | y_true | prediksi_Extra Trees Regressor | prediksi_Lasso Regression | prediksi_Lasso Least Angle Regression | prediksi_Elastic Net |
----- | ------ | ------------------------------ | ------------------------- | ------------------------------------- | -------------------- |
51619 |  2396  | 2468.4                         | 2842.2                    | 2842.2                                | 3277.8               |
23536 |  11540 | 11435.0                        | 9589.9                    | 9590.0                                | 8452.0               |
10413 |  4779  | 5763.0                         | 5577.1                    | 5577.1                                | 5551.6               |
3157  |  3334  | 3542.4                         | 3852.8                    | 3852.7                                | 3999.0               |
1566  |  3005  | 2622.4                         | 2754.5                    | 2754.4                                | 3399.7               |
52429 |  2513  | 2536.0                         | 2896.5                    | 2896.5                                | 3189.5               |
41000 |  1183  | 1273.1                         | 1608.3                    | 1608.3                                | 1326.2               |
11795 |  5088  | 5159.4                         | 5992.1                    | 5992.1                                | 5813.8               |
32397 |  791   | 864.0                          | 1298.6                    | 1298.6                                | 912.5                |
45947 |  1723  | 1814.0                         | 2063.6                    | 2063.6                                | 1993.6               |

Gambar 8: Prediction Table
Berdasarkan tabel diatas, kita dapat membandingkan prediksi dari beberapa model regresi dan melihat seberapa baik mereka memprediksi nilai target untuk 10 data uji pertama.

**Cara Kerja Metrik Mean Squared Error**: 
- *Mean Squared Error* adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat. MSE menghitung rata-rata dari kuadrat perbedaan antara setiap pasangan nilai prediksi dan nilai sebenarnya.
- Semakin kecil nilai MSE, maka akan semakin baik pula model tersebut dalam melakukan prediksi nilai.

**Kesimpulan**
- Berdasarkan hasil training dan test, maka algoritma yang terbaik adalah *Extra Trees Regressor*, alasannya karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.
- Model telah good fit dalam melakukan akurasi, alasannya karena nilai MSE yang dihasilkan kurang dari 10% 0.054081 sedangkan 10% nilai MSE, yaitu 1155.7
- 10 % nilai MSE dihitung dengan rumus: mse_target = (home_data['price'].max() - home_data['price'].min()) * 10/100 
 
