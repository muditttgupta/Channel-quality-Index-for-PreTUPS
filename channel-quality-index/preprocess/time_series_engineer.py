# preprocess/time_series_engineer.py

import os
import pandas as pd

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_PATH, exist_ok=True)

transactions = pd.read_csv(os.path.join(RAW_PATH, 'transactions.csv'))
complaints = pd.read_csv(os.path.join(RAW_PATH, 'complaints.csv'))

transactions['timestamp'] = pd.to_datetime(transactions['timestamp'])

# 7-day moving average and variance
volume = transactions.groupby(['timestamp', 'retailer_id'])['amount'].sum().reset_index()
pivot = volume.pivot(index='timestamp', columns='retailer_id', values='amount').fillna(0)
rolling = pivot.rolling(window=7).mean()

# Simple risk metric: last week's drop vs average
risk = ((rolling.iloc[-8:-1] < rolling.mean()).sum()) / 7
risk_df = risk.reset_index()
risk_df.columns = ['retailer_id', 'risk_prediction_score']

# Save
risk_df.to_csv(os.path.join(PROCESSED_PATH, 'retailer_time_series.csv'), index=False)
print("✅ retailer_time_series.csv created.")

