import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_scores(input_path, output_path):
    df = pd.read_csv(input_path)

    scaler = MinMaxScaler()
    df[['fraud_score', 'performance_score', 'feedback_score']] = scaler.fit_transform(
        df[['fraud_score', 'performance_score', 'feedback_score']]
    )

    df['fraud_quality'] = 1 - df['fraud_score']
    df['cqi_score'] = (
        0.3 * df['fraud_quality'] +
        0.4 * df['performance_score'] +
        0.3 * df['feedback_score']
    )

    df.to_csv(output_path, index=False)
    print(f"Final CQI scores written to {output_path}")

if __name__ == "__main__":
    input_path = "../data/merged/retailer_feature_matrix.csv"
    output_path = "../data/merged/retailer_feature_matrix.csv"  # overwrites with cqi_score
    compute_scores(input_path, output_path)
