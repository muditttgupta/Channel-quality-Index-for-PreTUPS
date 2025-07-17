import pandas as pd

def export_cqi_scores(input_path, output_path):
    df = pd.read_csv(input_path)
    selected = df[['retailer_id', 'cqi_score']]
    selected.to_csv(output_path, index=False)
    print(f"Exported retailer CQI scores to {output_path}")

if __name__ == "__main__":
    input_path = "../data/merged/retailer_feature_matrix.csv"
    output_path = "../data/reports/retailer_cqi_scores.csv"
    export_cqi_scores(input_path, output_path)
