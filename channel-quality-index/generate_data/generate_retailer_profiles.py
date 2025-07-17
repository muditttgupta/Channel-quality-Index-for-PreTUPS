# generate_data/generate_retailer_profiles.py

import os
import pandas as pd
import random

RAW_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_PATH, exist_ok=True)

zones = ['North', 'South', 'East', 'West', 'Central']

def generate_retailer_profiles(num_retailers=100):
    data = []
    for rid in range(1, num_retailers + 1):
        profile = {
            'retailer_id': f"R{rid:03}",
            'zone': random.choice(zones),
            'onboard_date': f"2023-{random.randint(1, 12):02}-01",
            'commission_rate': round(random.uniform(1.5, 5.0), 2)
        }
        data.append(profile)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_PATH, "retailer_profiles.csv"), index=False)
    print(f"✅ {len(df)} retailer profiles generated.")

if __name__ == "__main__":
    generate_retailer_profiles()
