# importing libraries
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd

# importing datasets
data_csv = pd.read_csv(r'C:\Users\vishal567795\Desktop\Real estate.csv')

# Extracting Independent and dependent Variable
x = data_csv.iloc[:, :-1].values
y = data_csv.iloc[:, 7].values

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Fitting the MLR model to the training set:
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set result;
y_pred = regressor.predict(x_test)

print('Train Score: ', regressor.score(x_train, y_train))
print('Test Score: ', regressor.score(x_test, y_test))
