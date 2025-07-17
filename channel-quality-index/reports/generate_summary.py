import pandas as pd
from utils_report import save_csv_report

def generate_summary_report(input_path, output_path):
    df = pd.read_csv(input_path)

    summary = {
        "Total Retailers": len(df),
        "Average Fraud Score": round(df['fraud_score'].mean(), 3),
        "Average Performance Score": round(df['performance_score'].mean(), 3),
        "Average Feedback Score": round(df['feedback_score'].mean(), 3)
    }

    summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])
    save_csv_report(summary_df, output_path)

if __name__ == "__main__":
    input_path = "../data/merged/retailer_feature_matrix.csv"
    output_path = "../data/reports/summary_report.csv"
    generate_summary_report(input_path, output_path)
