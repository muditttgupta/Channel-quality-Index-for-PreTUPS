# preprocess/feature_feedback.py

import os
import pandas as pd
from textblob import TextBlob

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_PATH, exist_ok=True)

feedback = pd.read_csv(os.path.join(RAW_PATH, 'feedback_logs.csv'))
complaints = pd.read_csv(os.path.join(RAW_PATH, 'complaints.csv'))
transactions = pd.read_csv(os.path.join(RAW_PATH, 'transactions.csv'))

# Sentiment
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

feedback['sentiment_score'] = feedback['feedback_text'].apply(get_sentiment)
sentiment = feedback.groupby('retailer_id')['sentiment_score'].mean().reset_index()

# Complaint intensity
complaint_counts = complaints.groupby('retailer_id').size().reset_index(name='complaint_count')
txn_counts = transactions.groupby('retailer_id').size().reset_index(name='txn_count')
merged = pd.merge(complaint_counts, txn_counts, on='retailer_id', how='right').fillna(0)
merged['complaint_intensity'] = merged['complaint_count'] / merged['txn_count']

# Merge and score
df = pd.merge(sentiment, merged[['retailer_id', 'complaint_intensity']], on='retailer_id', how='outer').fillna(0)
df['feedback_score'] = (0.6 * df['sentiment_score']) + (0.4 * (1 - df['complaint_intensity']))

# Save
df.to_csv(os.path.join(PROCESSED_PATH, 'retailer_feedback_nlp.csv'), index=False)
print("✅ retailer_feedback_nlp.csv created.")
