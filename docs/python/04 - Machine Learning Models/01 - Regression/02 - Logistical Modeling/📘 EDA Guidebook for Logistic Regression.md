___

## 🎯 Purpose
This guide outlines the essential steps for **exploratory data analysis (EDA)** before fitting a **logistic regression** model. Logistic regression models the relationship between one or more independent variables and a **binary or categorical outcome**.

---

## 🧭 1. Understand the Outcome Variable

### 🧠 Goal
Confirm that your **dependent variable (DV)** is binary (0/1 or two distinct classes).

### ✅ EDA Tasks
- Use `.value_counts()` to confirm balance
- Create bar plot of class frequencies

### 🐍 Example
```python
df['outcome'].value_counts()
sns.countplot(x='outcome', data=df)
```

### 📌 Notes
- Severe imbalance (e.g., 95%/5%) may require oversampling or synthetic data techniques like SMOTE.

---

## 🔍 2. Explore Categorical Predictors

### 🧠 Goal
Examine how the distribution of categories relates to the outcome.

### ✅ EDA Tasks
- Create **stacked bar plots** of outcome by category
- Use **chi-squared tests** to check for association

### 🐍 Example
```python
pd.crosstab(df['category'], df['outcome'], normalize='index').plot(kind='bar', stacked=True)
```

---

## 📈 3. Explore Numerical Predictors

### 🧠 Goal
Assess whether numerical predictors differ between outcome classes.

### ✅ EDA Tasks
- Use **histograms or KDE plots** split by outcome
- Compare distributions with **boxplots**
- Use **logistic regression scatterplots** for intuition

### 🐍 Example
```python
sns.boxplot(x='outcome', y='age', data=df)
sns.histplot(data=df, x='income', hue='outcome', kde=True)
```

---

## 🔄 4. Linearity of the Logit (For Continuous Variables)

### 🧠 Goal
Check that continuous predictors are linearly related to the **log odds** of the outcome.

### ✅ EDA Tasks
- Create **binned line plots** of predictor vs log-odds
- Use **Box-Tidwell test** (optional)

### 🐍 Example
```python
df['age_bins'] = pd.qcut(df['age'], q=10)
df.groupby('age_bins')['outcome'].mean().plot()
```

### 📌 Notes
If the relationship is non-linear, consider:
- Log or square root transforms
- Splines or polynomial terms

---

## 🧪 5. Multicollinearity Check

### 🧠 Goal
Avoid using highly correlated predictors that distort coefficient interpretation.

### ✅ EDA Tasks
- Create a **correlation heatmap**
- Calculate **Variance Inflation Factor (VIF)**

### 🐍 Example
```python
sns.heatmap(df.corr(), annot=True)
```

---
## 6.Optional: Early Visualization of Predicted Probabilities (Advanced)

If preliminary model predictions are available (e.g., from a baseline model or pretrained scores), you can inspect the distribution of predicted probabilities to assess class separation early.

**Note:**  
Predicted probabilities are generated using the `.predict_proba()` method after fitting a logistic model.  

Typically:

```python
proba = model.predict_proba(X)[:, 1]  # Probability of class 1
```
You cannot visualize predicted probabilities unless you already have model predictions available.

```python
import seaborn as sns
import matplotlib.pyplot as plt

#Assume `proba` contains pre-fitted probabilities
sns.histplot(proba, bins=30, kde=True, hue=y_true, stat='density', common_norm=False)
plt.xlabel('Predicted Probability')
plt.title('Distribution of Predicted Probabilities (Optional Early EDA)')
plt.show()
```

### 📋 Note: Predicted Probabilities in EDA (Advanced)
**Important:**  

Predicted probabilities (`proba`) are only available after fitting a model and calling `.predict_proba(X)`.  

They are not typically part of early EDA unless you are given pre-computed model scores or have a baseline model already trained.

 To visualize model confidence early:
```python

proba = model.predict_proba(X)[:, 1]  # Probability for class 1

sns.histplot(proba, bins=30, kde=True, hue=y_true, stat='density', common_norm=False)

plt.axvline(x=0.5, color='red', linestyle='--', label='Default Threshold 0.5')

plt.title('Distribution of Predicted Probabilities (Optional Early EDA)')

plt.legend()

plt.show()
```

## 📊 7. Feature Binning or Transformation (Optional)

### 🧠 Goal
Enhance model performance, improve interpretability, and correct skewness or nonlinear effects that might impact logistic regression assumptions.

### **✅ Key Techniques and When to Use Them**
#### **🔹 1. Feature Binning**
- Convert continuous variables into discrete categories.
- Helps capture non-linear relationships between predictors and the log-odds of the outcome.
```python
import pandas as pd

# Quantile-based binning (equal number of samples)

df['binned_feature'] = pd.qcut(df['feature'], q=4)

# Fixed-width binning

df['binned_feature'] = pd.cut(df['feature'], bins=5)
```
**Use when:**
- Relationship between predictor and target is not strictly linear.
- There are extreme outliers impacting interpretation.
- You want to simplify decision thresholds.

#### **🔹 2. Feature Transformation**
- Reduce skewness, stabilize variance, and approximate linearity with the logit.

 **Common methods:**
```python
import numpy as np
# Log transformation (handles skew)

df['log_feature'] = np.log1p(df['feature'])  # log(1 + x) for safe zero handling
```
**Use when:**
- Right-skewed or highly non-linear numerical features.
- Preparing data for robust regularized logistic regression.

#### **📊 Visualizing the Effect of Binning or Transformation**
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['feature'], kde=True)
plt.title('Before Transformation')

sns.histplot(df['log_feature'], kde=True)

plt.title('After Log Transformation')
```

## 📘 Summary Table

| **Task**                         | **Tool / Method**                | **Use When…**                       |
| -------------------------------- | -------------------------------- | ----------------------------------- |
| Check outcome balance            | value_counts(), bar plot         | Always                              |
| Explore categorical predictors   | Cross-tab, bar plots             | Always (for categorical features)   |
| Explore numeric distributions    | Boxplot, histogram, KDE          | Always (for numeric features)       |
| Linearity of logit check         | Binned log-odds plot             | Advanced: numeric predictors        |
| Outlier detection                | Boxplot, IQR filtering           | Strong skews or extreme values      |
| Multicollinearity check          | Heatmap, VIF                     | Always with multiple predictors     |
| Feature binning / transformation | qcut, cut, log, power transforms | Nonlinear or highly skewed features |

___

### 🔗 **Related Notes**

- [[Links]]