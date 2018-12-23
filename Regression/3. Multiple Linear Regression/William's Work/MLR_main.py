# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:57:31 2018

@author: William X Nguyen
"""

#Set the working directory
#Prepare the datasets

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

#Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values #removes last column
Y = dataset.iloc[:,4].values

#Need to encode State Independent variable since it is a categorical variable 
#Encoding Independent Variable must be done before splitting
#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() 
X[:,3] = labelencoder_X.fit_transform(X[:,3])
#This changes the text to numbers
#They need to numbers to create dummy variables 
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding Dummy Variable Trap
X = X[:,1:] #taking columns from index 1 to rest to avoid trap
#Next time no need to do this since library takes care of this

#Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state=0)
#Using 20% for testing 

#No need to apply feature scaling to multiple linear regressions since library takes care of that
#Fitting MLR to the Training Set after data-preprocessing 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
#We created an object of the class LinearRegression, regressor is the object
#Fit this object to training set
regressor.fit(X_train, Y_train)

#Testing performance of MLR in test sets
#Predicting the Test set results 
#Create vector of predictions
y_pred = regressor.predict(X_test) 
#we are going to compare real profits and predicted profits with our ten observations
#Y_test contains real profits, y_pred vector predictions based on our model 

#Building the optimal model using Backward Elimination (Prepation Step)
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis=1)
#Backward Elimination
#Creating new matrix of optimal features, indepdent variables having high impact on profit
#Writing the index of each column in X since we're removing the index at each step after
X_opt = X[:,[0,1,2,3,4,5]]
#Fitting MLR model to our future optimal matrix features X n Y
#Creating a new regressor from statsmodel library. Don't use same regressor from linear regre lib
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
#Above, we are fitting OLS to x_opt and y

#Now we are finding the p_values
#The lower the P_Value, the more significant your independent variable will be
regressor_OLS.summary() 

#Repeat to keep removing variables with p_values>0.05
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()






















