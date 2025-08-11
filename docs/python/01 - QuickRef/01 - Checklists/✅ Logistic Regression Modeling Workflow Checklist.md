## 🎯 Purpose

This checklist provides a workflow for the modeling phase of a logistic regression project, from fitting the model to evaluating its performance and diagnosing potential issues.

---

## 🧭 Model Setup
- [ ] EDA complete (see logistic EDA checklist)
- [ ] Assumptions reviewed (logit linearity, collinearity)

## ⚙️ Model Fit
- [ ] Used `Logit()` or `LogisticRegression()`
- [ ] Interpreted coefficients and converted to odds ratios
- [ ] Reviewed confidence intervals and p-values

## 🧪 Evaluation
- [ ] Confusion matrix, precision, recall, F1
- [ ] ROC curve + AUC
- [ ] Classification report used for interpretation
- [ ] **Threshold Tuning:** Reviewed precision-recall curve to select an optimal threshold if needed.

## ⚠️ Diagnostics
- [ ] Reviewed Cook’s distance or leverage
- [ ] Addressed misclassified cases
- [ ] Considered model calibration if needed

---

## 🧠 Final Tip

> "A logistic model's success isn't just its accuracy, but its ability to rank risk. Always check the AUC and consider if the default 0.5 threshold meets your business goal."