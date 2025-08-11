___
## 🎯 Purpose

Use this card to decide how to encode categorical variables based on model type, field cardinality, and downstream interpretability needs.

---

## 🔤 1. Encoding Options Overview

| Encoding Method            | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| **One-Hot Encoding**       | Creates binary columns for each category (no rank assumed)                  |
| **Label Encoding**         | Converts categories to numeric integers (rank implied!)                     |
| **Ordinal Encoding**       | Assigns ordered numeric values based on known category hierarchy            |
| **Binary Encoding**        | Hashes categories into fewer binary digits (efficient for high cardinality) |
| **Target / Mean Encoding** | Replaces category with target mean (use with caution, risk of leakage)      |

---

## 🧭 2. When to Use Which

| Situation                                               | Recommended Encoding                 |
| ------------------------------------------------------- | ------------------------------------ |
| Low-cardinality categorical (e.g. gender)               | ✅ One-Hot                            |
| Tree-based models (RF, XGB, LGBM)                       | ✅ Label or Ordinal                   |
| Linear models (LR, Ridge)                               | ✅ One-Hot (to avoid rank assumption) |
| Ordinal relationship exists (e.g. 'low', 'med', 'high') | ✅ Ordinal Encoding                   |
| High-cardinality (>15 categories)                       | ✅ Binary or Target Encoding          |

---

## 🧪 3. Tooling Examples

```python
# One-hot encoding
pd.get_dummies(df['color'])

# Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['encoded'] = le.fit_transform(df['state'])

# Ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['low', 'med', 'high']])
df['ordered'] = oe.fit_transform(df[['priority']])
```

---

## ⚠️ 4. Watch For

* Label encoding **injects ordinal structure** — avoid with linear models
* One-hot encoding **can explode feature space** if too many categories
* Target encoding **leaks target** unless cross-validated or regularized

---

## ✅ Decision Checklist

* [ ] Cardinality of each categorical feature reviewed
* [ ] Downstream model type considered
* [ ] Interpretability and feature explosion balanced
* [ ] Rank relationships respected (ordinal vs nominal)
* [ ] Target encoding used safely (with validation splits)

---

## 💡 Tip

> “How you encode today decides what your model assumes tomorrow.”
