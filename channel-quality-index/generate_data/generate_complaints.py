# generate_data/generate_complaints.py

import os
import pandas as pd
import random
from datetime import datetime, timedelta

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_PATH, exist_ok=True)

complaint_types = ["Fraud", "Delay", "Incorrect Recharge", "Rude Behavior", "Service Denial"]

def generate_complaints(num_entries=1000):
    data = []
    today = datetime.now()

    for i in range(num_entries):
        data.append({
            'retailer_id': f"R{random.randint(1, 100):03}",
            'complaint_type': random.choice(complaint_types),
            'date': (today - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_PATH, "complaints.csv"), index=False)
    print(f"✅ {len(df)} complaints generated.")

if __name__ == "__main__":
    generate_complaints()
