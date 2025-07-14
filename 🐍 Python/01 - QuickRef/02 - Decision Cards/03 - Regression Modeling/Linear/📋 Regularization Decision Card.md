___
## 🎯 Purpose

Use this decision card to choose between Ridge, Lasso, and ElasticNet regression based on your dataset structure, modeling goals, and need for feature selection or multicollinearity control.

---

## 🧠 1. Method Comparison

| Method     | Penalty           | Primary Effect                    |
| ---------- | ----------------- | --------------------------------- |
| Ridge      | L2 (squared sum)  | Shrinks coefficients, keeps all   |
| Lasso      | L1 (absolute sum) | Shrinks + selects (sparse output) |
| ElasticNet | L1 + L2 hybrid    | Balance between shrink + select   |

✔️ All methods reduce overfitting and handle multicollinearity.

---

## 📌 2. When to Use Each

| Use Case                                  | Choose...  |
| ----------------------------------------- | ---------- |
| High multicollinearity, keep all features | Ridge      |
| Need automatic feature selection          | Lasso      |
| Many correlated predictors + want balance | ElasticNet |

✔️ ElasticNet is ideal when Lasso is too aggressive and Ridge retains too much noise.

---

## ⚙️ 3. Tuning Considerations

| Param                   | Notes                               |
| ----------------------- | ----------------------------------- |
| `alpha`                 | Higher = stronger regularization    |
| `l1_ratio` (ElasticNet) | 0 = Ridge, 1 = Lasso, 0.5 = balance |

```python
# ElasticNet example:
ElasticNet(alpha=0.1, l1_ratio=0.5)
```

✔️ Always scale your features before regularization.

---

## 🔍 4. Output Expectations

| Method     | What You'll See                                        |
| ---------- | ------------------------------------------------------ |
| Ridge      | All features retained, small coefficients              |
| Lasso      | Some coefficients driven to zero (selected model)      |
| ElasticNet | Shrunk + selected balance, some near-zero coefficients |

---

## ✅ Decision Checklist

* [ ] Multicollinearity detected or suspected
* [ ] Need feature selection? → Lasso or ElasticNet
* [ ] Need only shrinkage? → Ridge
* [ ] All features scaled
* [ ] Tuning (`alpha`, `l1_ratio`) cross-validated

---

## 💡 Tip

> "Use Ridge to stabilize, Lasso to simplify, and ElasticNet to balance the two."
