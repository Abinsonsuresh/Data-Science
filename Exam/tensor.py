from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

import tensorflow as tf
import matplotlib.pyplot as plt

digits = load_digits()

x=digits.images
y=digits.target

x=x/16.0

x= x.reshape(-1,8,8,1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

plt.figure(figsize=(10,5))

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(digits.images[i],cmap='gray')
    plt.title(y[i])
    plt.axis('off')


plt.show()
