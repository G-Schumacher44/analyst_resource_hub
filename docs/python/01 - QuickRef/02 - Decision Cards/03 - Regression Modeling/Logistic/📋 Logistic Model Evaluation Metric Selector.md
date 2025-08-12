___
## 🎯 Purpose

Use this card to decide which classification metric (Accuracy, Precision, Recall, AUC, F1) to prioritize when evaluating a logistic regression model. Grounded in business impact, class imbalance, and prediction cost.

---

## 📊 1. Metric Summary Table

| Metric        | Use When...                                      |
| ------------- | ------------------------------------------------ |
| **Accuracy**  | Classes are balanced and errors are equal cost   |
| **Precision** | False positives are costly (e.g. spam filter)    |
| **Recall**    | False negatives are costly (e.g. fraud, disease) |
| **F1 Score**  | Need balance between precision & recall          |
| **AUC/ROC**   | Want to rank probabilities across thresholds     |

✔️ Don’t rely on accuracy alone in imbalanced datasets.

---

## ⚖️ 2. Decision Matrix

| Scenario                                      | Metric to Prioritize                |
| --------------------------------------------- | ----------------------------------- |
| Flagging spam, promotions, or ads             | **Precision**                       |
| Catching fraud, churn, disease                | **Recall**                          |
| Balanced false pos & neg (general classifier) | **F1 Score**                        |
| Model is a risk scorer (not hard 0/1)         | **AUC / ROC**                       |
| Stakeholders want simple pass/fail report     | **Accuracy** (⚠️ Validate balance!) |

---

## 🧪 3. Visual Aids to Compare

```python
from sklearn.metrics import roc_auc_score, precision_recall_curve, classification_report

# Classification report summary
print(classification_report(y_true, y_pred))

# Precision-Recall vs Threshold
precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
```

✔️ Use visualizations to show tradeoffs between metrics.

---

## ✅ Metric Evaluation Checklist

* [ ] Target imbalance reviewed
* [ ] False Positive vs False Negative cost assessed
* [ ] Metric(s) selected and validated across thresholds
* [ ] Stakeholder-aligned explanation provided
* [ ] AUC/ROC used when probabilities matter more than labels

---

## 💡 Tip

> “Every metric tells a story — but only the right one answers the business question.”
