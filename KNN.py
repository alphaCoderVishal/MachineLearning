import pandas as pd
import numpy as np
import matplotlib.pyplot as mtp
import seaborn as sns

dataset = pd.read_csv("Climate Data-kNN.csv")
# print(dataset.head())
x = dataset.iloc[:, 3:10]
y = dataset.iloc[:, -1]
# print(y)
# print(x)

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

# Fitting K-NN classifier to the training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(x_train, y_train)

# Predicting the test set result
y_pred = classifier.predict(x_test)
print("Training accuracy", classifier.score(x_train, y_train))
print("Testing accuracy", classifier.score(x_test, y_test))

# Creating the Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm)
mtp.show()
print("confusion Matrix:\n", cm)
