"""Clustering Analysis"""

import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def cluster_customers(df, features=['Age', 'Annual_Income_k', 'Spending_Score']):
    """Perform clustering"""
    print(f"\nClustering on: {features}")
    
    X = df[features].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Find optimal K
    silhouettes = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(X_scaled)
        silhouettes.append(silhouette_score(X_scaled, labels))
    
    optimal_k = silhouettes.index(max(silhouettes)) + 2
    print(f" Optimal K: {optimal_k}")
    
    # K-Means
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    sil_kmeans = silhouette_score(X_scaled, kmeans_labels)
    print(f"K-Means Silhouette: {sil_kmeans:.4f}")
    
    # DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=10)
    dbscan_labels = dbscan.fit_predict(X_scaled)
    n_dbscan = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
    print(f"DBSCAN Clusters: {n_dbscan}")
    
    return X_scaled, kmeans_labels, dbscan_labels