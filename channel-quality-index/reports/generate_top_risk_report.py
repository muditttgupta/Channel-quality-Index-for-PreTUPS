import pandas as pd
from utils_report import save_csv_report

def generate_top_risky_retailers(input_path, output_path, top_n=20):
    df = pd.read_csv(input_path)
    risky_df = df.sort_values(by='fraud_score', ascending=False).head(top_n)
    save_csv_report(risky_df, output_path)

if __name__ == "__main__":
    input_path = "../data/merged/retailer_feature_matrix.csv"
    output_path = "../data/reports/top_risk_report.csv"
    generate_top_risky_retailers(input_path, output_path)
