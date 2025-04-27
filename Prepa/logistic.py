import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

"""
Logistic regression is a categorical ML algorithm

"""

X_train = pd.read_csv("train_X.csv")
Y_train = pd.read_csv("train_Y.csv")

X_train = X_train.drop("Id" , axis=1)
Y_train = Y_train.drop("Id" , axis=1)

X_train = (X_train.values).T
Y_train = Y_train.values
Y_train = Y_train.reshape(1 , X_train.shape[1])


print(X_train.shape , Y_train.shape)
def sigmoid(z):
    return (1/(1+ np.exp(-z) ))

def model(X , y , lr , iterations):
    m = X_train.shape[1]
    n = X_train.shape[0]
    B = 0 
    
    W = np.zeros((n,1))
    c = []
    for i in range (iterations):
         
        Z = np.dot(W.T,X) + B
        A = sigmoid(Z)
        
        cost = (-1/m)* np.sum(y* np.log(A) + (1-y)*np.log(1-A))
        dW = (1/m)* np.dot((A - y),X.T)
        dB = (1/m)*np.sum(A - y)
    
        W = W - lr*dW.T
        B = B - lr*dB
        
        c.append(c)
        
        if (i % 10 == 0):
            print(f"Le prix ) la {i}-ème itération est de {cost}")
        
    return W , B , c

W ,B , costs = model(X_train, Y_train , 0.005  , 10000)

