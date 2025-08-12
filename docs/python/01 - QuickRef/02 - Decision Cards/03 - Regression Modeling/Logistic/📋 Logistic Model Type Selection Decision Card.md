___
## 🎯 Purpose

Use this card to choose between **Binary**, **Multiclass (Multinomial)**, or **Ordinal** Logistic Regression models based on the nature of your target variable.

---

## 1️⃣ Target Type Breakdown

| Target Type                       | Example                | Use Model                       |
| --------------------------------- | ---------------------- | ------------------------------- |
| Binary (2 classes)                | 0/1, Yes/No, Pass/Fail | Binary Logistic Regression      |
| Multiclass (≥3 unordered classes) | A, B, C (no ranking)   | Multinomial Logistic Regression |
| Ordinal (≥3 ordered classes)      | Low < Med < High       | Ordinal Logistic Regression     |

✔️ The type of logistic model **always depends on the target variable**

---

## 🛠️ 2. Tooling Map

| Model Type | Python Tool                                                   | R Tool                        |
| ---------- | ------------------------------------------------------------- | ----------------------------- |
| Binary     | `LogisticRegression()`                                        | `glm(..., family = binomial)` |
| Multiclass | `multi_class='multinomial'` + `solver='lbfgs'`                | `nnet::multinom()`            |
| Ordinal    | `mord.LogisticIT()` or `statsmodels.miscmodels.ordinal_model` | `MASS::polr()`                |

---

## 📏 3. Interpretation Layer

| Model      | Coefficients Tell You...                   |
| ---------- | ------------------------------------------ |
| Binary     | Log-odds of 1 vs 0                         |
| Multiclass | Log-odds of each class vs reference class  |
| Ordinal    | Log-odds of being in a **higher** category |

---

## ✅ Model Choice Checklist

* [ ] Target variable analyzed for number of classes
* [ ] Ordering of target clarified (ranked or nominal)
* [ ] Model matched to structure
* [ ] Fitting tool syntax selected and validated
* [ ] Interpretation aligned to business framing

---

## 💡 Tip

> “Logistic regression is a family — choose the branch that fits your target’s structure.”
