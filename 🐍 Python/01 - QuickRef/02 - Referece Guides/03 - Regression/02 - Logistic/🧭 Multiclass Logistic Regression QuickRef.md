___
🎯 Purpose

This QuickRef covers multinomial (multiclass) logistic regression — a generalization of binary logistic used when your target variable has 3 or more **unordered** classes.

---

## 📦 1. When to Use

| Condition                             | Use Multiclass Logistic |
| ------------------------------------- | ----------------------- |
| Target has ≥3 unordered categories    | ✅ Yes                   |
| Categories have no rank or order      | ✅ Yes                   |
| Binary target                         | ❌ Use standard logistic |
| Ordered categories (low < med < high) | ❌ Use ordinal logistic  |

Examples: Customer segments, product types, political affiliation

---

## 🧮 2. Model Logic (Softmax Function)

$$
P(Y = k \mid X) = \frac{\exp(X \cdot \beta_k)}{\sum_{j=1}^{K} \exp(X \cdot \beta_j)}
$$

Each class *k* has its own coefficient vector `β_k`, compared to a baseline (reference) class.

---

## 🛠️ 3. Fitting the Model

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(multi_class='multinomial', solver='lbfgs')
clf.fit(X_train, y_train)
```

```python
# statsmodels implementation
import statsmodels.api as sm
model = sm.MNLogit(y, sm.add_constant(X)).fit()
```

✔️ Use `predict_proba()` for class probabilities

---

## 📊 4. Output Interpretation

| Output            | Meaning                                |
| ----------------- | -------------------------------------- |
| `coef_`           | Log-odds of class k vs reference       |
| `np.exp(coef_)`   | Odds ratio for each class vs baseline  |
| `predict_proba()` | Class probability distribution per row |

---

## ⚠️ 5. Assumptions

| Assumption                                    | Notes                                                                                    |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Independence of Irrelevant Alternatives (IIA) | Assumes relative odds between any two categories do not depend on the presence of others |
| No ordering                                   | Categories must be nominal, not ordinal                                                  |

---

## ✅ Modeling Checklist

* [ ] Confirm target is nominal (unordered, ≥3 classes)
* [ ] Model fit using `multi_class='multinomial'` and proper solver (e.g. lbfgs)
* [ ] Probabilities interpreted using softmax logic
* [ ] Log-odds and odds ratios clearly reported
* [ ] IIA assumption acknowledged or tested (esp. in `statsmodels`)

---

## 💡 Tip

> “Binary logistic picks yes/no. Multiclass logistic asks: *which one?*”
