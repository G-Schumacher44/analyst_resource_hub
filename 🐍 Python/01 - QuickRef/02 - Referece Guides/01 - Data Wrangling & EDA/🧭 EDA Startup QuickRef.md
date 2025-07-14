 🎯 Purpose

This QuickRef provides a concise, repeatable checklist and syntax starter for exploratory data analysis. It includes structural diagnostics, missingness checks, distribution metrics, and common statistical diagnostics — all optimized for notebook use.

---

## 📦 1. Data Snapshot & Structure

```python
# Shape and preview
print(df.shape)
df.head()

# Info and column types
df.info()
df.dtypes

# Unique values per column
df.nunique()
```

✔️ Confirm row/column count matches expectations
✔️ Identify object-type columns needing conversion

---

## ❓ 2. Missingness Diagnostics

```python
# Count and percentage
missing = df.isnull().sum()
missing_pct = df.isnull().mean() * 100

# Visual (if needed)
import missingno as msno
msno.matrix(df)
```

✔️ Flag columns >30% null for review
✔️ Consider imputation or removal if MCAR (Missing Completely At Random)

---

## 📊 3. Descriptive Stats Summary

```python
# Core summary
summary = df.describe(include='all').T

# Shape + outlier preview
summary[['mean', 'std', 'min', 'max']]
```

✔️ Review for unit mismatches, implausible values, and flat distributions

---

## 📈 4. Distribution & Skew Checks

```python
from scipy.stats import skew, kurtosis

# Example: for all numeric columns
skews = df.select_dtypes('number').apply(skew)
kurtoses = df.select_dtypes('number').apply(kurtosis)
```

| Metric       | Interpretation              |
| ------------ | --------------------------- |
| Skew > 1     | Highly right-skewed         |
| Skew < -1    | Highly left-skewed          |
| Kurtosis > 3 | Heavy tails / outlier prone |

✔️ Suggests log or Yeo-Johnson transform candidates

---

## 📐 5. Correlation Matrix

```python
# Pearson (linear)
df.corr(numeric_only=True).round(2)

# Spearman (nonlinear/ordinal)
df.corr(method='spearman', numeric_only=True)
```

✔️ Identify highly correlated (>0.85) fields to review for redundancy

---

## 🧪 6. Outlier Detection (Stats-Based)

```python
from scipy.stats import zscore
z = df.select_dtypes('number').apply(zscore)
outliers = (z.abs() > 3).sum()
```

✔️ Flag for review, but don’t remove without domain justification

---

## ✅ Mini Summary Checklist

* [ ] `.info()` and `.dtypes` reviewed
* [ ] Missing data % calculated and visualized
* [ ] Descriptive stats exported
* [ ] Skew/kurtosis reviewed (high = transform candidate)
* [ ] Correlation matrix reviewed
* [ ] Outliers flagged via z-score or boxplot

---

## 💡 Tip

> “EDA isn’t about beautifying data — it’s about uncovering what you don’t know yet.”
