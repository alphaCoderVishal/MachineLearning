import numpy as np
import random
import math
from matplotlib import pyplot as plt


class KMeans:
    def init(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.clusters = []
        for i in range(n_clusters):
            self.clusters.append(set())

    def fit(self, X_train):
        # initializing centroids and clusters
        self.centroids = random.sample(X_train, self.n_clusters)
        for i in range(self.n_clusters):
            self.clusters[i].add(tuple(self.centroids[i]))

        for point in X_train:
            closest_centroid_index = 0
            min_distance = math.inf
            for index in range(len(self.centroids)):
                distance = self.euclidean(point, self.centroids[index])
                if (distance < min_distance):
                    closest_centroid_index = index
                    min_distance = distance
            self.clusters[closest_centroid_index].add(tuple(point))
            self.update_centroid(closest_centroid_index)

    def euclidean(self, point, data):
        return np.sqrt(np.sum((np.array(point) - np.array(data)) ** 2))

    def update_centroid(self, closest_centroid_index):
        new_centroid = np.mean(list(self.clusters[closest_centroid_index]))
        self.centroids[closest_centroid_index] = new_centroid


# Create a dataset of 2D distributions

kmeans = KMeans(n_clusters=3)
X_train = [[1, 1], [1, 2], [1, 3], [2, 2], [7, 1], [7, 2], [7, 3], [8, 1], [8, 2], [8, 3]]
kmeans.fit(X_train)

X = []
Y = []

for cluster in kmeans.clusters:
    temp_x = []
    temp_y = []
    for elem in cluster:
        temp_x.append(elem[0])
        temp_y.append(elem[1])
    X.append(temp_x)
    Y.append(temp_y)

plt.scatter(X[0], Y[0], color='red')
plt.scatter(X[1], Y[1], color='blue')
plt.scatter(X[2], Y[2], color='green')
plt.show()

# View results