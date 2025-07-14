___
## 🎯 Purpose

Use this card to determine when and how to apply feature transformations for linear models (OLS, Ridge, Lasso, ElasticNet). Helps identify skewed distributions, scaling needs, and encoding strategies.

---

## 🔍 1. Trigger Logic by Feature Type

### 🔹 Numeric (Continuous)

| Condition                          | Transformation                 |      |                        |
| ---------------------------------- | ------------------------------ | ---- | ---------------------- |
| Highly skewed (                    | skew                           | > 1) | Log, Sqrt, Yeo-Johnson |
| Strong outliers                    | RobustScaler or log/sqrt       |      |                        |
| Normal shape but different scales  | StandardScaler                 |      |                        |
| Nonlinear relationship with target | Polynomial features or binning |      |                        |

### 🔹 Categorical

| Condition                               | Transformation                                         |
| --------------------------------------- | ------------------------------------------------------ |
| Few unique values (<10)                 | One-hot encoding                                       |
| Ordinal category (e.g., low, med, high) | Ordinal encoding                                       |
| High-cardinality (>15)                  | Binary encoding or dimensionality reduction (optional) |

---

## 🧪 2. Visual + Statistical Triggers

| Signal                                | Action                            |
| ------------------------------------- | --------------------------------- |
| Skewed histogram                      | Apply log or sqrt transform       |
| Long right tail                       | Use log1p or robust scale         |
| Large variance across numeric columns | Normalize or standardize          |
| Strong multicollinearity              | Use VIF to flag + drop or combine |

---

## 🔁 3. Common Transform Functions

```python
# Standard Scaling
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)

# Log Transform
import numpy as np
X['log_var'] = np.log1p(X['skewed_var'])

# One-hot Encoding
pd.get_dummies(X['category'])

# Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(categories=[['low', 'med', 'high']])
X['encoded'] = encoder.fit_transform(X[['priority']])
```

---

## ✅ Checklist Before Linear Modeling

* [ ] All continuous features reviewed for skew/outliers
* [ ] All numeric variables scaled appropriately
* [ ] Categorical fields encoded to avoid implicit order (unless intentional)
* [ ] Feature interactions or polynomials added if nonlinear patterns expected
* [ ] Multicollinearity checked (VIF < 5 for main predictors)

---

## 💡 Tip

> “Transform before you model — or your model will just learn to transform.”
