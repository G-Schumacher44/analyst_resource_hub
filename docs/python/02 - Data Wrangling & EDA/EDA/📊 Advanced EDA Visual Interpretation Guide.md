___
🎯 Purpose

This guide expands upon standard exploratory data visualizations by focusing on advanced, high-dimensional, and context-specific visual tools. These visuals are designed to support deeper discovery, pattern recognition, and structure validation across complex datasets.

---

## 📈 1. Advanced Distribution Analysis

### Used for:

* Identifying subtle non-normality
* Flagging asymmetric or long-tail features
* Pre-transform checks

### Recommended Visuals:

* QQ Plot (for normality)

```python
from scipy import stats
stats.probplot(df['feature'], dist="norm", plot=plt)
```

* Box-Cox Distribution Comparison
* Histogram with log scale overlay

✔️ Use when assessing need for transformation or normalization

---

## 📦 2. Multivariate Outlier Detection

### Used for:

* Catching high-dimensional anomalies
* Finding data points that don’t fit the core structure

### Recommended Visuals:

* Mahalanobis Distance vs Observation Plot
* Isolation Forest Score Distribution
* t-SNE or UMAP embedding with outlier overlay

✔️ Color outliers in reduced-dim scatter for visual impact

---

## 🔄 3. Feature Interaction Visualization

### Used for:

* Capturing non-linear, conditional, or synergistic relationships
* Informing new feature creation

### Recommended Visuals:

* Interaction Plot by Group
* LOESS curve overlays on scatterplots
* PairGrid with color by target or cluster

✔️ Use to justify interaction terms in models

---

## 🧬 4. Conditional Distribution by Target or Cluster

### Used for:

* Exploring feature shifts between subgroups
* Validating groupwise trends

### Recommended Visuals:

* Boxen plots split by target or label
* Density plots with hue = class or group
* Violin plots for long-tail variables

✔️ Helps flag high-leverage group-specific features

---

## 🔍 5. Dimensionality Reduction Projections

### Used for:

* Understanding structure in complex data
* Pre-clustering and anomaly discovery

### Recommended Visuals:

* PCA scatter with color by class or metric
* UMAP/t-SNE embedding (cluster or group-labeled)
* Explained variance bar plot

✔️ Use consistent scaling and coloring across runs

---

## 🧮 6. Redundancy and Multicollinearity Checks

### Used for:

* Identifying feature duplication or instability
* Supporting feature pruning decisions

### Recommended Visuals:

* Correlation Matrix Heatmap
* VIF Score Bar Chart
* Condition Index Plot

✔️ Filter collinear features visually before modeling

---

## 🧰 7. Missingness Pattern Maps

### Used for:

* Evaluating missing data structure
* Detecting systematic vs random gaps

### Recommended Visuals:

* Missingno Heatmap / Matrix
* Custom bar chart of % missing per feature
* Time series missing block map (if applicable)

✔️ Use to guide imputation method selection

---

## 📋 Analyst Visual EDA Checklist

* [ ] Target-level conditional p
