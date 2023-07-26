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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

print(" ")

# Loading the data
car_data = pd.read_csv('car_data.csv')

# look at some of the data
car_data.head()
car_data.info()

# encoding Columns - replace text with numbers
car_data.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
car_data.replace({'Seller_Type': {'Dealer': 0, 'Individual': 1}}, inplace=True)
car_data.replace({'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

# display revised data frame
car_data.head()

corrMatrix = car_data.corr(numeric_only=True)
sns.heatmap(corrMatrix, annot=True, cmap='viridis') 
plt.show()

X = car_data.drop(['Car_Name', 'Selling_Price'], axis=1)
X.head(7)

# Create a separate 1 column matrix for the prices
Y = car_data['Selling_Price']
Y.head(7)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

# create a linear regression model (using the constructor)
lin_reg_model = LinearRegression() 

# Fit the model to our dataset
lin_reg_model.fit(X_train, Y_train)

print("Linear Regression Model created and fitted")

training_data_prediction = lin_reg_model.predict(X_train)

# R squared Error 
train_error_score = metrics.r2_score(Y_train, training_data_prediction) 

print("R squared Error - for Training  Data: ", train_error_score) 


Y_pred = lin_reg_model.predict(X_test)

test_error_score = metrics.r2_score(Y_test, Y_pred)

print("R squared Error - Test: ", test_error_score)

sns.regplot(x=Y_test, y=Y_pred, scatter_kws={"color": "green"}, line_kws={"color": "blue"})
plt.show()

print()
