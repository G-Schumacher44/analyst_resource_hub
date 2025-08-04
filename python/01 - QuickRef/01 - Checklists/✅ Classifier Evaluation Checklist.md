## 🎯 Purpose

This checklist helps ensure thorough, appropriate, and reproducible evaluation of classifier models. It guides analysts through metric selection, diagnostics, calibration, and deployment-readiness for both binary and multiclass problems.

---

## 🔍 1. Problem Framing

* [ ] Is this a **binary**, **multiclass**, or **multilabel** problem?
* [ ] Is there **class imbalance**?
* [ ] What are the **costs of false positives vs false negatives**?
* [ ] Is the goal **ranking**, **probability estimation**, or **classification**?

---

## 📊 2. Metric Selection

| Metric        | Use When                              | Avoid When                      |
| ------------- | ------------------------------------- | ------------------------------- |
| Accuracy      | Balanced classes, simple reporting    | Imbalanced data                 |
| Precision     | False positives are expensive         | Need sensitivity                |
| Recall        | False negatives are costly            | Need specificity                |
| F1 Score      | Balance of precision/recall           | No severe class imbalance       |
| ROC-AUC       | Rank performance, general binary task | Imbalanced problems             |
| PR-AUC        | Imbalanced datasets                   | Balanced data                   |
| Log-Loss      | Probabilistic confidence              | Not needed for hard classifiers |
| Cohen’s Kappa | Chance-adjusted agreement             | Often ignored in ML settings    |

---

## 📈 3. Visual Diagnostics

* [ ] Confusion matrix (raw and normalized)
* [ ] ROC curve with AUC
* [ ] Precision-recall curve
* [ ] Calibration curve (for probability reliability)
* [ ] Class probability distribution or histogram
* [ ] SHAP or permutation-based feature importance (if applicable)

---

## 🧪 4. Validation Strategy

* [ ] Train/test split or CV preserves class balance (StratifiedKFold)
* [ ] Repeated CV or bootstrap for small datasets
* [ ] Nested CV for model + parameter selection
* [ ] Used multiple scoring functions during CV

---

## 🧰 5. Risk Mitigation

* [ ] Tested alternative thresholds (not just 0.5)
* [ ] Used cost matrix or business rules to define cutoff
* [ ] Used class\_weight or resampling techniques (SMOTE, etc.)
* [ ] Assessed overfitting via training vs test performance
* [ ] Considered simplicity vs overcomplexity tradeoff

---

## 🚀 6. Production Readiness

* [ ] Probabilities calibrated (Platt, Isotonic)
* [ ] Classifier exported with threshold or scoring guidance
* [ ] Model version tracked (with hyperparameters + metrics)
* [ ] Model fairness checked (if applicable)
* [ ] Decision curve or cost-benefit visual prepared for stakeholders

---

## 📌 Recommendation Card

| If...                          | Then Use...                           |
| ------------------------------ | ------------------------------------- |
| Need transparency              | Logistic Regression, Decision Tree    |
| Need performance on mixed data | Random Forest, Gradient Boosting      |
| Need calibrated probabilities  | CalibratedClassifierCV + ROC/PR curve |
| Dealing with major imbalance   | Weighted logistic, PR curve, SMOTE    |
| Stakeholders require visuals   | Confusion matrix + SHAP or importance |

---

## 🧠 Final Tip

> “No single metric tells the full story. Use complementary tools to explain, verify, and stress-test your model in context.”
