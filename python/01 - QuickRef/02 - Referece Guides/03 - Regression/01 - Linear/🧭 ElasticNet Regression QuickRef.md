___
🎯 Purpose

This QuickRef provides a clean walkthrough for using **ElasticNet Regression**, which blends Ridge and Lasso to balance shrinkage and sparsity in high-dimensional linear models.

---

## 📦 1. When to Use ElasticNet

| Scenario                              | Why ElasticNet Works                                    |
| ------------------------------------- | ------------------------------------------------------- |
| Many correlated features              | Combines L2 shrinkage (Ridge) with L1 selection (Lasso) |
| Lasso is too aggressive               | ElasticNet allows partial feature retention             |
| Need compromise between shrink + drop | ElasticNet balances both tendencies                     |
| Want tunable regularization behavior  | Adjust `l1_ratio` for control                           |

---

## ⚙️ 2. How It Works

* Uses a mix of **L1 + L2** penalties:

$$
\text{Loss} = RSS + \alpha \left( \rho \sum |w_i| + (1-\rho) \sum w_i^2 \right)
$$

* `alpha`: controls overall regularization strength
* `l1_ratio`: determines Ridge vs Lasso behavior (0 = Ridge, 1 = Lasso)

---

## 🛠️ 3. Fitting ElasticNet in sklearn

```python
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(StandardScaler(), ElasticNet(alpha=0.1, l1_ratio=0.5))
model.fit(X_train, y_train)
```

✔️ Always scale features before fitting

---

## 🔁 4. Cross-Validation & Tuning

```python
from sklearn.linear_model import ElasticNetCV
model = ElasticNetCV(l1_ratio=[.1, .5, .9], cv=5).fit(X, y)
```

| Param        | Effect                                  |
| ------------ | --------------------------------------- |
| `alpha ↑`    | Increases shrinkage overall             |
| `l1_ratio ↑` | More feature selection (Lasso-like)     |
| `l1_ratio ↓` | More coefficient shrinkage (Ridge-like) |

---

## 📊 5. Output Interpretation

| Coefficients            | Interpretation                 |
| ----------------------- | ------------------------------ |
| = 0                     | Feature dropped (L1 effect)    |
| ≠ 0 (small)             | Retained with shrinkage        |
| Mix of zero and nonzero | Balanced model (Ridge + Lasso) |

✔️ Use `R²`, `MAE`, `RMSE` for evaluation

---

## ✅ Modeling Checklist

* [ ] Features scaled prior to fitting
* [ ] `alpha` and `l1_ratio` tuned with CV
* [ ] Zeroed features reviewed for model implications
* [ ] Compared vs Ridge and Lasso performance

---

## 💡 Tip

> “ElasticNet is your safety net — when Ridge keeps too much and Lasso cuts too deep.”
