# -*- coding: utf-8 -*-
"""Predictive Analysis Submission.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_xq6TceIwXKNnKTk4fyCmwFWnxEnYxWR

Nama : Randi Julian Saputra

Github : github.com/randiijulian

Dataset : kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor

## Project Submission 1 Dicoding Machine Learning Terapan
Predictive Analysis

---

**Connect to drive**
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan"

"""**Import needed library and module**"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import os
import seaborn as sns

from google.colab import drive
from google.colab import data_table
from sklearn.metrics import mean_absolute_error

!pip install pycaret #Install Pycaret For references using models

"""**Load Dataset**
Install kaggle and using kaggle API for import public dataset from kaggle
"""

# !pip install -U -q kaggle # install kaggle for using kaggle
# !mkdir -p ~/.kaggle
# !cp /content/drive/MyDrive/kaggle.json ~/.kaggle/ # use API kaggle for import file from kaggle
# !kaggle datasets download -d thedevastator/jobs-dataset-from-glassdoor # download file from kaggle
# !ls

# !unzip \*.zip && rm *.zip

"""## Data Preparation

Deskripsi variabel pada dataset
"""

import pandas as pd
url = 'https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv'
home_data = pd.read_csv(url)
home_data

# home_data = pd.read_csv("/content/drive/MyDrive/Uni Life's/ML Dicoding/ML Terapan/salary_data_cleaned.csv")
# # home_data.drop(['Unnamed: 0', 'flight'], axis = 1, inplace = True)

home_data.head()

home_data.info()

home_data.describe()

"""### pycaret setup models"""

from pycaret.regression import * #Setup Models
setup = setup(home_data, target = 'price', session_id = 123)

best = compare_models() #Run models for references

"""Melihat seluruh algoritma regresi yang ada dan melakukan perbandingan algoritma yang menghasilkan performa yang bagus berdasarkan kesesuaian dengan data yang digunakan. Berdasarkan hasil dari perbandingan model tersebut, maka proyek ini akan menggunakan algoritma Extra Trees Regressor serta menggunakan Lasso Regression.

### Exploratory Data Analysis

#### Exploratory Data Analysis - Data Cleansing

melakukan pengecekan missing value pada data
"""

for col in home_data.columns: #Hitung missing value setiap kolom
  print("Kolom : {} memiliki nilai NaN sebanyak {} dari {} row".format(col, 
                         str(home_data[col].isna().sum()), 
                         str(len(home_data.index))))

"""melakukan pengecekan value bernilai 0 pada data"""

for col in home_data.columns: #Cek yang bernilai 0
  print("Kolom : {} memiliki nilai 0 sebanyak {} dari {} row".format(col, 
                         str((home_data[col]==0).sum()), 
                         str(len(home_data.index))))

home_data.isnull().sum()

home_data.loc[(home_data['z']==0)]

"""drop nilai 0 yang terdapat pada kolom x, y, z dan melakukan pengecekan ukuran data untuk memastikan baris sudah di drop"""

home_data = home_data.loc[(home_data[['x','y','z']]!=0).all(axis=1)]
home_data.shape

"""#### Exploratory Data Analysis - Univariate Analysis"""

Q1 = home_data.quantile(0.25)
Q3 = home_data.quantile(0.75)
IQR=Q3-Q1
home_data=home_data[~((home_data<(Q1-1.5*IQR))|(home_data>(Q3+1.5*IQR))).any(axis=1)]

# Cek ukuran dataset setelah kita drop outliers
home_data.shape

numerical_features = ['price', 'carat', 'depth', 'table', 'x', 'y', 'z']
categorical_features = ['cut', 'color', 'clarity']

import matplotlib.pyplot as plot

feature = categorical_features[0]
count = home_data[feature].value_counts()
percent = 100*home_data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature, color="green");

feature = categorical_features[1]
count = home_data[feature].value_counts()
percent = 100*home_data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature, color="green");

home_data.hist(bins=50, figsize=(20,15), color="green")
plot.show()

"""#### Explotaroty Data Analysis - Multivariate Analysis"""

cat_features = home_data.select_dtypes(include='object').columns.to_list()
import seaborn as sns
for col in cat_features:
  sns.catplot(x=col, y="price", kind="bar", dodge=False, height = 4, aspect = 3,  data=home_data, palette="Set3")
  plot.title("Rata-rata 'price' Relatif terhadap - {}".format(col))

sns.pairplot(home_data, diag_kind = 'kde')

"""Melakukan visualisasi correlation matrix untuk melihat tingkat keterkaitan antar variabel"""

plot.figure(figsize=(10, 8))
correlation_matrix = home_data.corr().round(2)
# annot = True to print the values inside the square
color = sns.light_palette("green")
sns.heatmap(data=correlation_matrix, annot=True, cmap=color, linewidths=0.5, )
plot.title("Correlation Matrix untuk Fitur Numerik ", size=20)

home_data.drop(['depth'], inplace=True, axis=1)
home_data.head()

"""### One Hot Encoder"""

from sklearn.preprocessing import OneHotEncoder
home_data = pd.concat([home_data, pd.get_dummies(home_data['cut'], prefix='cut', drop_first=True)],axis=1)
home_data = pd.concat([home_data, pd.get_dummies(home_data['color'], prefix='color', drop_first=True)],axis=1)
home_data = pd.concat([home_data, pd.get_dummies(home_data['clarity'], prefix='clarity', drop_first=True)],axis=1)
home_data.drop(['cut','color','clarity'], axis=1, inplace=True)
home_data.head()

"""#### Splitting Dataset
Melakukan split data sebelum dilakukannya modeling
"""

from sklearn.model_selection import train_test_split
 
X = home_data.drop(["price"],axis =1)
y = home_data["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

from sklearn.decomposition import PCA
 
pca = PCA(n_components=3, random_state=123)
pca.fit(X_train[['x','y','z']])
princ_comp = pca.transform(X_train[['x','y','z']])

pca.explained_variance_ratio_.round(3)

sns.pairplot(X_train[['x','y','z']], plot_kws={"s": 3});

from sklearn.decomposition import PCA
pca = PCA(n_components=1, random_state=123)
pca.fit(X_train[['x','y','z']])
X_train['dimension_index'] = pca.transform(X_train.loc[:, ('x','y','z')]).flatten()
X_train.drop(['x','y','z'], axis=1, inplace=True)
X_train.head()

from sklearn.decomposition import PCA
# pca = PCA(n_components=1, random_state=123)
# pca.fit(X_test[['x','y','z']])
X_test['dimension_index'] = pca.transform(X_test.loc[:, ('x','y','z')]).flatten()
X_test.drop(['x','y','z'], axis=1, inplace=True)
X_test.head()

from sklearn.preprocessing import StandardScaler
 
numerical_features = ['carat', 'table', 'dimension_index']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()
X_test.loc[:, numerical_features]= scaler.transform(X_test[numerical_features])

X_train[numerical_features].describe().round(4)

"""## Modeling
Melakukan modeling dengan membandingkan beberapa algoritma yang digunakan

#### Extra Trees Regressor
Melakukan modeling menggunakan algoritma Extra Trees Rergressor
"""

#Import Necessary Library
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error

ETree_regressor = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the regressor to the training data
ETree_regressor.fit(X_train, y_train)

# Predict on the test data
y_pred = ETree_regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error Extra Trees:", mse)

"""#### Lasso Regression
Melakukan modeling menggunakan algoritma Lasso Regression
"""

#Import Necessary Library
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Initialize the Lasso regression model
lasso = Lasso(alpha=0.1, random_state=42)

# Fit the model to the training data
lasso.fit(X_train, y_train)

# Predict on the test data
y_pred = lasso.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error Lasso:", mse)

"""#### Lasso Least Angle Regression
Melakukan modeling menggunakan algoritma Lasso Least Angle Regression
"""

#Import Necessary Library
from sklearn.linear_model import LassoLars
from sklearn.metrics import mean_squared_error

# Initialize the LassoLars regression model
lasso_lars = LassoLars(alpha=0.1)

# Fit the model to the training data
lasso_lars.fit(X_train, y_train)

# Predict on the test data
y_pred = lasso_lars.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error Lasso Least Angle:", mse)

"""#### Elastic Net
Melakukan modeling menggunakan algoritma Elastic Net
"""

#Import Necessary Library
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error

# Initialize the Elastic Net regression model
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)

# Fit the model to the training data
elastic_net.fit(X_train, y_train)

# Predict on the test data
y_pred = elastic_net.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error Elastic Net:", mse)

"""#### Lasso Net"""

# !pip install pycox

# !pip install lassonet

# #Import Necessary Library
# from lassonet import LassoNetCoxRegressorCV
# from sklearn.metrics import mean_squared_error

# # Initialize the Lasso Net regression model
# lasso_net = LassoNetCoxRegressorCV(cv=5, random_state=42)

# # Fit the model to the training data
# lasso_net.fit(X_train, y_train)

# # Predict on the test data
# y_pred = lasso_net.predict(X_test)

# # Evaluate the model
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse)

"""#### Network Lasso"""

# !python2 -m pip install network_lasso

# import networkx as nx
# import numpy as np
# from network_lasso import NetworkLasso

# # Create a random graph
# G = nx.erdos_renyi_graph(20, 0.2, seed=42)

# # Generate random node features
# X = np.random.rand(G.number_of_nodes(), 5)

# # Generate random target values
# y = np.random.rand(G.number_of_nodes())

# # Create the adjacency matrix
# adj_matrix = nx.to_numpy_array(G)

# # Initialize Network Lasso regression model
# netlasso = NetworkLasso(alpha=0.1, gamma=0.5)

# # Fit the model to the data
# netlasso.fit(X, y, adj_matrix)

# # Predict on new data
# y_pred = netlasso.predict(X, adj_matrix)

# # Print the predicted values
# print("Predicted values:", y_pred)

"""## Evaluation"""

mse = pd.DataFrame(columns=['train', 'test'], index=['Extra Trees Regressor','Lasso Regression','Lasso Least Angle Regression', 'Elastic Net'])
model_dict = {'Extra Trees Regressor': ETree_regressor, 'Lasso Regression': lasso, 'Lasso Least Angle Regression': lasso_lars, 'Elastic Net': elastic_net}
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
 
mse

fig, ax = plot.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

prediksi = X_test.iloc[:10].copy()
pred_dict = {'y_true':y_test[:10]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)