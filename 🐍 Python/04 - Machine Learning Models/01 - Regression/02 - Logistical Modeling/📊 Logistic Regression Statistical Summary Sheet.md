___
🎯 Purpose

This reference provides statistical evaluation tools and interpretation guidelines for logistic regression models. It supports binary and multiclass classification workflows with model fit diagnostics, threshold-aware metrics, and probability-based summaries.

---

## 📐 1. Core Classification Metrics

### ✅ Accuracy

Proportion of correct predictions.

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
```

---

### ✅ Precision, Recall, and F1 Score

Evaluate class-specific predictive performance.

```python
from sklearn.metrics import precision_score, recall_score, f1_score
```

* `average='binary'`, `'macro'`, `'weighted'` as needed

---

### ✅ Confusion Matrix

Compare predicted vs actual labels.

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_true, y_pred)
```

* Ideal for visual + text reporting

---

### ✅ ROC AUC (Area Under Curve)

Evaluates probability-based ranking ability.

```python
from sklearn.metrics import roc_auc_score
roc_auc_score(y_true, y_proba)
```

* Best for binary or OvR for multiclass

---

### ✅ Log Loss (Cross-Entropy)

Measures penalty for incorrect/confident predictions.

```python
from sklearn.metrics import log_loss
log_loss(y_true, y_proba)
```

* Lower is better

---

### ✅ Brier Score

Mean squared error of predicted probabilities.

```python
from sklearn.metrics import brier_score_loss
brier_score_loss(y_true, y_proba)
```

* Lower = better-calibrated model

---

## 📊 2. Logistic Regression Fit & Diagnostics

### ✅ McFadden’s Pseudo R²

Compares log-likelihoods against null model.

```python
1 - (model.llf / model.llnull)  # statsmodels
```

* Values closer to 1 are better (but lower than OLS R²)

---

### ✅ AIC / BIC (Model Selection Criteria)

Used to compare fit with complexity penalty.

```python
model.aic, model.bic  # statsmodels
```

* Lower = better fit

---

### ✅ Classification Report

One-line summary of precision, recall, F1, and support per class.

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

---

## 📈 3. Threshold + Probability Analysis

### ✅ Threshold Evaluation (beyond 0.5)

```python
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
```

### ✅ Calibration Curve

Compare predicted proba vs true class probability.

```python
from sklearn.calibration import calibration_curve
prob_true, prob_pred = calibration_curve(y_true, y_proba, n_bins=10)
```

---

## 🧾 4. Suggested Report Summary Table

| Field                | Description                          |
| -------------------- | ------------------------------------ |
| Model Type           | Logistic / Multinomial / Regularized |
| Accuracy / F1        | Basic classifier summary             |
| ROC AUC / Log Loss   | Probability performance              |
| Pseudo R² (McFadden) | Model fit (statsmodels only)         |
| AIC / BIC            | Fit vs complexity                    |
| Confusion Matrix     | Class-level correctness              |
| Calibration Status   | Raw vs Platt/Isotonic                |
| Threshold Logic Used | 0.5 default or custom cutoff         |

---

## 🧠 Final Tip

> “Logistic regression is interpretable, but not assumption-free. Combine statistical fit, threshold diagnostics, and class-level metrics to verify performance.”

Use with: ROC/PR Visual Guide, Evaluation Checklist, and Model Diagnostics Runner.
