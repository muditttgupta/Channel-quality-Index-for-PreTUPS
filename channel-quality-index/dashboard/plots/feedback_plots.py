import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_sentiment_distribution(df):
    """Shows distribution of sentiment scores."""
    if 'sentiment_score' not in df.columns:
        st.warning("Sentiment score column not found.")
        return

    plt.figure(figsize=(6, 4))
    sns.histplot(df['sentiment_score'], bins=20, kde=True, color='skyblue')
    plt.title("Sentiment Score Distribution")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Retailer Count")
    st.pyplot(plt.gcf())
    plt.clf()

def plot_complaint_intensity(df):
    """Bar chart of complaint intensity across clusters."""
    if 'complaint_intensity' not in df.columns or 'cluster_label' not in df.columns:
        st.warning("Required columns not found for complaint intensity plot.")
        return

    avg_complaints = df.groupby('cluster_label')['complaint_intensity'].mean().reset_index()

    plt.figure(figsize=(6, 4))
    sns.barplot(data=avg_complaints, x='cluster_label', y='complaint_intensity', palette='pastel')
    plt.title("Average Complaint Intensity per Cluster")
    plt.xlabel("Cluster Label")
    plt.ylabel("Avg Complaint Intensity")
    st.pyplot(plt.gcf())
    plt.clf()
