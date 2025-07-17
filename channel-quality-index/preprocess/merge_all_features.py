# preprocess/merge_all_features.py

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
MERGED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'merged')
os.makedirs(MERGED_PATH, exist_ok=True)

# Load all processed features
fraud = pd.read_csv(os.path.join(PROCESSED_PATH, 'retailer_fraud_behavior.csv'))
perf = pd.read_csv(os.path.join(PROCESSED_PATH, 'retailer_performance.csv'))
time_series = pd.read_csv(os.path.join(PROCESSED_PATH, 'retailer_time_series.csv'))
feedback = pd.read_csv(os.path.join(PROCESSED_PATH, 'retailer_feedback_nlp.csv'))

# Merge all
df = fraud.merge(perf, on='retailer_id', how='outer')
df = df.merge(time_series, on='retailer_id', how='outer')
df = df.merge(feedback, on='retailer_id', how='outer')
df = df.fillna(0)

# === Weighted CQI: Reward performance, penalize fraud ===
# You can adjust the weight below (e.g., 0.5 means fraud has 50% weight vs. performance)
fraud_penalty_weight = 0.7
raw_cqi = df['performance_score'] - fraud_penalty_weight * df['fraud_score']
df['cqi_score'] = MinMaxScaler().fit_transform(raw_cqi.values.reshape(-1, 1))

# Save
df.to_csv(os.path.join(MERGED_PATH, 'retailer_feature_matrix.csv'), index=False)
print("Updated merged feature matrix with penalized CQI")
