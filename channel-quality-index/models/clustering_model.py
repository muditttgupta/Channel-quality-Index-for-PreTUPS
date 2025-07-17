# models/clustering_model.py

import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Define paths
MERGED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'merged')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load merged feature matrix
df = pd.read_csv(os.path.join(MERGED_PATH, 'retailer_feature_matrix.csv'))

# Keep retailer_id separately
retailer_ids = df['retailer_id']

# ✅ Cluster only on cqi_score
X = df[['cqi_score']].fillna(0)

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans clustering (4 groups)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
df['cluster_id'] = clusters

# ✅ Sort cluster centers by average CQI score to assign proper labels
cluster_perf = df.groupby('cluster_id')['cqi_score'].mean().sort_values(ascending=False)
sorted_clusters = cluster_perf.index.tolist()
label_order = ['Star', 'Newcomer', 'Dormant', 'Risky']
label_map = {cid: label for cid, label in zip(sorted_clusters, label_order)}
df['cluster_label'] = df['cluster_id'].map(label_map)

# Save clustered data
df.to_csv(os.path.join(PROCESSED_PATH, 'retailer_clusters.csv'), index=False)
print("✅ Clustered data saved as retailer_clusters.csv")

# Save updated feature matrix with cluster labels
df.to_csv(os.path.join(MERGED_PATH, 'retailer_feature_matrix.csv'), index=False)
print("✅ Final feature matrix updated with cluster labels.")
