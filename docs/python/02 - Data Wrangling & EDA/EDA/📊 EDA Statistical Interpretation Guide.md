___
🎯 Purpose

This guide explains how to interpret key statistical summaries and tests commonly used in exploratory data analysis. It supports analysts in understanding distributional patterns, variable relationships, and data quality before modeling.

---

## 🧮 1. Descriptive Statistics

| Metric             | Meaning                    | Use Case                     |
| ------------------ | -------------------------- | ---------------------------- |
| **Mean**           | Average value of a feature | Central tendency (symmetric) |
| **Median**         | Middle value               | Skewed distributions         |
| **Std / Variance** | Spread of values           | Dispersion detection         |
| **Min / Max**      | Range endpoints            | Outlier spotting             |
| **Skewness**       | Asymmetry in distribution  | Transformation decision      |
| **Kurtosis**       | Tail heaviness             | Outlier likelihood           |

### Code Example:

```python
df.describe().T
```

---

## 📉 2. Distribution Normality Tests

| Test             | Interpretation                       |
| ---------------- | ------------------------------------ |
| Shapiro-Wilk     | p < 0.05 → not normally distributed  |
| D’Agostino’s K²  | Combines skew/kurtosis for normality |
| Anderson-Darling | Strong tail sensitivity              |

### Code Example:

```python
from scipy.stats import shapiro, normaltest
```

✔️ Use to justify transformation, bootstrapping, or robust stats

---

## 🔍 3. Correlation and Association

### 🔹 Pearson Correlation

* Measures linear relationship (range: –1 to +1)
* Sensitive to outliers

### 🔹 Spearman Rank Correlation

* Nonlinear, monotonic trends
* Robust to outliers and skew

### 🔹 Cramer’s V (Categorical)

* Association strength between categoricals

### Code:

```python
from scipy.stats import pearsonr, spearmanr
```

---

## 🔗 4. Feature-to-Target Relationship Tests

| Scenario                   | Test                         | Purpose                       |
| -------------------------- | ---------------------------- | ----------------------------- |
| Numeric vs Numeric         | Pearson/Spearman correlation | Linear/monotonic relationship |
| Categorical vs Numeric     | ANOVA / Kruskal-Wallis       | Group mean differences        |
| Categorical vs Categorical | Chi-Squared / Cramer’s V     | Association strength          |

---

## 🧪 5. Outlier Detection (Statistical)

| Method               | Description                    |
| -------------------- | ------------------------------ |
| Z-Score              | Observations > 3 SD from mean  |
| IQR Method           | Outside 1.5×IQR from Q1/Q3     |
| Mahalanobis Distance | Multivariate outlier detection |

✔️ Flag but don’t remove outliers without cause/context

---

## 📋 Analyst Summary Table Elements

| Field               | Use                                 |
| ------------------- | ----------------------------------- |
| Mean / Median       | Central location                    |
| Std / IQR           | Dispersion/spread                   |
| Skewness / Kurtosis | Transformation, normality           |
| Missing %           | Imputation plan                     |
| # Unique Values     | Cardinality (for encoding/grouping) |

---

## 💡 Final Tip

> “Stats don’t tell you the answer—but they tell you where to look. Use summary patterns to guide deeper investigation.”

Use with: General & Advanced EDA Guidebook
