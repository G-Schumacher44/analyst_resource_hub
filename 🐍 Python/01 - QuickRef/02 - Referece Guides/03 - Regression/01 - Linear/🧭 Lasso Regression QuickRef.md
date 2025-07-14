___
🎯 Purpose

This QuickRef guides you through the logic, fitting process, and interpretation of **Lasso Regression** — a linear model with built-in feature selection via L1 regularization.

---

## 📦 1. When to Use Lasso

| Scenario                           | Why Lasso Works                             |
| ---------------------------------- | ------------------------------------------- |
| Many weak or irrelevant predictors | Drives unimportant coefficients to zero     |
| Need automated feature selection   | Simplifies model by removing noise features |
| Overfitting in OLS                 | Regularizes with variable removal           |
| High-dimensional (p > n) data      | Useful when predictors > observations       |

---

## ⚙️ 2. How It Works

* Adds **L1 penalty** to loss function:

$$
\text{Loss} = RSS + \alpha \sum |w_i|
$$

* Forces some coefficients to exactly zero — feature selection built-in

---

## 🛠️ 3. Fitting Lasso in sklearn

```python
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), Lasso(alpha=0.1))
model.fit(X_train, y_train)
```

✔️ Always scale features before fitting

---

## 🔁 4. Tuning Alpha

```python
from sklearn.linear_model import LassoCV
model = LassoCV(cv=5).fit(X, y)
```

| Alpha ↑ | Effect                                  |
| ------- | --------------------------------------- |
| Low     | Keeps more features (closer to OLS)     |
| High    | Drops more features, increases sparsity |

---

## 📊 5. Output Interpretation

| Coefficients  | Meaning                           |
| ------------- | --------------------------------- |
| = 0           | Dropped by model (not predictive) |
| ≠ 0           | Kept in model — shrunk estimate   |
| Sparse output | Makes downstream models simpler   |

✔️ Use with caution if interpretability or p-values are critical

---

## ✅ Modeling Checklist

* [ ] All features standardized
* [ ] `alpha` selected via cross-validation
* [ ] Zeroed features interpreted as "dropped"
* [ ] Model evaluated vs OLS or Ridge

---

## 💡 Tip

> “Lasso isn’t just about shrinkage — it’s your first line of defense against irrelevant features.”
