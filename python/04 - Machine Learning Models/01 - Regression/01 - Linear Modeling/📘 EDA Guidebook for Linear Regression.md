___
## 🎯 Purpose

This guide outlines structured exploratory data analysis (EDA) steps to prepare a dataset for linear regression. It focuses on verifying assumptions, inspecting variable relationships, detecting skewness and outliers, and diagnosing multicollinearity prior to model fitting.

---

## 🧠 1. Confirm Problem Structure

* [ ] ✅ Target variable is **continuous**
* [ ] ✅ Input features are mostly numeric (or encoded)
* [ ] ✅ No excessive missing values in target
* [ ] ✅ Modeling goal: **prediction**, **inference**, or **interpretation** clarified

---

## 📊 2. Target Variable Assessment

### 🔹 Distribution Check

```python
sns.histplot(y, kde=True)
```

* ⚠️ Strong skew? Consider log or Box-Cox transformation
* 🔍 Check for outliers or multi-modal shape

### 🔹 Normality Tests (optional)

```python
from scipy.stats import shapiro, normaltest
```

* Normality helps inferences (but not required for prediction)

---

## 📈 3. Feature-Target Relationship Checks

### 🔹 Correlation Matrix (Numeric)

```python
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
```

* Identify predictors with strong linear associations to `y`

### 🔹 Scatterplots

```python
sns.scatterplot(x=X['feature'], y=y)
```

* Look for linear trend, outliers, variance changes

### 🔹 Linearity of Relationship

* Plot residuals (even pre-model): LOESS trend helps detect curvature

---

## 📦 4. Skewness & Transformation Candidates

### 🔹 Assess Skew

```python
from scipy.stats import skew
skew(X['feature'])
```

* Skew > |1.0| = consider transforming (log, sqrt, etc.)

### 🔹 Visualize Distribution

```python
sns.histplot(X['feature'], kde=True)
```

* Use log scale or apply transformation for right-skewed features

---

## 🧹 5. Outlier Detection

### 🔹 Boxplots

```python
sns.boxplot(data=X, orient='h')
```

* Visually flag outliers per feature

### 🔹 Z-Scores (Numerical Outliers)

```python
from scipy.stats import zscore
z = zscore(X.select_dtypes(include='number'))
```

* Z > |3| = potential outlier

---

## 🔁 6. Multicollinearity Diagnostics

### 🔹 Correlation Matrix

* Look for feature pairs > 0.85

### 🔹 Variance Inflation Factor (VIF)

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
```

* VIF > 5–10 = multicollinearity issue

### 🔹 Dimensionality Reduction (optional)

* PCA or feature pruning for highly redundant predictors

---

## 🔎 7. Optional Binning / Feature Engineering

* Group continuous variables into bins if relationship is non-linear but monotonic
* Create interaction terms if suspected synergy between features
* Apply log transformations where variance or skew is unstable

---

## 📋 Analyst EDA Checklist for Linear Regression

* [ ] Target variable checked for skew and outliers
* [ ] Features screened for missingness and skew
* [ ] Relationships to `y` explored with scatterplots
* [ ] High-cardinality categoricals reviewed or encoded
* [ ] Correlation matrix inspected for redundancy
* [ ] VIF calculated for multicollinearity
* [ ] Outliers noted and handling strategy drafted

---

## 💡 Final Tip

> “Linear regression is sensitive to structure, not just data. Let EDA guide what transformations and diagnostics come next.”

Use this before: Fitting OLS / Ridge / Lasso models, or validating linearity assumptions visually.
