___
## 🎯 Purpose

Use this card to decide when to apply transformations when working with **logistic regression**, **Poisson**, or **negative binomial models**. Focuses on skew handling, scale sensitivity, and model assumptions.

---

## 🔍 1. Trigger Logic by Feature Type

### 🔹 Numeric (Continuous)

| Condition                                        | Transformation                                                   |      |                         |
| ------------------------------------------------ | ---------------------------------------------------------------- | ---- | ----------------------- |
| Right-skewed distribution (                      | skew                                                             | > 1) | ✅ Log or Sqrt Transform |
| Wide magnitude spread                            | ✅ StandardScaler or MinMaxScaler (esp. for regularized logistic) |      |                         |
| Count-based exposure (e.g., `minutes`, `visits`) | ✅ Log or Offset transform (Poisson/Negative Binomial)            |      |                         |

### 🔹 Categorical

| Condition            | Transformation                               |
| -------------------- | -------------------------------------------- |
| Nominal (unordered)  | ✅ One-hot Encoding                           |
| Ordinal (known rank) | ✅ Ordinal Encoding                           |
| High-cardinality     | 🔁 Grouping, embedding, or collapse (manual) |

---

## 🧪 2. Model-Specific Cues

| Model                   | Trigger                                 | Action                                      |
| ----------------------- | --------------------------------------- | ------------------------------------------- |
| **Logistic Regression** | Skewed numeric, regularization          | Scale or log                                |
| **Poisson Regression**  | Log-linear fit assumption               | Log transform predictors + offset(optional) |
| **Negative Binomial**   | Same as Poisson, handles overdispersion | Same transforms apply                       |

---

## 🔁 3. Common Transform Functions

```python
# Standard Scaling
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)

# Log transform for positive skewed count data
X['log_visits'] = np.log1p(X['visits'])

# One-hot encoding for categorical
X = pd.get_dummies(X, columns=['device_type'])

# Offset for Poisson
model = sm.GLM(y, X, family=sm.families.Poisson(), offset=np.log(X['exposure']))
```

---

## ✅ Checklist Before Modeling

* [ ] Numeric features reviewed for skew or count-like structure
* [ ] Categorical variables encoded correctly (one-hot or ordinal)
* [ ] For Poisson/NB: offset column included (log of exposure)
* [ ] Scaled if using regularized logistic (L1/L2)
* [ ] Transforms documented and justified in EDA or notebook

---

## 💡 Tip

> “When modeling probabilities or counts, log is your best friend — but only when used intentionally.”
