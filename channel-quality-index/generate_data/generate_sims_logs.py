# generate_data/generate_sim_logs.py

import os
import pandas as pd
import random
from datetime import datetime, timedelta

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_PATH, exist_ok=True)

def generate_sim_logs(num_retailers=100):
    data = []
    today = datetime.now()

    for rid in range(1, num_retailers + 1):
        for _ in range(random.randint(5, 15)):
            log = {
                'retailer_id': f"R{rid:03}",
                'imei': random.randint(100000000000000, 999999999999999),
                'sim_serial': f"SIM{random.randint(10000, 99999)}",
                'date': (today - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
            }
            data.append(log)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_PATH, "sim_logs.csv"), index=False)
    print(f"✅ {len(df)} SIM logs generated.")

if __name__ == "__main__":
    generate_sim_logs()
