

import matplotlib.pyplot as plt
import seaborn as sns

def plot_violinplots(df, numeric_cols, target_col):
    for num_col in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.violinplot(x=target_col, y=num_col, data=df, palette="Set3")
        plt.title(f"Violin plot of {num_col} by {target_col}", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

def plot_swarmplots(df, numeric_cols, target_col):
    for num_col in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.swarmplot(x=target_col, y=num_col, data=df, size=3)
        plt.title(f"Swarm plot of {num_col} by {target_col}", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

def plot_pairwise_kde(df, numeric_cols):
    sns.pairplot(df[numeric_cols], kind='kde')
    plt.tight_layout()
    plt.show()