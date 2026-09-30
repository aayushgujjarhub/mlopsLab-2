from sklearn.cluster import KMeans

X = [[1, 2], [2, 3], [8, 9], [9, 10]]

model = KMeans(n_clusters=2, random_state=0)
model.fit(X)

print("Clusters:", model.labels_)