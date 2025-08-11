___
## 🎯 Purpose

This guide provides advanced visual tools for analyzing the output of classification models. It complements the EDA and modeling guidebooks by focusing on post-model diagnostics, probability behavior, threshold analysis, and interpretability across binary and multiclass settings.

---

## 📉 1. Confusion Matrix (with Heatmap)

**Purpose:** Show accuracy and misclassification rates per class.

```python
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_true, y_pred, cmap="Blues")
```

✔️ Normalize by rows to visualize per-class recall
✔️ Annotate with % or count for stakeholders

---

## 📈 2. ROC Curve (Binary / Multiclass OvR)

**Purpose:** Measure model's ranking ability at different thresholds.

```python
from sklearn.metrics import roc_curve, roc_auc_score
```

* Plot TPR vs FPR
* Add `AUC` to legend for comparison

✔️ Use OvR format for multiclass classifiers
✔️ Use to compare multiple models on one plot

---

## 🌿 3. Precision-Recall Curve (Imbalanced Data)

**Purpose:** Reveal classifier performance on minority class.

```python
from sklearn.metrics import precision_recall_curve
```

✔️ Steep drop-off = model sensitivity to threshold
✔️ Use area under PR curve as stability measure

---

## 📦 4. Predicted Probability Histogram

**Purpose:** Show model confidence across samples.

```python
plt.hist(y_proba, bins=20)
```

✔️ Sharp peaks near 0 or 1 = confident classifier
⚠️ Flat or centered = underfit or poorly calibrated

---

## 📏 5. Calibration Curve (Reliability Plot)

**Purpose:** Compare predicted proba to actual likelihood.

```python
from sklearn.calibration import calibration_curve
```

✔️ Curve ≈ diagonal = well-calibrated
⚠️ Over/underconfidence curves inform post-hoc scaling

---

## 🧪 6. Threshold Tuning Plot

**Purpose:** Visualize how precision, recall, and F1 change across thresholds.

```python
from sklearn.metrics import precision_recall_curve
```

✔️ Identify optimal threshold (not always 0.5)
✔️ Pair with business cost matrix if available

---

## 🧠 7. SHAP / Feature Importance Plots

### For Tree Models:

```python
shap.summary_plot(shap_values, X_test)
```

### For Linear Models:

```python
sns.barplot(x=coefficients, y=feature_names)
```

✔️ Use to explain model behavior by input
✔️ Export visuals to stakeholder decks

---

## 🧭 8. Per-Class Breakdown (Multiclass Models)

**Purpose:** Visually diagnose class-level performance.

* Confusion matrix heatmap (normalized)
* One-vs-rest ROC/PR curves
* Class-specific confidence histograms

✔️ Flag underperforming classes by color threshold
✔️ Use radar plots for class summary profiles

---

## 📋 Analyst Visual Review Checklist

* [ ] Confusion matrix plotted and interpreted
* [ ] ROC or PR curve plotted by class
* [ ] Probability distribution reviewed
* [ ] Calibration plot created
* [ ] Threshold vs F1/Recall chart analyzed
* [ ] SHAP or feature impact plot exported
* [ ] Stakeholder visuals saved

---

## 💡 Final Tip

> “Visuals are your interface between model truth and stakeholder understanding. Always tune thresholds and validate confidence.”

Use with: Classifier Statistical Summary Sheet, Evaluation Checklist, and Modeling Guidebook.
