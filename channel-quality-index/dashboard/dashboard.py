# dashboard/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
features = pd.read_csv("../data/merged/retailer_feature_matrix.csv")

st.set_page_config(layout="wide")
st.title(" Channel Quality Index Dashboard")

# === Metrics Summary ===
st.subheader(" Summary Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Retailers", features.shape[0])
col2.metric("Clusters", features['cluster_label'].nunique())
col3.metric("Average CQI Score", round(features['channel_quality_score'].mean(), 2))

# === Cluster Label Breakdown ===
st.markdown("---")
st.subheader("Cluster Label Distribution")
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.countplot(data=features, x='cluster_label', order=features['cluster_label'].value_counts().index, palette="Set2", ax=ax1)
plt.xticks(rotation=30)
st.pyplot(fig1)

# === Top Performers ===
st.markdown("---")
st.subheader("Top 5 Retailers by CQI Score")
top_cqi = features.sort_values(by='cqi_score', ascending=False).head(5)
st.dataframe(top_cqi[['retailer_id', 'cqi_score', 'cluster_label']])

# === Fraud Risk ===
st.markdown("---")
st.subheader("High Risk Retailers (Fraud Score)")
top_fraud = features.sort_values(by='fraud_score', ascending=False).head(5)
fraud_cols = ['retailer_id', 'fraud_score', 'sim_change_rate', 'balance_forward_usage', 'same_msisdn_ratio']
available_fraud_cols = [col for col in fraud_cols if col in top_fraud.columns]
st.dataframe(top_fraud[available_fraud_cols])

# === Cluster Exploration ===
st.markdown("---")
st.subheader("Explore a Cluster")
clusters = features['cluster_label'].unique()
selected_cluster = st.selectbox("Select Cluster", clusters)
filtered = features[features['cluster_label'] == selected_cluster]

col4, col5, col6 = st.columns(3)
col4.metric("Avg CQI Score", round(filtered['channel_quality_score'].mean(), 2))
col5.metric("Avg Ticket Size", round(filtered['avg_ticket_size'].mean(), 2) if 'avg_ticket_size' in filtered else 0)
col6.metric("Avg Fraud Score", round(filtered['fraud_score'].mean(), 2))

# === CQI Score Distribution ===
st.markdown("---")
st.subheader("Channel Quality Index Distribution")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.histplot(features['channel_quality_score'], kde=True, color='purple', bins=20, ax=ax2)
st.pyplot(fig2)

# === Customer Sentiment ===
if 'sentiment_score' in features.columns:
    st.markdown("---")
    st.subheader("Customer Feedback Sentiment")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sentiment_counts = features['sentiment_score'].apply(lambda x: 'Positive' if x >= 0 else 'Negative').value_counts()
    ax3.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'salmon'])
    ax3.axis('equal')
    st.pyplot(fig3)

# === Complaint Intensity ===
if 'complaint_intensity' in features.columns:
    st.markdown("---")
    st.subheader("Complaint Intensity by Cluster")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=features, x='cluster_label', y='complaint_intensity', estimator='mean', palette='coolwarm', ax=ax4)
    plt.xticks(rotation=30)
    st.pyplot(fig4)

# === Final CQI Score Table ===
st.markdown("---")
st.subheader("Final CQI Scores by Retailer")
st.dataframe(features[['retailer_id', 'channel_quality_score']].sort_values(by='channel_quality_score', ascending=False))

# === Optional: Data Table ===
st.markdown("---")
if st.checkbox("Full retailer data Table"):
    st.dataframe(features.head(100))
