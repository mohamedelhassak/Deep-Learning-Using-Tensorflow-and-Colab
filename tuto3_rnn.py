# -*- coding: utf-8 -*-
"""tuto3- RNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bCJRS09GyPZKIGzGGsR7Vx5gKG589ns
"""

## import pacckages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

## load data
df = pd.read_csv('/content/AirPassengers.csv')
df.head()

data = df[['#Passengers']].values
data.shape

## preeprocessinh
sc = MinMaxScaler(feature_range=(0,1))

data_scaled = sc.fit_transform(data)

print('data max : ',data_scaled.max())

# split data
X_data = []
y_data = []

look_back =1

for i in range(len(data_scaled) -1):
  X_data.append(data_scaled[i:(i +look_back),0])
  y_data.append(data_scaled[i +look_back,0])

X_data, y_data = np.array(X_data), np.array(y_data)

X_data.shape

#reshaping
X_data = np.reshape(X_data,(X_data.shape[0],X_data.shape[1],1))
X_data.shape

y_data = np.reshape(y_data,(y_data.shape[0],1))
y_data.shape



## split data into Train and Test
tarin_size = int(len(X_data)*0.7)
test_size = len(X_data) - tarin_size

X_train = X_data[0:tarin_size,:]
X_test  = X_data[tarin_size:len(X_data),:]
y_train = y_data[0:tarin_size]
y_test  = y_data[tarin_size:len(X_data)]

X_train.shape

y_train.shape

X_test.shape

y_test.shape

## build model RNN
model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1],1)))
model.add(LSTM(units=50, return_sequences=True))
model.add(LSTM(units=50))

## output layerr
model.add(Dense(units=1))

## compile model
model.compile(optimizer='adam',
              loss='mean_squared_error')

model.summary()

## fiiting model
model.fit(X_train,y_train,batch_size=16, epochs=200)

## evaluate model
test_loss   = model.evaluate(X_test,y_test)

print(f'test loss {test_loss} ')

## plott result
plt.plot(y_test,color='red',label='nb passenger reel')
plt.plot(model.predict(X_test),color='green',label='nb passenger predicted')
plt.title('reel vs predicted')
plt.xlabel('temps')
plt.ylabel('Passenger')
plt.legend()
plt.show()

X_new = np.array([122,122])
X_new = np.reshape(X_new,(X_new.shape[0],1,1))

y_new_pred = model.predict(X_new)

y_new_pred

