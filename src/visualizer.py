"""Visualization"""

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_clusters(X_scaled, kmeans_labels, dbscan_labels):
    """Create cluster plots"""
    print("\nCreating visualizations...")
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels, cmap='tab10', s=20, alpha=0.6)
    axes[0].set_title('K-Means Clustering', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('PC1')
    axes[0].set_ylabel('PC2')
    
    axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=dbscan_labels, cmap='tab10', s=20, alpha=0.6)
    axes[1].set_title('DBSCAN Clustering', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('PC1')
    axes[1].set_ylabel('PC2')
    
    plt.tight_layout()
    plt.savefig('Final_Result_Images/clusters.png', dpi=200, bbox_inches='tight')
    print(" Saved: Final_Result_Images/clusters.png")
    plt.close()