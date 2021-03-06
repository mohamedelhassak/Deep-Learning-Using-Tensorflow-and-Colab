# -*- coding: utf-8 -*-
"""tuto1-ann breast cancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bwyf36gygvlqyctON5GXA6nSRreGjhrf
"""

## Import packages
 from sklearn import datasets
 import numpy as np
 import tensorflow as tf
 from sklearn.preprocessing import StandardScaler
 from sklearn.model_selection import train_test_split

## load data 
df  = datasets.load_breast_cancer()

## Exploryy data
print(df.DESCR)

df.data.shape

## prepare data 
X = df.data
y = df.target

## standarized data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled

X_train, X_test, y_train, y_test = train_test_split(X_scaled,y, test_size=0.2, random_state=42)

X_train.shape

## Build Neural Network

### Create model
model = tf.keras.models.Sequential()

## add layers
### add one hidden layer of 15 units
model.add(tf.keras.layers.Dense(units=15,activation='relu',kernel_initializer='uniform',input_dim=30))
### add input layer of 1 unit
model.add(tf.keras.layers.Dense(units=1,activation='sigmoid',kernel_initializer='uniform'))

## compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

## summary model
model.summary()

## training our model
 model.fit(X_train,y_train,batch_size=16,epochs=100)

##evaluate  model on test set
test_loss ,test_acc  = model.evaluate(X_test,y_test)

print(f'test loss {test_loss} and test accuracy {test_acc}')

