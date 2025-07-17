# generate_data/generate_feedback_logs.py

import os
import pandas as pd
import random

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_PATH, exist_ok=True)

feedback_options = [
    "Excellent service", "Very helpful", "Average experience",
    "Retailer overcharged", "Fraudulent behavior", "Recharge not received",
    "Slow response", "Highly recommended", "Untrustworthy", "Rude behavior"
]

def generate_feedback_logs(num_entries=1000):
    data = []
    for i in range(num_entries):
        data.append({
            'retailer_id': f"R{random.randint(1, 100):03}",
            'feedback_text': random.choice(feedback_options),
            'rating': random.randint(1, 5)
        })

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_PATH, "feedback_logs.csv"), index=False)
    print(f"✅ {len(df)} feedback entries generated.")

if __name__ == "__main__":
    generate_feedback_logs()
