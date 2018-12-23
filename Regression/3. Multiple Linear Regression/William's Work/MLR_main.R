#Data preprocessing template

#Importing dataset
dataset = read.csv("50_Startups.csv")

#Encoding categorical data
dataset$State = factor(dataset$State,
                       levels = c('New York','California','Florida'),
                       labels = c(1,2,3))

#Splitting dataset into Trainingset and Test set
library(caTools)
set.seed(123)
split=sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)

#We do not need to manually do feature scaling since we have a function
#For simple linear regressions, no need to do feature scaling manually


#Fitting Multiple Linear Regression to Training Set 
# 1. Introduce the Multiple Linear Regressor.
# 2. Get a regressor to fit into training set
# 3. Apply predict functions to predict new observations on test set


#Expressing profit as a linear combination of all these independent variables
# data, we are want to train our model on training set and test performance on test set later
regressor = lm(formula = Profit ~ .,
               data = training_set)
#regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State)




#predicting the test set results
y_pred = predict(regressor, newdata = test_set)
#Compare real test_set profits against y_pred

#Building the optimal model using Backward Elimination. 
# Remove each independent variable p >0.05 one by one 

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
#Finding p_values
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend,
               data = dataset)
summary(regressor)












