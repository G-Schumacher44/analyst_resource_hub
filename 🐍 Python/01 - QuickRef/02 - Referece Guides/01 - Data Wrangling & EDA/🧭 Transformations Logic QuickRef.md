___
🎯 Purpose

This QuickRef provides reusable code snippets and logic patterns for performing feature transformations before modeling. Includes encoding, scaling, normalization, binning, and mathematical transformations.

---

## 🔤 1. Categorical Encoding

```python
# One-hot encoding
pd.get_dummies(df['color'], prefix='color')

# Label encoding (tree models only!)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['state_code'] = le.fit_transform(df['state'])

# Ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['low', 'med', 'high']])
df['priority_code'] = oe.fit_transform(df[['priority']])
```

---

## 📏 2. Scaling & Normalization

```python
# Standard scaling (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[num_cols])

# Min-Max scaling (0 to 1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[num_cols])

# Robust scaling (resistant to outliers)
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
df_scaled = scaler.fit_transform(df[num_cols])
```

---

## 🧮 3. Log/Sqrt/Power Transforms

```python
# Log transform for positive-skewed numeric fields
df['log_income'] = np.log1p(df['income'])

# Square root transform (positive-only)
df['sqrt_size'] = np.sqrt(df['lot_size'])

# Yeo-Johnson (handles negative values)
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
df_transformed = pt.fit_transform(df[['skewed_var']])
```

✔️ Always inspect distribution **before and after**

---

## 🧱 4. Binning & Discretization

```python
# Equal-width bins
df['bin'] = pd.cut(df['age'], bins=5)

# Quantile-based binning
df['income_bin'] = pd.qcut(df['income'], q=4, labels=False)
```

---

## 🔀 5. Feature Interaction / Polynomial Expansion

```python
# Polynomial expansion (e.g. interaction + squares)
from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2, include_bias=False)
X_poly = pf.fit_transform(df[['x1', 'x2']])
```

✔️ Beware of multicollinearity when expanding features

---

## ✅ Transformation Checklist

* [ ] Numeric features scaled appropriately (standard, min-max, robust)
* [ ] Categorical fields encoded with model-specific logic
* [ ] Skewed features transformed (log/sqrt) where applicable
* [ ] Feature binning used to reduce noise or group sparse features
* [ ] Polynomial/interaction terms only included with justification

---

## 💡 Tip

> “The model will use whatever you feed it — your transformations decide what it sees.”
