#Simple Linear Regression


#FirstStep: Preprocess Data
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#Import dataset

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

#Splitting dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)

#Fitting Simple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
#Second thing we created an object of the class SK Learn
#we created an object of class Linear Regression
#Fitting Simple Linear Regression to the Training Set
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
#We use fit method to fit simple linear regressor to our training set thereby simple linear regressor learned the correlations
#set to predict the dependent variable (salary) BASED on independent variable (years of experience)


#Predicting the test set results
#create a vector containing of predicted salaries into a single vector called y_pred
# y_pred is vector prediction of dependent variables (predicted salaries of test sets)

#y_pred is the predictions of the x_test set
y_pred = regressor.predict(X_test)


#Visualising the Training Set Results, Plugging real data
plt.scatter(X_train,Y_train, color = "red")
#Plot prediction/regression line
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
#Improve our visualisation
plt.title('Salary Vs Experience (Training Set)')
plt.xlabel('Years of Exeperience')
plt.ylabel('Salary')
plt.show()


#Visualising test-set results
plt.scatter(X_test,Y_test, color = "red")
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('Salary Vs Experience (Training Set)')
plt.xlabel('Years of Exeperience')
plt.ylabel('Salary')
plt.show()
