_Companion to: [[General EDA Guidebook]] and [[Eda Advanced Guidebook]]_
___
## 🎯 Purpose
This guide builds on the basics with advanced techniques to deepen your understanding of data through EDA. It focuses on practical applications and actionable insights to help you handle complex data scenarios effectively.

---

## 📈 1. Advanced Distribution Analysis

### Used for:
- Detecting subtle distribution features
- Identifying outliers and anomalies
- Understanding data shape beyond basics

### Practical Tips
- Use **QQ plots** to check how closely data follows a theoretical distribution.
- Apply **transformation tests** (e.g., Box-Cox) to improve normality.
- Consider **robust statistics** like median and MAD for skewed data.

---

## 📦 2. Outlier Detection Techniques

### Used for:
- Identifying unusual observations
- Improving model robustness

### Practical Tips
- Use **Mahalanobis distance** to find multivariate outliers in a simple way.
- Apply **Isolation Forest** for scalable anomaly detection in large datasets.
- Always review flagged points contextually before removal.

---

## 🔄 3. Feature Relationships and Interaction

### Used for:
- Uncovering complex dependencies
- Identifying non-linear relationships

### Practical Tips
- Explore **partial dependence plots** to understand feature effects on predictions.
- Use **interaction plots** to visualize combined effects of features.
- Employ **correlation ratios** for mixed data types.

---

## 🔍 4. Dimensionality Reduction

### Used for:
- Simplifying data visualization
- Reducing noise and redundancy

### Practical Tips
- Use **PCA** to capture main variance directions.
- Apply **t-SNE** or **UMAP** for visualizing clusters in high-dimensional data.
- Remember to scale data before applying these methods.

---

## 🛠 5. Handling Missing Data

### Used for:
- Understanding missingness patterns
- Choosing appropriate imputation strategies

### Practical Tips
- Visualize missing data with heatmaps or matrix plots.
- Use simple imputations (mean, median) for small gaps.
- For complex missingness, consider model-based imputation or flagging missingness as a feature.

---

## 📐 6. Advanced Visualization Techniques

### Used for:
- Revealing hidden patterns
- Communicating complex insights clearly

### Practical Tips
- Use **heatmaps** with clustering to spot groups.
- Apply **parallel coordinate plots** for multivariate data.
- Leverage **interactive plots** for deeper exploration.

---

## 🧭 Summary Reference Table

| Technique              | Purpose                         | When to Use                      | Key Action                         |
|------------------------|---------------------------------|----------------------------------|-----------------------------------|
| Advanced Distribution  | Detailed shape and outliers    | Subtle distribution features     | Use QQ plots, transformations     |
| Outlier Detection      | Identify unusual points        | Multivariate or large datasets   | Apply Mahalanobis, Isolation Forest|
| Feature Interaction    | Understand complex relations   | Non-linear or combined effects   | Use partial dependence, interaction plots|
| Dimensionality Reduction| Simplify and visualize data    | High-dimensional data            | Apply PCA, t-SNE, UMAP             |
| Missing Data Handling  | Manage incomplete data         | Various missingness patterns     | Visualize, impute, or flag missing|
| Advanced Visualization | Reveal and communicate patterns| Complex or multivariate data     | Use heatmaps, parallel coords, interactive plots|

---

Let me know when you’re ready for the next steps or additional resources!