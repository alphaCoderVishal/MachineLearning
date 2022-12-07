import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("bank.csv", header=[0])
# print(dataset)
# dataset.head()
# print(dataset.shape)
# dataset.dropna()
# print(dataset.columns(9))
# print(list(dataset.columns))
# dataset.columns[9]
dataset.drop(dataset.columns[[0, 3, 5, 8, 9, 10, 11, 12, 13, 14]], axis=1, inplace=True)
# print(list(dataset.columns))

# print(dataset)
print(dataset.head())
# creating one hot encoding
data = pd.get_dummies(dataset, columns =['job', 'marital', 'default', 'housing', 'loan', 'poutcome'])
# print(data.head())
# print(data.columns)
print(data.columns)

data.drop(data.columns[[12, 18, 25]], axis=1, inplace=True)
print(data.columns)
X = data.iloc[:, 1:]
print(X.head())
Y = data.iloc[:, 0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
classifier = LogisticRegression(solver='lbfgs', random_state=0)
classifier.fit(X_train, Y_train)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, max_iter=100, multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=0, solver='lbfgs', tol=0.0001, verbose=0, warm_start=False)
predicted_y = classifier.predict(X_test)
print(predicted_y)
for x in range(len(predicted_y)):
    if predicted_y[x] == 'yes':
        print(x, end="\t")

print('Accuracy: {:.2f}'.format(classifier.score(X_test, Y_test)))


