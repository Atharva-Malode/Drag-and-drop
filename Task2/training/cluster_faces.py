from sklearn.cluster import KMeans
def cluster_faces(features, n_clusters=4):
    """
    Clusters face features using KMeans.
    :param features: Array of feature vectors.
    :param n_clusters: Number of clusters to create.
    :return: List of cluster labels and the KMeans model.
    """
    print(f"Clustering features into {n_clusters} clusters using KMeans.")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(features)
    print("Clustering completed.")
    return labels, kmeans