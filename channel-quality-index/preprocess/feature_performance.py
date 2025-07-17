# preprocess/feature_performance.py

import os
import pandas as pd

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_PATH, exist_ok=True)

transactions = pd.read_csv(os.path.join(RAW_PATH, 'transactions.csv'))
profiles = pd.read_csv(os.path.join(RAW_PATH, 'retailer_profiles.csv'))

transactions['timestamp'] = pd.to_datetime(transactions['timestamp'])
days_range = (transactions['timestamp'].max() - transactions['timestamp'].min()).days + 1

# Feature engineering
agg = transactions.groupby('retailer_id').agg({
    'amount': ['sum', 'mean'],
    'timestamp': 'nunique'
}).reset_index()
agg.columns = ['retailer_id', 'total_volume', 'avg_ticket_size', 'active_days']

agg['avg_txn_volume'] = agg['total_volume'] / days_range
agg['active_days_ratio'] = agg['active_days'] / days_range

# Add performance score
agg['performance_score'] = (
    0.5 * agg['avg_txn_volume'] +
    0.3 * agg['avg_ticket_size'] +
    0.2 * agg['active_days_ratio']
)

# Save
agg.to_csv(os.path.join(PROCESSED_PATH, 'retailer_performance.csv'), index=False)
print("retailer_performance.csv created.")
