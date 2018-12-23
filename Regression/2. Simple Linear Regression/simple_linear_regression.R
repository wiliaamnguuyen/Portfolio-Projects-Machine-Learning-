#Set the working directory
#Step 1: Data pre-processing 

#Simple Linear Regression 

#Importing the dataset
dataset = read.csv("Salary_Data.csv")

#Splitting the dataset into Training Set and Test Set 
#Install package ("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

#Simple Linear Regression package takes care of feature scaling. 
#No need to manually feature scale manually 
#Data pre-processing finished. 

#I am now fitting our simple linear regressions to our training sets
#"Salary ~ YearsExperience" is simply the SLR formula
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)


#Predicting test sets, see how SLR behaves 
y_pred = predict(regressor, newdata = test_set)

#Visualising the Training Set Results 
#install.packages('ggplot2') once it is installed, no need to do it again
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata=training_set)),
            colour = 'blue') + 
  ggtitle('Salary Vs Experience (Training Set)') +
  xlab('Years of Experience') + 
  ylab('Salary')

#plot predicted salaries of \
#training sets
#plots observational points vs regression line

#Now, I use SLR to predict new observations of the test set. 
#Visualising the Test Set Results 
#install.packages('ggplot2') once it is installed, no need to do it again
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata=training_set)), #No need to change, same SLRline
            colour = 'blue') + 
  ggtitle('Salary Vs Experience (Test Set)') +
  xlab('Years of Experience') + 
  ylab('Salary')

