# models/scoring_logic.py

import os
import pandas as pd

PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
MERGED_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'merged')

# Load merged dataset
df = pd.read_csv(os.path.join(MERGED_PATH, 'retailer_feature_matrix.csv'))

# Calculate Channel Quality Score (custom logic — tune weights as needed)
df['channel_quality_score'] = (
    0.4 * df['performance_score'] +
    0.2 * (1 - df['fraud_score']) +  # Lower fraud score is better
    0.2 * df['sentiment_score'] +
    0.2 * (1 - df['complaint_intensity'])  # Lower complaints = better
)

# Save only scores (optional file)
df_scores = df[['retailer_id', 'channel_quality_score']]
df_scores.to_csv(os.path.join(PROCESSED_PATH, 'retailer_scores.csv'), index=False)
print("✅ Channel Quality Scores saved to retailer_scores.csv")

# Also update the main feature matrix with the score
df.to_csv(os.path.join(MERGED_PATH, 'retailer_feature_matrix.csv'), index=False)
print("✅ Final feature matrix updated with CQI scores.")
