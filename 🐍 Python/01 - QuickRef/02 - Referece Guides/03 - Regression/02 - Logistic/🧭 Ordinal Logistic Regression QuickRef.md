___
🎯 Purpose

This QuickRef covers ordinal logistic regression — a model used when the target variable is **ordered** but not continuous. Commonly used in rating scales, satisfaction levels, or risk categories.

---

## 📦 1. When to Use

| Condition                                         | Use Ordinal Logistic?      |
| ------------------------------------------------- | -------------------------- |
| Target has ≥3 **ordered** categories              | ✅ Yes                      |
| Values have clear ranking (e.g. low < med < high) | ✅ Yes                      |
| Target is unordered                               | ❌ Use multinomial logistic |
| Continuous regression needed                      | ❌ Use linear model         |

---

## 🧮 2. Model Logic (Proportional Odds)

The model assumes a single set of coefficients across multiple threshold logits:

$$
\log \left( \frac{P(Y \leq j)}{P(Y > j)} \right) = \theta_j - X \cdot \beta
$$

* `θ_j` = intercept (cutoff) for category *j*
* `β` = shared coefficient vector

---

## ⚙️ 3. Fitting the Model

```python
# Python (mord package)
from mord import LogisticIT
model = LogisticIT().fit(X, y)
```

```r
# R (MASS package)
polr(y ~ x1 + x2, data = df, method = "logistic")
```

✔️ Encode target labels as ordered integers (0, 1, 2, ...)

---

## 📊 4. Output Interpretation

| Output            | Meaning                                        |
| ----------------- | ---------------------------------------------- |
| Coef (β)          | Effect on odds of being in **higher** category |
| Intercepts (θ\_j) | Logit cutoffs between class levels             |
| `exp(coef)`       | Proportional odds ratio per feature            |

✔️ “A 1-unit increase in X increases odds of being in a **higher** category by OR.”

---

## 🧪 5. Assumptions

| Assumption         | Notes                                         |
| ------------------ | --------------------------------------------- |
| Proportional Odds  | Effect of X is consistent across class splits |
| Linearity in logit | X must relate linearly to cumulative logit    |

📉 If violated: Consider adjacent-category models or partial proportional odds models

---

## ✅ Modeling Checklist

* [ ] Target verified as ordered (e.g. ordinal categories or numeric codes)
* [ ] Model fit with ordinal-compatible library (mord, polr, etc.)
* [ ] Intercepts and β interpreted with respect to category ordering
* [ ] Proportional odds assumption considered or tested

---

## 💡 Tip

> “Ordinal logistic doesn’t ask *which* class — it asks *how far up the scale you’re likely to go.*”
