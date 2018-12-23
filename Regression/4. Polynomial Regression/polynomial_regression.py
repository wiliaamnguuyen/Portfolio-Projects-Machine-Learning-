#Polynomial Regression

#DATA PREPROCESSING
#Import the libaries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#Importing the dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2:].values

#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

#Fitting Polynomial Regression to the dataset
#Below polymorphic object is a transformer tool 
#that will transform our matrix of features X into 
#a new matrix of features named X_poly
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly,Y)

#Once this new matrix of polynomial features X_poly was created
#Near linear regression object that we fitted to this new matrix X_poly and Y
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,Y)

#Visualising the Linear Regression Results
plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg.predict(X),color="blue")
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show

#Make a better model by visualising polynomial regression results
X_grid = np.arange(min(X), max(X),0.1)
#This gives us a vector, but we want a matrix
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y,color= "red")
plt.plot(X_grid,lin_reg_2.predict(poly_reg.fit_transform(X_grid)),color="blue")
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

#Predicting a new result with Linear Regression
#Employee previous level 6.5, results below code 330K, not best model
lin_reg.predict(6.5)

#Predicting a new result with Polynomial Regression
#Results if 158k, thus what employee said is true
lin_reg_2.predict(poly_reg.fit_transform(6.5))



