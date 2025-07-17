# preprocess/feature_fraud.py

import os
import pandas as pd

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load SIM logs and complaints
df_sim = pd.read_csv(os.path.join(RAW_PATH, 'sim_logs.csv'))
df_complaints = pd.read_csv(os.path.join(RAW_PATH, 'complaints.csv'))

# Step 1: Detect SIM changes
df_sim = df_sim.sort_values(by=['retailer_id', 'date'])

def count_sim_changes(group):
    return (group['sim_serial'] != group['sim_serial'].shift()).sum() - 1

sim_change_counts = df_sim.groupby('retailer_id').apply(count_sim_changes).reset_index()
sim_change_counts.columns = ['retailer_id', 'sim_change_count']

# Step 2: Complaint count per retailer
complaint_counts = df_complaints.groupby('retailer_id').size().reset_index(name='complaint_count')

# Step 3: Combine fraud features
df_fraud = sim_change_counts.merge(complaint_counts, on='retailer_id', how='outer').fillna(0)

# Step 4: Normalize and create a fraud score
df_fraud['fraud_score'] = (
    0.6 * (df_fraud['sim_change_count'] / (df_fraud['sim_change_count'].max() or 1)) +
    0.4 * (df_fraud['complaint_count'] / (df_fraud['complaint_count'].max() or 1))
)

# Save to processed
df_fraud.to_csv(os.path.join(PROCESSED_PATH, 'retailer_fraud_behavior.csv'), index=False)
print("retailer_fraud_behavior.csv created.")
