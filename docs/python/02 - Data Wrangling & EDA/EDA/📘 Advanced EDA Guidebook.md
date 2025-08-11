_Companion to: [[General EDA Guidebook]]_
___
## 🎯 Purpose
This guidebook dives deeper into **Exploratory Data Analysis (EDA)** with a focus on practical, advanced techniques. It covers targeted profiling, interaction detection, outlier identification, dimensionality reduction, data quality checks, and missing data handling—all aimed at improving your data understanding and modeling readiness.

---

## 🧬 1. Target-Aware Profiling

### 🔍 Comparing Feature Distributions by Outcome
```python
# Summary stats for numeric features grouped by target
for col in numeric_features:
    print(f"Stats for {col} by target:")
    display(df.groupby('target')[col].describe())
```
- Quickly spot differences in feature distributions between classes
- Useful for identifying features that separate target groups

### 🔄 Testing Distribution Differences
```python
from scipy.stats import ks_2samp

# KS test to check if feature distribution differs by target
stat, p_value = ks_2samp(df[df['target']==0]['feature'], df[df['target']==1]['feature'])
print(f"KS statistic: {stat}, p-value: {p_value}")
```
- Practical way to confirm if distributions differ significantly
- Helps detect feature drift or shifts related to the target

---

## 📊 2. Interaction & Conditional Visualizations

### When to Use:
- To explore how features work together or affect the target jointly
- To uncover patterns not visible in univariate analysis

### Examples
```python
# Interaction between categories and numeric target
sns.pointplot(x='cat1', y='num', hue='cat2', data=df)

# Boxplots by subgroup and target to see conditional distributions
sns.catplot(x='cat1', y='num', hue='cat2', kind='box', col='target', data=df)
```
- Use these plots to guide feature engineering and interaction terms

---

## 🧪 3. Outlier Detection

### Mahalanobis Distance (Multivariate Outliers)
```python
from scipy.spatial.distance import mahalanobis
import numpy as np

cov_matrix = np.cov(df[numeric_features].values, rowvar=False)
inv_cov_matrix = np.linalg.inv(cov_matrix)
mean_distr = df[numeric_features].mean().values

df['mahalanobis'] = df[numeric_features].apply(lambda x: mahalanobis(x, mean_distr, inv_cov_matrix), axis=1)
```
- Identifies points that stand out when considering all features together
- Useful for spotting unusual observations that might affect modeling

### Isolation Forest (Anomaly Detection)
```python
from sklearn.ensemble import IsolationForest

iso = IsolationForest(contamination=0.02, random_state=42)
df['outlier'] = iso.fit_predict(df[numeric_features])
```
- Detects anomalies in complex, high-dimensional data
- Good for finding rare or unexpected events in your dataset

---

## 🧠 4. Dimensionality Reduction

### Principal Component Analysis (PCA)
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
components = pca.fit_transform(df[numeric_features])
df['PC1'], df['PC2'] = components[:,0], components[:,1]
```
- Simplifies data by capturing the main sources of variation
- Helps with visualization and reducing noise

### t-SNE (Non-linear Embedding)
```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
tsne_results = tsne.fit_transform(df[numeric_features])
df['TSNE1'], df['TSNE2'] = tsne_results[:,0], tsne_results[:,1]
```
- Useful for visualizing complex clusters and patterns not captured by PCA

### Visualization
```python
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(df['PC1'], df['PC2'], c=df['target'])
plt.title('PCA projection')

plt.subplot(1,2,2)
plt.scatter(df['TSNE1'], df['TSNE2'], c=df['target'])
plt.title('t-SNE projection')
plt.show()
```

---

## 📉 5. Checking Feature Redundancy

### Condition Number
```python
from numpy.linalg import cond

condition_number = cond(df[numeric_features].values)
print(f"Condition number: {condition_number}")
```
- High values indicate multicollinearity or redundant features
- Helps identify features that may cause unstable models

---

## 📚 6. Data Quality Checks

### Unique Value Ratios
```python
unique_ratios = df.nunique() / len(df)
print(unique_ratios)
```
- Detects constant or near-constant columns that add little value

### Leakage Checks
- Look for features that might leak future information or duplicates
- Important to prevent overly optimistic model performance

---

## 🔁 7. Handling Missing Data

### Visualizing Missingness
```python
import missingno as msno

msno.heatmap(df)
```
- Understand patterns in missing data to decide on imputation

### Simple Imputation
```python
df.fillna(df.median(), inplace=True)
```
- Start with straightforward methods unless data complexity requires more

---

## 🧭 8. Automated Profile Reports

### pandas-profiling
```python
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Advanced EDA Report")
profile.to_notebook_iframe()
```

### sweetviz
```python
import sweetviz

report = sweetviz.analyze(df)
report.show_html()
```

---

## ✅ Advanced EDA Checklist

| Task                      | Tool / Method             | When to Use                         |
|---------------------------|---------------------------|-----------------------------------|
| Feature distribution by target | Group stats, KS test      | To compare feature behavior across classes |
| Feature interactions       | Pointplot, boxplot        | To explore combined effects or segmentations |
| Outlier detection          | Mahalanobis, IsolationForest | To find unusual or rare data points |
| Dimensionality reduction   | PCA, t-SNE                | For visualization and noise reduction |
| Redundancy detection       | Condition number          | To identify multicollinearity issues |
| Data quality checks        | Unique ratios, leakage review | To ensure reliable modeling inputs |
| Missing data analysis      | missingno, simple imputation | To handle incomplete data effectively |

---

Let me know if you'd like these sections converted into ready-to-use scripts, visualizations, or notebook formats!
