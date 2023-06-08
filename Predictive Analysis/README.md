# *Predictive Analysis Submission*
## *Business Understanding*
## *Data Understanding*
Data yang digunakan adalah dataset yang bersumber dari situs Github yang berisi dataset terkait Diamonds Price. Dataset yang digunakan dapat didownload pada link berikut ini:(https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv). Jumlah data yang terdapat didalam file tersebut sebanyak 53940 data.

### Variabel-variabel yang terdapat dalam dataset Diamonds:
- carat 
- cut
- color 
- clarity
- depth 
- table
- price
- x
- y
- z

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

### **Hasil Exploratory Data Analysis**

![alt text](https://github.com/randiijulian/Machine-Learning-Terapan-Dicoding/blob/main/Predictive%20Analysis/Images/cut.png?raw=true)

Gambar 1: visualisasi variabel cut dengan menggunakan histogram

Berdasarkan hasil visualisasi, kategori ideal pada kolom cut memiliki nilai terginggi dibandingkan dengan kategori lainnya.

![image](https://user-images.githubusercontent.com/122204998/215275641-df70eac8-b271-4935-b5ee-b4c28e2f21aa.png)

Gambar 2: visualisasi variabel days_left dengan menggunakan boxplot

Berdasarkan hasil visualisasi, tidak terdapat outliers dalam variabel days_left.

![image](https://user-images.githubusercontent.com/122204998/215275715-4455ce36-d97b-4919-b969-07ad60d44acc.png)

Gambar 3: univariate analysis pada variabel airline

Berdasarkan hasil visualisasi, maskapai penerbangan vistara memiliki jumlah data yang paling banyak dibandingkan dengan masakapai penerbangan lainnya, sedangkan maskapai penerbangan SpiceJet memiliki jumlah data yang paling sedikit dibandingkan dengan maskapai penerbangan lainnya.

![image](https://github.com/randiijulian/Machine-Learning-Terapan-Dicoding/blob/main/Predictive%20Analysis/color.png?raw=true)

Gambar 4: univariate analysis pada variabel source_city

Berdasarkan hasil visualisasi, Delhi memiliki jumlah data yang paling banyak dibandingkan dengan kota keberangkatan lainnya, sedangkan Chennai memiliki jumlah data yang paling sedikit dibandingkan dengan kota keberangkatan lainnya.

![image](https://user-images.githubusercontent.com/122204998/215276030-75013578-016d-4d3b-94cf-da7fe78773d1.png)

Gambar 5: univariate analysis pada variabel departure_time

Berdasarkan hasil visualisasi, waktu keberangkatan pagi (morning) memiliki jumlah data yang paling banyak dibandingkan dengan kota keberangkatan lainnya, namun masih relatif seimbang, kecuali waktu keberangkatan tengah malam memiliki jumlah data yang sangat sedikit dibandingkan dengan waktu keberangkatan lainnya.

![image](https://user-images.githubusercontent.com/122204998/215276157-c79c42f4-555d-45c8-ab5c-b8197aaaf718.png)

Gambar 6: univariate analysis pada variabel destination_city

Berdasarkan hasil visualisasi, waktu keberangkatan pagi (morning) memiliki jumlah data yang paling banyak dibandingkan dengan kota keberangkatan lainnya, namun masih relatif seimbang, kecuali waktu keberangkatan tengah malam memiliki jumlah data yang sangat sedikit dibandingkan dengan waktu keberangkatan lainnya.

![image](https://user-images.githubusercontent.com/122204998/215276300-e37a7db7-8f6e-4e12-b292-c422cf019d08.png)

Gambar 7: univariate analysis pada variabel class

Berdasarkan hasil visualisasi, kelas ekonomi mendominasi jumlah data di dalam dataset, dibandingkan dengan kelas bisnis.

![image](https://user-images.githubusercontent.com/122204998/215276447-0869bef6-e328-41f0-9258-47fbe7260974.png)

Gambar 8: univariate analysis pada stops, duration, variabel days_left, price dengan menggunakan histogram

Berdasarkan hasil visualisasi, maka dapat dibuat kesimpulan sebagai berikut:
- kebanyakan pesawat melakukan transit sebanyak satu kali.
- semakin cepat waktu penerbangan, maka harga tiket pesawat semakin mahal.
- variabel days_left tidak begitu berpengaruh pada harga tiket pesawat.

![image](https://user-images.githubusercontent.com/122204998/215325509-8f151876-8200-4db2-b8fc-77759423de7d.png)

Gambar 9: multivariate analysis antara variabel airline dengan price

Berdasarkan hasil visualisasi, variabel airline memiliki korelasi yang kuat terhadap price.

![image](https://user-images.githubusercontent.com/122204998/215325764-55e8913b-14f3-49b2-8b07-6646cc08a379.png)

Gambar 10: multivariate analysis antara variabel source_city dengan price

Berdasarkan hasil visualisasi, variabel source city kurang memiliki korelasi terhadap price.

![image](https://user-images.githubusercontent.com/122204998/215325834-fae3b485-55bf-4e11-b61a-60a3cdd993b0.png)

Gambar 11: multivariate analysis antara variabel departure_time dengan price

Berdasarkan hasil visualisasi, variabel departure_time cukup memiliki korelasi terhadap price.

![image](https://user-images.githubusercontent.com/122204998/215325927-c2e1f93b-f6de-4eb4-adf4-ddf382d952cb.png)

Gambar 12: multivariate analysis antara variabel arrival_time dengan price

Berdasarkan hasil visualisasi, variabel arrival_time cukup memiliki korelasi terhadap price.

![image](https://user-images.githubusercontent.com/122204998/215326002-60fecf19-efc5-4213-813b-ab022cff7bef.png)

Gambar 13: multivariate analysis antara variabel destination_city dengan price

Berdasarkan hasil visualisasi, variabel destination_city kurang memiliki korelasi terhadap price.

![image](https://user-images.githubusercontent.com/122204998/215326095-7fde0672-65cd-4773-b75a-870225f74455.png)

Berdasarkan hasil visualiasi, variabel class memiliki korelasi yang kuat terhadap price.

![multivariate numerical variable](https://user-images.githubusercontent.com/122204998/215327836-cbe9e62d-b87d-499c-a7df-052ae29507f1.gif)

Gambar 13: multivariate analysis variabel stops, duration, days_left terhadap price

Berdasarkan hasil visualiasi, dapat dibuat kesimpulan bahwa variabel stops, duration dan days_left kurang memiliki korelasi dengan price.

![correlation matrix](https://user-images.githubusercontent.com/122204998/215327123-a9d84239-f9c7-467a-b853-7eceb68719fe.jpg)

Gambar 14: Correlation Matrix

Bila kita lihat, bahwa korelasi variabel stops terhadap price = 0.12, korelasi variabel duration terhadap price = 0.22, sedangkan korelasi variabel days_left terhadap price sebesar 0.09.

**Proses *Data Preparation***: 
- Proses data preparation dilakukan melalui langkah-langkah, yaitu sebagai berikut: Melakukan *load* data pada *google colaboratory*, kemudian melakukan analisis awal terkait variabel yang sangat tidak relevan untuk diproses lebih lanjut. Selanjutnya, memahami makna-makna variabel dengan menerapkan *Exploratory Data Analysis*, kemudian melakukan visualisasi data untuk mencari outlier dengan menggunakan *boxplot* dari *library seaborn*. Selanjutnya, menerapkan metode IQR untuk mengeliminasi outlier, kemudian menggunakan *univariate analysis* serta *multivariative analysis*. Selanjutnya membuat *correlation matrix*, kemudian membuang variabel numberik yang memiliki korelasi rendah terhadap variabel *price.*
- Data preparation diperlukan agar data yang akan diproses oleh algoritma *machine learning* bebas dari *outlier* dan variabel-variabel yang digunakan untuk algoritma adalah variabel yang memiliki korelasi tinggi terhadap penentuan prediksi harga tiket pesawat.
- Pembuatan aplikasi ini menggunakan IQR *(Interquartile Range)* untuk mengeliminasi *outlier* yang terdapat dalam dataset *flight price prediction*.
### *Exploratory Data Analysis*
#### *Exploratory Data Analysis - Data Cleansing*
#### *Exploratory Data Analysis - Univariate Analysis*
#### *Exploratory Data Analysis - Multivariate Analysis*
### *Splitting Data*
## *Modeling*
## *Evaluation*
Tabel 1: Hasil Evaluasi Model dengan Menggunakan Mean Squared Error
Model                        | train        | test	        |
---------------------------- | -----------  | ------------ |
Extra Trees Regressor        | 0.054081 	   | 149.967816   |
Lasso Regression             | 558.32874	   | 555.515268   |
Lasso Least Angle Regression | 558.328177   | 555.515686   |
Elastic Net                  | 837.14892    | 831.40399    |
- Metrik yang digunakan untuk mengukur hasil *training* adalah *mean squared error (MSE)*. 
- Berdasarkan hasil training, bahwa model *Extra Trees Regressor* menghasilan nilai MSE pada saat *training* = 0.054081 dan pada saat tes = 149.967816. 
- Berdasarkan hasil training model, maka ditetapkan bahwa algoritma yang terbaik diantara *Extra Trees Regressor* sedangkan *Lasso Regression* dan *Lasso Least Angle Regression* memiliki performa yang tidak terpaut jauh dalam memprediksi harga diamonds, yaitu algoritma *Extra Trees Regressor*.
- Alasannya, karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.

**Cara Kerja Metrik Mean Absolute Error**: 
- *Mean Squared Error* adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat. MSE menghitung rata-rata dari kuadrat perbedaan antara setiap pasangan nilai prediksi dan nilai sebenarnya.
- Semakin kecil nilai MSE, maka akan semakin baik pula model tersebut dalam melakukan prediksi nilai.

**Kesimpulan**
- Berdasarkan hasil training dan test, maka algoritma yang terbaik adalah *Extra Trees Regressor*, alasannya karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.
- Model telah good fit dalam melakukan akurasi, alasannya karena nilai MSE yang dihasilkan kurang dari 10% 0.054081 sedangkan 10% nilai MSE, yaitu 1155.7
- 10 % nilai MSE dihitung dengan rumus: mse_target = (home_data['price'].max() - home_data['price'].min()) * 10/100 
 
