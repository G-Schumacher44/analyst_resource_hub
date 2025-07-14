## 🎯 Purpose

This card provides a quick-reference tool to help analysts choose the right classification model based on problem characteristics, business requirements, and data constraints. Use it during exploration, modeling, or stakeholder alignment.

---

## ⚙️ Step 1: Problem Characteristics

| Question                               | If Yes... | Then Consider...                   |
| -------------------------------------- | --------- | ---------------------------------- |
| Is the target binary?                  | ✅         | Logistic Regression, NB, Tree      |
| Is the target multiclass (3+ classes)? | ✅         | Random Forest, Gradient Boosting   |
| Is class imbalance present?            | ✅         | Weighted Logistic, XGB, PR Curve   |
| Do you need model probabilities?       | ✅         | Calibrated Logistic, NB, XGB       |
| Is interpretability important?         | ✅         | Logistic Regression, Decision Tree |
| Is accuracy more important than speed? | ✅         | Random Forest, XGBoost             |
| Is the dataset large and noisy?        | ✅         | Gradient Boosting, RF              |
| Is data mostly text/categorical?       | ✅         | Naive Bayes, Tree-based models     |

---

## 🧰 Step 2: Model Preference Guide

| Preference               | Recommended Models                    |
| ------------------------ | ------------------------------------- |
| 🔎 Interpretability      | Logistic Regression, Decision Tree    |
| ⚡️ Speed / Simplicity    | Naive Bayes, Logistic, KNN            |
| 🧠 Nonlinear Flexibility | Random Forest, XGBoost, LightGBM      |
| 🧪 Probabilistic Output  | Logistic (calibrated), Naive Bayes    |
| 📈 Feature Impact        | Tree models with SHAP or permutation  |
| ⚖️ Imbalance Handling    | Weighted Logistic, XGB, SMOTE+Tree    |
| 🧬 Mixed Feature Types   | Tree-based models, Ensemble Pipelines |

---

## 📊 Step 3: Diagnostic Strategy by Model

| Model Type          | Suggested Diagnostics                        |
| ------------------- | -------------------------------------------- |
| Logistic Regression | ROC/AUC, Confusion Matrix, Calibration Curve |
| Naive Bayes         | Confusion Matrix, PR Curve                   |
| Random Forest       | SHAP, Feature Importance, ROC                |
| XGBoost             | SHAP, Log-Loss, Calibration Curve            |
| SVM                 | ROC, Confusion Matrix                        |
| KNN                 | Confusion Matrix, PR Curve                   |
| Neural Networks     | Confidence Histogram, PR Curve, Calibration  |

---

## 🧠 Final Reminders

* 🎯 Start simple, baseline with Logistic or Naive Bayes.
* ⚖️ Tune thresholds and test with multiple metrics.
* 📉 Visuals improve communication — always include CM, ROC/PR.
* 🔍 Use SHAP for any ensemble or "black-box" model in production.

---

Use this card during model planning, notebook prototyping, or team review sessions to maintain structure and clarity in model selection.
