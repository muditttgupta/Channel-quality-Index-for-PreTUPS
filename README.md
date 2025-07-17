# Channel Quality Index (CQI) Scoring System

## 📌 Overview

This project is a complete blueprint for building an AI-driven **Channel Quality Index (CQI)** scoring system designed for telecom retailers. It simulates the process of identifying high-performing, dormant, risky, or emerging retailers using clustering techniques and composite scoring based on multiple key metrics. Originally built as a blueprint project for **PretUPS** (a product by **Comviva Technologies**, a Tech Mahindra Company), this public version uses **fully simulated dummy data** and contains **no company-sensitive information**.

---

## 🎯 Project Goals

- Simulate retailer behavioral datasets such as transactions, feedback, revenue, and fraud risk.
- Engineer meaningful features that can influence business performance and fraud likelihood.
- Score retailers using a weighted CQI system that balances business KPIs and fraud risk.
- Use clustering to segment retailers into actionable categories (Star, Risky, Emerging, Dormant).
- Generate business-ready reports and dashboards.
- Provide an end-to-end automated pipeline from data generation to dashboarding.

---

## 🧠 AI/ML Use Cases

- **Clustering**: Retailers are segmented using unsupervised ML (KMeans) based on CQI scores.
- **Anomaly Indicators**: Fraud scores based on complaint intensities and synthetic anomaly triggers.
- **Composite Scoring**: Weighted metric system combines multiple behavioral indicators into a unified CQI score.
- **Visualization & Dashboarding**: Jupyter notebooks and Streamlit used for model explainability and inspection.

---

## 📂 Project Structure

```bash
ChannelQualityIndex/
│
├── dashboard/
│   ├── dashboard.py
│   └── plots/
│       ├── __init__.py
│       ├── cluster_plots.py
│       ├── feedback_plots.py
│       └── fraud_plots.py
│
├── data/
│   ├── raw/              # Simulated raw datasets (generated)
│   ├── processed/        # Cleaned feature datasets
│   ├── merged/           # Final merged feature matrix
│   └── reports/          # Output reports
│
├── generate_data/
│   ├── generate_transactions.py
│   ├── generate_feedback.py
│   ├── generate_fraud_indicators.py
│   ├── generate_revenue.py
│   └── generate_retailers.py
│
├── merge/
│   └── merge_all_features.py
│
├── models/
│   ├── clustering_model.py
│   └── scoring_logic.py
│
├── notebooks/
│   ├── eda_final.ipynb
│   └── fraud_inspection.ipynb
│
├── pipeline/
│   └── run_pipeline.py
│
├── preprocess/
│   ├── preprocess_feedback.py
│   ├── preprocess_fraud_indicators.py
│   ├── preprocess_revenue.py
│   ├── preprocess_retailers.py
│   └── preprocess_transactions.py
│
├── reports/
│   ├── generate_summary.py
│   ├── generate_top_risk_report.py
│   └── utils_report.py
│
├── scoring/
│   ├── compute_final_scores.py
│   └── score_exporter.py
│
├── LICENSE
├── README.md
└── requirements.txt
```
## ⚙️ Workflow / Pipeline
1. Generate Raw Data → /generate_data/
2. Preprocess Raw Data → /preprocess/
3. Merge into Feature Matrix → /merge/
4. Score Retailers → /models/scoring_logic.py
5. Cluster Retailers → /models/clustering_model.py
6. Generate Reports → /reports/
7. Final CQI Score Export → /scoring/
8. Visualize in Streamlit Dashboard → /dashboard/

Run the full pipeline using:
python pipeline/run_pipeline.py

---

## 📊 CQI Scoring Logic

The CQI Score is a weighted score composed of:
	•	Transaction Volume
	•	Revenue
	•	Complaint Intensity (inverse)
	•	Fraud Risk Score (inverse)
	•	Customer Feedback Score

The scoring weights (customizable) are used to compute a normalized composite CQI score. Higher fraud or complaint rates reduce the CQI score.

---

## 📈 Clustering Logic

Retailers are clustered using KMeans (n_clusters = 4) into the following segments:
	•	Star Retailers: High CQI, low fraud
	•	Emerging Retailers: Medium CQI, potential to grow
	•	Dormant Retailers: Low activity, low fraud
	•	Risky Retailers: High fraud risk regardless of activity

Clustering is done based on the final weighted CQI score to keep it interpretable.

---

## 🧪 Notebooks
	•	eda_final.ipynb: Visual exploration of retailer metrics, scores, and clustering distribution.
	•	fraud_inspection.ipynb: Drill-down analysis of fraud scores and risky cluster behavior.

📸 Recommended Screenshots for GitHub
	•	Cluster distribution pie chart from eda_final.ipynb
	•	Fraud risk distribution plot
	•	Final Streamlit dashboard summary

 ---

 ## 📊 Streamlit Dashboard

 Run:
 streamlit run dashboard/dashboard.py

 The dashboard includes:
	•	Cluster-level analysis
	•	Individual retailer explorer
	•	Fraud heatmaps and feedback score plots
	•	Score distribution graphs

 ---

 ## 📝 License

This project was developed for PretUPS (a product of Comviva Technologies, a Tech Mahindra Company). It uses simulated data only and contains no confidential or sensitive company information. It is posted publicly on GitHub for educational and architectural reference purposes under the MIT License.

---

## 👨‍💻 Author

Mudit Gupta
AI/ML Intern, DYMRA TECH
LinkedIn: linkedin.com/in/muditgupta
GitHub: github.com/yourusername

