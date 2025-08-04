___
🎯 Purpose

This reference provides a structured overview of classification model evaluation metrics and statistical summaries. It supports model interpretation, diagnostics, and reporting across binary and multiclass classification tasks.

---

## 📐 1. Classification Metrics (Binary & Multiclass)

### ✅ Accuracy

Proportion of correct predictions.

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
```

* ⚠️ Misleading for imbalanced datasets

---

### ✅ Precision, Recall, and F1 Score

Measures of prediction quality by class.

```python
from sklearn.metrics import precision_score, recall_score, f1_score
precision_score(y_true, y_pred, average='binary')
recall_score(y_true, y_pred, average='binary')
f1_score(y_true, y_pred, average='binary')
```

* `average='macro'`, `'micro'`, or `'weighted'` for multiclass

---

### ✅ Confusion Matrix

Breakdown of predicted vs actual labels.

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_true, y_pred)
```

* Use with heatmaps or annotation for reports

---

### ✅ ROC AUC (Area Under Curve)

Measures ranking ability of classifier.

```python
from sklearn.metrics import roc_auc_score
roc_auc_score(y_true, y_proba)
```

* Best for binary or OvR multiclass with `y_proba`

---

### ✅ Log Loss (Cross Entropy)

Penalty for incorrect probabilities.

```python
from sklearn.metrics import log_loss
log_loss(y_true, y_proba)
```

* Sensitive to poorly calibrated outputs

---

### ✅ Matthews Correlation Coefficient (MCC)

Balanced metric for binary classification.

```python
from sklearn.metrics import matthews_corrcoef
matthews_corrcoef(y_true, y_pred)
```

* Works well for imbalanced classes

---

### ✅ Cohen’s Kappa

Measures agreement beyond chance.

```python
from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_true, y_pred)
```

* Useful for reviewer agreement or weak supervision

---

## 📊 2. Per-Class Statistics (Multiclass Models)

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

| Output Includes: | Description                        |
| ---------------- | ---------------------------------- |
| Precision        | Correctness of predicted positives |
| Recall           | Sensitivity to true positives      |
| F1-Score         | Balance of precision/recall        |
| Support          | Count of true instances per class  |

---

## 📈 3. Confidence + Probability Analysis

### Prediction Confidence Histogram

```python
plt.hist(y_proba, bins=20)
```

* Check model certainty and threshold behavior

### Brier Score (probability accuracy)

```python
from sklearn.metrics import brier_score_loss
brier_score_loss(y_true, y_proba)
```

* Lower is better; complements log loss

### Calibration Curve

```python
from sklearn.calibration import calibration_curve
prob_true, prob_pred = calibration_curve(y_true, y_proba, n_bins=10)
```

* Helps interpret output probability quality

---

## 🔎 4. Summary Table Elements (for Reports)

| Column             | Description                              |
| ------------------ | ---------------------------------------- |
| Model              | Model name or type                       |
| Accuracy / F1      | Summary performance                      |
| ROC AUC / PR AUC   | Probability performance                  |
| TP / FP / FN / TN  | Basic confusion stats                    |
| Top Features       | Feature importance (if available)        |
| Threshold Used     | If not default (0.5), must be documented |
| Calibration Status | Calibrated or raw probabilities?         |
| Version / Run Date | Metadata for reproducibility             |

---

## 🧠 Final Tip

> “Use at least one probability-based metric, one confusion-based metric, and one visual output in every classification summary.”

Use this in tandem with: Visual Guide, Classifier Evaluation Checklist, and Modeling Guidebook.
