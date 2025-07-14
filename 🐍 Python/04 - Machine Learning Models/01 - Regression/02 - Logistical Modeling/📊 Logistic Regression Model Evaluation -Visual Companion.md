#GAD #Coursera #dataAnalytics #regression 
Regression Analysis
**Course:** [[Google Advanced Data Analytics Certificate]]  
**Module:** 5
___
This guide pairs common evaluation metrics with **visual interpretations** and real-world insights.

---

## 🧩 Confusion Matrix

### 📈 Visual:
- 2×2 table showing True Positive (TP), False Positive (FP), False Negative (FN), True Negative (TN)
- Heatmap style preferred

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
```

### 🧠 Interpretation:
| Cell        | Meaning                        |
|-------------|---------------------------------|
| TP          | Correctly predicted positive    |
| FP          | Incorrectly predicted positive  |
| FN          | Missed positive                 |
| TN          | Correctly predicted negative    |

- **Diagonal dominance** (high TP/TN) = good model
- **High FP** = bad for precision
- **High FN** = bad for recall

---

## 📋 Classification Report

### 📈 Visual:
- Text output or table summarizing:
  - Precision
  - Recall
  - F1-score
  - Support (number of examples per class)

```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

### 🧠 Interpretation:
| Metric     | Insight                                  |
|------------|-------------------------------------------|
| Precision  | Trustworthiness of positive predictions  |
| Recall     | Coverage of actual positives             |
| F1-score   | Balanced metric if classes are imbalanced|

- Low precision: many false alarms
- Low recall: many missed positives

---

## 📈 ROC Curve + AUC

### 📈 Visual:
- Plot of **True Positive Rate** vs **False Positive Rate**
- AUC = area under the ROC curve

```python
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_test, clf.predict_proba(X_test)[:,1])
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], 'k--')  # Random guess line
```

### 🧠 Interpretation:
| AUC Value    | Meaning                              |
|--------------|---------------------------------------|
| ~0.5         | Random guessing                      |
| 0.7–0.8      | Acceptable                           |
| 0.8–0.9      | Good                                  |
| >0.9         | Excellent (but beware of overfitting!)|

- **Higher AUC** = better probability ranking model
- **ROC shape:** Closer to top-left = better

---

## 📊 Precision-Recall Curve (Bonus)

Better than ROC when working with highly **imbalanced datasets**.

```python
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(y_test, clf.predict_proba(X_test)[:,1])
plt.plot(recall, precision)
```

- Visualizes trade-off between precision and recall directly
- Use when **positives are rare** (e.g., fraud detection)

---

## ✅ Visual Summary
| Visual Type         | Primary Goal                     | When to Use                            |
|---------------------|-----------------------------------|----------------------------------------|
| Confusion Matrix    | Understand class prediction errors| Always                                 |
| Classification Report | Summarize precision/recall/F1 | Always                                 |
| ROC Curve + AUC     | Measure ranking ability           | Binary balanced/mid imbalance datasets |
| Precision-Recall Curve | Classify rare-event cases     | Imbalanced datasets (rare positives)   |

---

Would you like a mini notebook that auto-generates all these plots after fitting a model?


___

### 🔗 **Related Notes**

- [[Links]]