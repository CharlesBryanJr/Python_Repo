# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
# pylint: disable=E0401

print()

'''
Organize the notebook
to create a Linear Regression Model
to predict the price per square foot
for the following housing data set:
housing_data.csv

Your task is to:
A. Prepare the data for machine learning
    a. Remove the column ‘No’
       with transaction sequence numbers
       since they do not contribute to home prices
    
    b. Convert the column ‘condition’
       to appropriate numeric values
       since ML cannot work with text values,
       only numbers
    
B. Divide the data into training and testing data sets
    a. Display the first five lines of the training set
    b. Display the first five lines of the testing set
    
C. Create a regression model
   based on the training data
   to predict’ Y price per sqft’
   
D. Test the model with the testing data set 
   and compute the accuracy of the predictions
    a. Display the accuracy value
       for both the test
       and training data sets
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# A. Prepare the data for machine learning

# Loading the data
housing_data = pd.read_csv('housing_data.csv')

# look at some of the data
print(housing_data.head(5))
housing_data.info()

# Remove the column ‘No’ with transaction sequence numbers since they do not contribute to home prices
housing_data.drop('No', axis=1, inplace=True)

# Convert the column ‘condition’ to appropriate numeric values since ML cannot work with text values, only numbers
conditions = set([condition for condition in housing_data['condition']])
print(conditions)
housing_data.replace({'condition': {'Poor': 0, 'Average': 1, 'Good': 2, 'Excellent': 3}}, inplace=True)

# display revised data frame
housing_data.info()
print(housing_data.head(5))

# check for correlation
correlated_matrix = housing_data.corr(numeric_only=True)
print(max(correlated_matrix))
sns.heatmap(correlated_matrix, annot=True, cmap='viridis')
plt.show()

Y = housing_data['Y price per sqft']
X = housing_data.drop('Y price per sqft', axis=1)

# Divide the data into training and testing data sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=33)

# Display the first five lines of the training set
print(X_train.head(5))
print(Y_train.head(5))

# Display the first five lines of the testing set
print(X_test.head(5))
print(Y_test.head(5))


# create a linear regression model (using the constructor)
lin_reg_model = LinearRegression()

# Fit the model to our dataset
lin_reg_model.fit(X_train, Y_train)
print("Linear Regression Model created and fitted")

# Predict Y_train using the X_train
Y_train_prediction = lin_reg_model.predict(X_train)

# Calculate error between Y_train and model's prediction of Y_train
# R squared Error
training_error_score = metrics.r2_score(Y_train, Y_train_prediction)
print(f'Training Data R squared Error: {training_error_score}')

# Test the model using X_test to predict of Y_test
Y_test_prediction = lin_reg_model.predict(X_test)
testing_error_score = metrics.r2_score(Y_test, Y_test_prediction)
print(f'Test Data R squared Error: {testing_error_score}')

sns.regplot(x=Y_test, y=Y_test_prediction, scatter_kws={'color': 'green'}, line_kws={'color': 'blue'})
plt.show()
print()