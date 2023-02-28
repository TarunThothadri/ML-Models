# -*- coding: utf-8 -*-
"""Lasso Regression Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cGZTbCFoSfUx8ACt_FO_t6RWFQMoS1FP

Model - Lasso Regression
"""

import numpy as np

class Lasso_Regression():
  #initiate hyperparameters
  def __init__(self,learning_rate,no_of_iterations,lambdap):
    self.learning_rate=learning_rate
    self.no_of_iterations=no_of_iterations
    self.lambdap=lambdap


  def fit(self,X,Y):
    #no of datapoints and features
    self.m,self.n =X.shape

    #weight and bias
    self.w = np.zeros(self.n)
    self.b = 0

    #X and Y
    self.X = X
    self.Y = Y

    for i in range(self.no_of_iterations):
      self.update_weights()


  def update_weights(self):
    Y_prediction = self.predict(self.X)

    #initiating dw
    dw = np.zeros(self.n)

    #gradients
    for i in range(self.n):
      if(self.w[i]>0):
        dw[i] = -((2*(self.X[:,i].dot(self.Y-Y_prediction)+self.lambdap))/self.m)

      else:
        dw[i] = -((2*(self.X[:,i].dot(self.Y-Y_prediction)-self.lambdap))/self.m)

    db = dw[i] = -(2*(np.sum(self.Y-Y_prediction))/self.m)
    
    self.w = self.w - self.learning_rate*dw
    self.b = self.b - self.learning_rate*db


  def predict(self,X):
    output = np.dot(X,self.w) + self.b
    return output