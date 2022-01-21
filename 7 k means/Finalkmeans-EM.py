"""
7.  Apply EM algorithm to cluster a set of data stored in a .CSV file. 
    Use the same data set for clustering using k-Means algorithm. 
    Compare the results of these two algorithms and comment on the quality of 
    clustering. You can add Java/Python ML library classes/API in the program.

"""
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
# Importing the dataset
data = pd.read_csv('xclara.csv')
print("Input Data and Shape")
print(data.shape)
data.head()
# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))
print('Graph for whole dataset')
plt.scatter(f1, f2, c='black', s=7)
plt.show()
##########################################
kmeans = KMeans(3, random_state=0)
labels = kmeans.fit(X).predict(X)
centroids = kmeans.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis');
print('Graph using Kmeans Algorithm')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
plt.show()
#gmm demo
gmm = GaussianMixture(n_components=3).fit(X)
labels = gmm.predict(X)
# for ploting

probs = gmm.predict_proba(X)
size = 10 * probs.max(1) ** 3
print('Graph using EM Algorithm')
#print(probs[:300].round(4))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=size, cmap='viridis');
plt.show()



