# -*- coding: utf-8 -*-
"""Recommender System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tCZHDvDlaffFf9zTS-i--8zErtSnEbDH

Nama : Randi Julian Saputra

Github : github.com/randiijulian

Dataset :

## Project Submission 2 Dicoding Machine Learning Terapan
**Recommender System**

---

Pada project Machine Learning saya membuat Recommender System mengenai pencarian buku berdasarkan preferensi pengguna dan rating yang diberikan pengguna sebelumnya. Perpustakaan sudah merambah ke ranah digital. Keberadaan sistem informasi perpustakaan di perguruan tinggi dapat  dirasakan telah  memudahkan para  pengunjung, baik mahasiswa maupun dosen, dalam  mencari bahan referensi yang  menjadi  koleksi perpustakaan  dimaksud.

Proyek ini berguna ketika pengunjung perpustakaan kampus menelusuri judul buku dan judul buku terkait tidak tersedia dan tidak adanya rekomendasi untuk buku-buku lain   yang mungkin menarik untuk dibaca atau bahkan dibutuhkan  sebagai pelengkap dari judul buku yang diinginkan, maka peran sistem rekomendasi disini sangat dibutuhkan. Rekomendasi tersebut bisa berdasarkan preferensi pengunjung dan rating yang diberikan pengunjung sebelumnya.

[Referensi terkait](http://jurnal.iaii.or.id/index.php/RESTI/article/view/971/158)

**Connect to drive**
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System"

"""**Import needed library and module**"""

!pip install tensorflow

"""**Load Dataset**
Install kaggle and using kaggle API for import public dataset from kaggle
"""

!pip install -U -q kaggle # install kaggle for using kaggle
!mkdir -p ~/.kaggle
!cp /content/drive/MyDrive/kaggle.json ~/.kaggle/ # use API kaggle for import file from kaggle
# download file from kaggle and place to folder dataset
!kaggle datasets download -d arashnic/book-recommendation-dataset -p "/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset"
!ls

# unzip file and place to folder dataset
!unzip "/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset/book-recommendation-dataset.zip" -d "/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset/"

"""## Data Understanding

---

### Atribut Tiap Dataset

#### Book Atribute
"""

import pandas as pd
book = pd.read_csv("/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset/Books.csv")
book

"""Deskripsi variabel pada dataset"""

#Melihat rangkuman dan deskripsi dataset
book.info()
book.describe()

"""#### Rating Atribute"""

import pandas as pd
rating = pd.read_csv("/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset/Ratings.csv")
rating

rating.info()
rating.describe()

"""#### User Atribute"""

import pandas as pd
user = pd.read_csv("/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/Recommender System/Dataset/Users.csv")
user

#mengambil sampel dataset yang akan dilakukan training dan evaluasi sebanyak 25% dari tiap-tiap dataset yang ada
book = book.sample(frac=0.25)
user = user.sample(frac=0.25)
rating = rating.sample(frac=0.25)

#Melihat rangkuman dan deskripsi dataset
user.info()
user.describe()

# Drop Image Url pada dataset
book = book.drop(columns=['Image-URL-S','Image-URL-M','Image-URL-L'], axis=0)
book

#drop nilai NaN pada tiap dataset
book.dropna(inplace=True)
rating.dropna(inplace=True)
user.dropna(inplace=True)

#menampilkan dataset users
user

#menampilkan dataset rating
rating

#menampilkan dataset book
book

"""## Data Preparation

---

### Data Preprocessing
"""

#mengubah nama pada kolom User-ID menjadi UserId karena tidak sesuai format inisasi variabel
dict = {'User-ID': 'UserId'
        }
# call rename () method
user.rename(columns=dict,
          inplace=True)

#mengubah nama pada kolom User-ID menjadi UserId karena tidak sesuai format inisasi variabel
dict = {'User-ID': 'UserId'
        }
# call rename () method
rating.rename(columns=dict,
          inplace=True)

#Impor library numpy
import numpy as np
# Menggabungkan seluruh ISBN pada tabel users dan rating
book_n_rating = np.concatenate((
    book.ISBN.unique(),
    rating.ISBN.unique(),
))

# Mengurutkan data dan menghapus data yang sama
book_n_rating = np.sort(np.unique(book_n_rating))
print('Jumlah seluruh data buku berdasarkan ISBN: ', len(book_n_rating))

# Menggabungkan seluruh userID
user_all = np.concatenate((
    user.UserId.unique(),
    rating.UserId.unique(),
))

# Menghapus data yang sama kemudian mengurutkannya
user_all = np.sort(np.unique(user_all))

print('Jumlah seluruh user: ', len(user_all))

# Menggabungkan dataframe rating dengan book_recommendation berdasarkan nilai ISBN
book_fix = pd.merge(rating, book , on='ISBN', how='left')
book_fix

# Cek missing value dengan fungsi isnull()
book_fix.isnull().sum()

#grup ISBN
book_fix.groupby('ISBN').sum()

# Definisikan dataframe rating ke dalam variabel book_rate
book_rate = rating
book_rate

#menampilkan dataset book_fix
book_fix

#mengubah nama pada kolom dataset book_fix
dict = {'Book-Rating': 'rate',
        'Book-Title': 'title',
        'Book-Author': 'author',
        'Year-Of-Publication': 'year',
        'Publisher':'publisher'
        }
# call rename () method
book_fix.rename(columns=dict,
          inplace=True)

#menampilkan data pada tabel book_fix
book_fix

# Menggabungkan book_rate dengan dataframe book_fix berdasarkan ISBN
all_book_name = pd.merge(book_rate, book_fix[['ISBN','title','publisher']], on='ISBN', how='left')

# Print dataframe all_book_name
all_book_name

#inisiasi variabel baru
book_all_fix = all_book_name
book_all_fix

# Mengecek missing value pada dataframe book_all_fix
book_all_fix.isnull().sum()

# Membersihkan missing value dengan fungsi dropna()
book_clean_fix = book_all_fix.dropna()
book_clean_fix

# Mengecek kembali missing value pada variabel book_clean_fix
book_clean_fix.isnull().sum()

# Mengurutkan buku berdasarkan ISBN kemudian memasukkannya ke dalam variabel fix_book_all
fix_book_all = book_clean_fix.sort_values('ISBN', ascending=True)
fix_book_all

# Mengecek berapa jumlah fix_book_all berdasarkan ISBN
len(fix_book_all.ISBN.unique())

# Mengecek berapa jumlah fix_book_all berdasarkan publisher
len(fix_book_all.publisher.unique())

dict = {'Book-Rating': 'rate'}
# call rename () method
fix_book_all.rename(columns=dict,
          inplace=True)

#menampilkan dataset
fix_book_all

#mengetahui rating buku lebih dari 8
fix_book_all[fix_book_all['rate'] >= 8]

# Membuat variabel preparation yang berisi dataframe fix_book_all kemudian mengurutkan berdasarkan ISBN
preparation = fix_book_all
preparation.sort_values('ISBN')

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('ISBN')
preparation

# Mengonversi data series 'ISBN' menjadi dalam bentuk list
book_isbn = preparation['ISBN'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
book_title = preparation['title'].tolist()

# Mengonversi data series ‘publisher’ menjadi dalam bentuk list
book_publisher = preparation['publisher'].tolist()

#cetak total
print(len(book_isbn))
print(len(book_title))
print(len(book_publisher))

# Membuat dictionary untuk data ‘book_id’, ‘book_name’, dan ‘cuisine’
book_new = pd.DataFrame({
    'isbn': book_isbn,
    'title': book_title,
    'publisher': book_publisher
})
book_new

"""## Modeling

---


Melakukan modeling dengan membandingkan beberapa algoritma yang digunakan

### Content Based Filtering
"""

#inisiasi variabel baru
data = book_new

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(data['publisher'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['publisher'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

#membuat dataframe baru berdasarkan fitur yang ada dan vektor tf-idf yang telah diubah dengan fungsi todense()
pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data
).sample(22, axis=1).sample(10, axis=0)

from sklearn.metrics.pairwise import cosine_similarity
# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama buku
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['title'], columns=data['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap buku
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

def book_recommendations(nama_buku, similarity_data=cosine_sim_df, items=data[['title', 'publisher']], k=5):
        # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_buku].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_buku agar nama buku yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_buku, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

#cek apakah data berada dalam tabel yang telah diseleksi
data[data.title.eq('Hornet Flight: A Novel')]

# Mendapatkan rekomendasi buku yang mirip dengan Made in America
# book_recommendations('Hornet Flight: A Novel')

"""### Collaborative Filtering"""

# Commented out IPython magic to ensure Python compatibility.
# Import library
import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt
# %matplotlib inline

data = rating

data

#mengubah nama kolom Book-Rating menjadi rate
dict = {'Book-Rating': 'rate'}
# call rename () method
data.rename(columns=dict,
          inplace=True)
data

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = data['UserId'].unique().tolist()
print('list userID: ', user_ids)

# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

# Mengubah ISBN menjadi list tanpa nilai yang sama
book_ids = data['ISBN'].unique().tolist()

# Melakukan proses encoding ISBN
book_to_book_encoded = {x: i for i, x in enumerate(book_ids)}

# Melakukan proses encoding angka ke ISBN
book_encoded_to_book = {i: x for i, x in enumerate(book_ids)}

#Selanjutnya, petakan UserId dan ISBN ke dataframe yang berkaitan.

# Mapping UserId ke dataframe user
data['users'] = data['UserId'].map(user_to_user_encoded)

# Mapping ISBN ke dataframe book
data['book'] = data['ISBN'].map(book_to_book_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah buku
num_book = len(book_encoded_to_book)
print(num_book)

# Mengubah rating menjadi nilai float
data['rate'] = data['rate'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(data['rate'])

# Nilai maksimal rating
max_rating = max(data['rate'])

print('Number of User: {}, Number of Book: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_book, min_rating, max_rating
))

# Mengacak dataset
data = data.sample(frac=1, random_state=42)
data

# Membuat variabel x untuk mencocokkan data users dan book menjadi satu value
x = data[['users', 'book']].values

# Membuat variabel y untuk membuat rating dari hasil
y = data['rate'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * data.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_book, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_book = num_book
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.book_embedding = layers.Embedding( # layer embeddings book
        num_book,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.book_bias = layers.Embedding(num_book, 1) # layer embedding book bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    book_vector = self.book_embedding(inputs[:, 1]) # memanggil layer embedding 3
    book_bias = self.book_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_book = tf.tensordot(user_vector, book_vector, 2)

    x = dot_user_book + user_bias + book_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_book, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[[tf.keras.metrics.Precision(),tf.keras.metrics.Recall()]]
)

# Memulai training
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 64,
    epochs = 15,
    validation_data = (x_val, y_val)
)

# #Plot Precision dan recall dari data train dan test
# plt.plot(history.history['precision'])
# plt.plot(history.history['recall'])
# plt.title('model_metrics')
# plt.ylabel('precision and recall')
# plt.xlabel('epoch')
# plt.legend(['precision', 'recall'], loc='upper left')
# plt.show()

# #Plot Val precision dan recall dari data train dan test
# plt.plot(history.history['val_precision'])
# plt.plot(history.history['val_recall'])
# plt.title('model_metrics')
# plt.ylabel('val precision and recall')
# plt.xlabel('epoch')
# plt.legend(['precision', 'recall'], loc='upper left')
# plt.show()

#inisiasi variabel baru
book_df = book_new
# Mengambil sample user
user_id = data.UserId.sample(1).iloc[0]
book_visited_by_user = data[data.UserId == user_id]

# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
book_not_visited = book_df[~book_df['isbn'].isin(book_visited_by_user.ISBN.values)]['isbn']
book_not_visited = list(
    set(book_not_visited)
    .intersection(set(book_to_book_encoded.keys()))
)

#
book_not_visited = [[book_to_book_encoded.get(x)] for x in book_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_not_visited), book_not_visited)
)

#meratakan data rating untuk diprediksi
ratings = model.predict(user_book_array).flatten()

#top rating
top_ratings_indices = ratings.argsort()[-10:][::-1]

#rekomendasi buku
recommended_book_ids = [
    book_encoded_to_book.get(book_not_visited[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Book with high ratings from user')
print('----' * 8)

#mencari rekomendasi buku berdasarkan rating yang diberikan pengguna
top_book_user = (
    book_visited_by_user.sort_values(
        by = 'rate',
        ascending=False
    )
    .ISBN.values
)

book_df_rows = book_df[book_df['isbn'].isin(top_book_user)]
for row in book_df_rows.itertuples():
    print(row.title, ':', row.publisher)

print('----' * 8)
print('Top 10 book recommendation')
print('----' * 8)

#rekomendasi buku
recommended_book = book_df[book_df['isbn'].isin(recommended_book_ids)]
#fungsi perulangan untuk rekomendasi buku sebanyak 10 buah
for row in recommended_book.itertuples():
    print(row.title, ':', row.publisher)

"""## Evaluation

---

Melakukan evaluation terhadap beberapa model algoritma yang digunakan pada tahap modeling
"""

test_loss = model.evaluate(x_val, y_val)
print('\ nTest Loss: {}'.format(test_loss))

#Define precission and recall value
precision=0.6537
recall=0.3765

#count f_measuer
f_measure=2*(precision*recall)/(precision+recall)
print("F Measure =",f_measure)