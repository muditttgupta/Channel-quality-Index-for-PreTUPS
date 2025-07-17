import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_fraud_vs_performance(df):
    """Scatter plot of Fraud Score vs Performance Score."""
    if 'fraud_score' not in df.columns or 'performance_score' not in df.columns:
        st.warning("Required columns not found for fraud-performance plot.")
        return

    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x='fraud_score', y='performance_score', hue='cluster_label', palette='tab10')
    plt.title("Fraud Score vs Performance Score")
    plt.xlabel("Fraud Score")
    plt.ylabel("Performance Score")
    st.pyplot(plt.gcf())
    plt.clf()
