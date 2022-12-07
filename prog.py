import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

import scipy.spatial
from collections import Counter

data = pd.read_csv(r"Climate Data-kNN.csv")
data = data.dropna()

X = data.iloc[:,1:-1]
Y = data.iloc[:,-1]

X = X.to_numpy()
Y = Y.to_numpy()

X = normalize(X, axis=0, norm='max')

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

class KNN:
    def __init__(self, k):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
    def distance(self, X1, X2):
        distance = scipy.spatial.distance.euclidean(X1, X2)
    
    def predict(self, X_test):
        final_output = []
        for i in range(len(X_test)):
            d = []
            votes = []
            for j in range(len(X_train)):
                dist = scipy.spatial.distance.euclidean(X_train[j] , X_test[i])
                d.append([dist, j])
            d.sort()
            d = d[0:self.k]
            for d, j in d:
                votes.append(y_train[j])
            ans = Counter(votes).most_common(1)[0][0]
            final_output.append(ans)
            
        return final_output
    
    def score(self, X_test, y_test):
        predictions = self.predict(X_test)
        return (predictions == y_test).sum() / len(y_test)

clf = KNN(30)
clf.fit(X_train, y_train)

sc = clf.score(X_test, y_test)

print(sc)