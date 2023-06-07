# *Predictive Analysis Submission*
## *Business Understanding*
## *Data Understanding*
## *Data Preparation*
## *Modeling*
## *Evaluation*
Tabel 1: Hasil Evaluasi Model dengan Menggunakan Mean Squared Error
Model                        |    train     |     test	    |
---------------------------- | -----------  | ------------ |
Extra Trees Regressor        |   0.054081 	 |  149.967816  |
Lasso Regression             |  558.32874	  |  555.515268  |
Lasso Least Angle Regression |  558.328177  |  555.515686  |
Elastic Net                  |  837.14892   |  831.40399   |
- Metrik yang digunakan untuk mengukur hasil *training* adalah *mean squared error (MSE)*. 
- Berdasarkan hasil training, bahwa model *Extra Trees Regressor* menghasilan nilai MSE pada saat *training* = 0.054081 dan pada saat tes = 149.967816. 
- Berdasarkan hasil training model, maka ditetapkan bahwa algoritma yang terbaik diantara *Extra Trees Regressor* sedangkan *Lasso Regression* dan *Lasso Least Angle Regression* memiliki performa yang tidak terpaut jauh dalam memprediksi harga diamonds, yaitu algoritma *Extra Trees Regressor*.\
- Alasannya, karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.

**Cara Kerja Metrik Mean Absolute Error**: 
- *Mean Squared Error* adalah metrik evaluasi yang digunakan untuk mengukur kesalahan antara nilai prediksi dan nilai sebenarnya dalam bentuk kuadrat. MSE menghitung rata-rata dari kuadrat perbedaan antara setiap pasangan nilai prediksi dan nilai sebenarnya.
- Semakin kecil nilai MSE, maka akan semakin baik pula model tersebut dalam melakukan prediksi nilai.

**Kesimpulan**
- Berdasarkan hasil training dan test, maka algoritma yang terbaik adalah *Extra Trees Regressor*, alasannya karena nilai *Mean Squared Error (MSE)* yang dihasilkan *Extra Trees Regressor* lebih baik dari algoritma lain yang digunakan.
- Model telah good fit dalam melakukan akurasi, alasannya karena nilai MSE yang dihasilkan kurang dari 10% 0.054081 sedangkan 10% nilai MSE, yaitu 1155.7
- 10 % nilai MSE dihitung dengan rumus: mse_target = (home_data['price'].max() - home_data['price'].min()) * 10/100 
 
