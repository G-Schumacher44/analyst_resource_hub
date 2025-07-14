___
## 🎯 Purpose

This guidebook expands traditional logistic regression to cover **multiclass (nominal)** and **ordinal** classification tasks using extensions of the logit framework.

---

## 1️⃣ Multiclass (Multinomial) Logistic Regression

### 🔍 Overview

Multinomial logistic regression models outcomes with 3+ **unordered categories**, using one-vs-rest or full softmax-style probabilities.

* Target example: `{'low', 'medium', 'high'}` *(treated as nominal)*
* Implemented in `sklearn`, `statsmodels`, and `R` (`multinom`, `mlogit`)

---

### 🧮 Model Form (Softmax)

$$
P(Y = k \mid X) = \frac{\exp(X \cdot \beta_k)}{\sum_{j=1}^{K} \exp(X \cdot \beta_j)}
$$

Each class gets its own set of coefficients (compared to a reference class).

---

### 📦 Tools & Syntax

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(multi_class='multinomial', solver='lbfgs')
clf.fit(X, y)
```

```python
import statsmodels.api as sm
model = sm.MNLogit(y, sm.add_constant(X)).fit()
```

✔️ Use `predict_proba()` to return class probabilities

---

### 📊 Output Interpretation

* Coefficients represent log-odds of class *k* vs reference
* `np.exp(coef_)` returns relative odds ratios
* Watch for sign reversals when comparing class coefficients

---

## 2️⃣ Ordinal Logistic Regression

### 🔍 Overview

Ordinal logistic regression models outcomes with a natural **order**, using a single coefficient vector but multiple thresholds.

* Target example: `{'low' < 'medium' < 'high'}`
* Often referred to as **Proportional Odds Model**

---

### 🧮 Model Form

$$
\log \left( \frac{P(Y \leq j)}{P(Y > j)} \right) = \theta_j - X \cdot \beta
$$

* Each cutoff (j) has its own intercept `θ_j`
* The slope `β` is shared across classes

---

### ⚙️ Tooling

```python
# In Python (via mord package)
from mord import LogisticIT  # or LogisticAT for adjacent categories
model = LogisticIT().fit(X, y)
```

```r
# In R
polr(y ~ x1 + x2, data = df, method = "logistic")
```

✔️ Check proportional odds assumption before trusting output

---

### 📊 Output Interpretation

* Coefficients `β` → effect across all splits (assumes consistency)
* Intercepts `θ_j` → logit cutoff for class boundaries
* Interpretation is: "↑X increases odds of being in a **higher** category"

---

## 🔍 Assumptions Summary

| Model       | Key Assumption                                   |
| ----------- | ------------------------------------------------ |
| Multinomial | Independence of Irrelevant Alternatives (IIA)    |
| Ordinal     | Proportional Odds — same slope across thresholds |

---

## ✅ Guide Checklist

* [ ] Target reviewed for type (nominal vs ordinal)
* [ ] Model syntax matched to structure
* [ ] Assumptions checked (IIA or PO)
* [ ] Probabilities or odds correctly interpreted
* [ ] Evaluation metrics chosen based on task (macro-F1, accuracy, etc.)

---

## 💡 Tip

> “Multinomial predicts which. Ordinal predicts **how high**.”
