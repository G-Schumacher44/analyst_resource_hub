___
🎯 Purpose

Use this card to decide whether **Ordinal Logistic Regression** is appropriate by evaluating the **Proportional Odds (PO)** assumption. PO assumes that predictor effects are constant across all cumulative logit thresholds.

---

## 📐 1. What is the PO Assumption?

The effect of each predictor is assumed to be **equal across all splits** in the ordinal target.

$$
\log \left( \frac{P(Y \leq j)}{P(Y > j)} \right) = \theta_j - X \cdot \beta
$$

✔️ If this assumption holds, a single slope vector `β` applies to all logit splits.

---

## 🧪 2. When to Suspect Violation

| Symptom                                           | Action               |
| ------------------------------------------------- | -------------------- |
| Different predictors affect different thresholds  | PO may be violated   |
| Residuals or marginal effects vary by class group | Suspect PO violation |
| Strong nonlinearity in feature vs threshold plots | Consider relaxing PO |

---

## 🛠️ 3. How to Check the Assumption

| Tool                                    | Approach                                       |
| --------------------------------------- | ---------------------------------------------- |
| `brant()` in R                          | Formal test of PO assumption for each variable |
| Compare slope plots across class splits | Visual inconsistency suggests PO failure       |
| Fit parallel binary logistic models     | Test for consistent slopes manually            |

---

## 🔁 4. Alternatives if PO Fails

| Option                              | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| Partial Proportional Odds Model     | Allows some slopes to vary, others stay constant |
| Adjacent-Category Logit             | Models odds between neighboring categories       |
| Nonparametric or Tree-Based Ordinal | Use ordinal classification trees                 |

---

## ✅ PO Evaluation Checklist

* [ ] Target verified as ordinal
* [ ] Assumption formally tested or visualized
* [ ] Predictor effects reviewed across logit splits
* [ ] Alternate model considered if PO violated
* [ ] Business interpretation updated for model structure

---

## 💡 Tip

> “Ordinal logistic regression is powerful — but only when its threshold logic speaks with one voice.”
