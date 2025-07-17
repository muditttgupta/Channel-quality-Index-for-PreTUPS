# generate_data/generate_transactions.py

import os
import pandas as pd
import random
from datetime import datetime, timedelta

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_PATH, exist_ok=True)

def generate_dummy_transactions(num_retailers=100, days=20):
    data = []
    today = datetime.now()

    for rid in range(1, num_retailers + 1):
        for d in range(days):
            date = today - timedelta(days=d)
            for _ in range(random.randint(3, 7)):
                txn = {
                    'retailer_id': f"R{rid:03}",
                    'timestamp': date.strftime('%Y-%m-%d'),
                    'amount': round(random.uniform(10, 500), 2),
                    'msisdn': f"98{random.randint(10000000, 99999999)}"
                }
                data.append(txn)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_PATH, "transactions.csv"), index=False)
    print(f"✅ {len(df)} transactions generated.")

if __name__ == "__main__":
    generate_dummy_transactions()
