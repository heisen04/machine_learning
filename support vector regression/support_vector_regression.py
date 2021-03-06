#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:07:26 2017

@author: heisenberg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_dataset():
    global dataset, X, Y
    dataset = pd.read_csv("Position_Salaries.csv")
    X = dataset.iloc[:, 1:2].values
    Y = dataset.iloc[:, 2:3].values #.reshape(-1,1)
    
def scale_data():
    global X, Y, sc_x, sc_y
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    sc_x.fit(X)
    sc_y.fit(Y)
    X = sc_x.transform(X)
    Y = sc_y.transform(Y)

def create_train_model():
    global regressor
    from sklearn.svm import SVR
    regressor = SVR(kernel='rbf')
    regressor.fit(X, Y)

def predict_values(value):
    value = sc_x.transform(np.array(value))
    pred = sc_y.inverse_transform(regressor.predict(value))
    print(pred)
    
def plot_graph():
    plt.scatter(X, Y, color = 'blue')
    x_grid = np.arange(min(X), max(X), 0.01)
    x_grid = x_grid.reshape(len(x_grid), 1)
    plt.plot(x_grid, regressor.predict(x_grid), color = 'red')
    plt.title('Truth or Bluff (SVR)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    #plt.show()
    
load_dataset()
scale_data()
create_train_model()
predict_values(6.5)
plot_graph()