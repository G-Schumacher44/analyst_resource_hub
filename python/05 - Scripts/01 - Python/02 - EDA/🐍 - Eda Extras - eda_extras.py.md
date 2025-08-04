# 🌟 Bonus / Optional EDA Visualizations (Tier 3)

___
# **🏃🏼‍♂️ Function calls**
```python
# 📈 Cluster Map
plot_cluster_map(df, numeric_cols)

# 📈 Andrews Curves (if target_col provided)
plot_andrews_curves(df, target_col)

# 🌈 Colored Pairplot
plot_colored_pairplot(df, target_col, numeric_cols)

# 🧬 Dendrogram
plot_dendrogram(df, numeric_cols)

# 🧪 Shapiro-Wilk Test
shapiro_wilk_test(df, numeric_cols)

# 🧪 Anderson-Darling Test
anderson_darling_test(df, numeric_cols)

# 🧪 Kolmogorov-Smirnov Test
kolmogorov_smirnov_test(df, numeric_cols)

# 📏 Skewness Correction Suggestions
suggest_skew_correction(df, numeric_cols)

# 📉 Hybrid Histograms + Q-Q Plots
for col in numeric_cols:
    plot_hybrid_hist_qq(df, col)
```
## **📈 Cluster Map — Feature Correlation Clustering**

```python
def plot_cluster_map(df, numeric_cols, title="Cluster Map of Feature Correlations"):
    """
    Plot a cluster map of feature correlations.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns to include.
    """
    corr = df[numeric_cols].corr()
    sns.clustermap(corr, cmap="coolwarm", annot=True, fmt=".2f", figsize=(12, 10))
    plt.suptitle(title, fontsize=16)
    plt.show()
```

___

## **📈 Andrews Curves — Pattern Visualization**

```python
def plot_andrews_curves(df, class_col):
    """
    Plot Andrews Curves to visualize multidimensional patterns by class.

    Args:
        df (DataFrame): Dataset.
        class_col (str): Target/class column name.
    """
    from pandas.plotting import andrews_curves

    plt.figure(figsize=(12, 8))
    andrews_curves(df, class_col=class_col)
    plt.title(f"Andrews Curves colored by {class_col}", fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___
## **🌈 Colored Pairplot — Colored by Target**
```python
def plot_colored_pairplot(df, class_col, numeric_cols):
    """
    Plot a pairplot colored by a target class.

    Args:
        df (DataFrame): Dataset.
        class_col (str): Target/class column name.
        numeric_cols (list): List of numeric columns to plot.
    """
    sns.pairplot(df, hue=class_col, vars=numeric_cols, diag_kind='kde', palette='husl')
    plt.tight_layout()
    plt.show()
```

___
## **🧬 Dendrogram — Hierarchical Clustering**
```python
def plot_dendrogram(df, numeric_cols, title="Dendrogram of Feature Clustering"):
    """
    Create a dendrogram for hierarchical clustering of features.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns.
    """
    from scipy.cluster.hierarchy import dendrogram, linkage

    corr = df[numeric_cols].corr()
    linked = linkage(corr, method='ward')

    plt.figure(figsize=(12, 8))
    dendrogram(linked, labels=numeric_cols, orientation='top', distance_sort='descending')
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.show()
```

___
# **🧪 Statistical Diagnostics**

## **🧹 Shapiro-Wilk Test for Normality**
```python
def shapiro_wilk_test(df, numeric_cols):
    """
    Perform Shapiro-Wilk normality test on numeric columns.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns.
    """
    from scipy.stats import shapiro

    for col in numeric_cols:
        stat, p = shapiro(df[col].dropna())
        print(f"🔎 Shapiro-Wilk Test for {col}: W={stat:.4f}, p={p:.4f}")
```

___

## **🧹 Anderson-Darling Test for Normality**
```python
def anderson_darling_test(df, numeric_cols):
    """
    Perform Anderson-Darling normality test on numeric columns.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns.
    """
    from scipy.stats import anderson

    for col in numeric_cols:
        result = anderson(df[col].dropna(), dist='norm')
        print(f"🔎 Anderson-Darling Test for {col}: A2={result.statistic:.4f}")
```

____
## **🧹 Kolmogorov-Smirnov Test (Against Normal)**
```python
def kolmogorov_smirnov_test(df, numeric_cols):
    """
    Perform Kolmogorov-Smirnov test for goodness-of-fit against a normal distribution.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns.
    """
    from scipy.stats import kstest

    for col in numeric_cols:
        stat, p = kstest(df[col].dropna(), 'norm', args=(df[col].mean(), df[col].std()))
        print(f"🔎 Kolmogorov-Smirnov Test for {col}: D={stat:.4f}, p={p:.4f}")
```

___

## **📏 Auto-Skewness Correction Suggester**
```python
def suggest_skew_correction(df, numeric_cols, threshold=1.0):
    """
    Suggest log/sqrt transformation if skewness exceeds threshold.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list): List of numeric columns.
        threshold (float): Skewness threshold to trigger suggestions.
    """
    from scipy.stats import skew

    for col in numeric_cols:
        skewness = skew(df[col].dropna())
        if abs(skewness) > threshold:
            suggestion = "log transform" if skewness > 0 else "sqrt transform"
            print(f"⚡ {col} has high skewness ({skewness:.2f}). Consider applying a {suggestion}.")
```

___

## **📉 Histogram Overlayed on Q-Q Plot (Hybrid Visual)**
```python
def plot_hybrid_hist_qq(df, col):
    """
    Overlay histogram and Q-Q plot for a feature.

    Args:
        df (DataFrame): Dataset.
        col (str): Feature column to analyze.
    """
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Histogram with KDE
    sns.histplot(df[col].dropna(), kde=True, ax=axs[0], color='steelblue')
    axs[0].set_title(f"Histogram of {col}", fontsize=14)
    axs[0].grid(True, linestyle='--', alpha=0.7)

    # Q-Q Plot
    stats.probplot(df[col].dropna(), dist="norm", plot=axs[1])
    axs[1].set_title(f"Q-Q Plot of {col}", fontsize=14)
    axs[1].grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()
```