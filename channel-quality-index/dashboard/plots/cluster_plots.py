import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_cluster_distribution(df):
    """Bar plot of cluster label counts."""
    if 'cluster_label' not in df.columns:
        st.warning("Cluster label column not found.")
        return

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='cluster_label', palette='Set2')
    plt.title("Retailer Cluster Distribution")
    plt.xlabel("Cluster Label")
    plt.ylabel("Count")
    st.pyplot(plt.gcf())
    plt.clf()
