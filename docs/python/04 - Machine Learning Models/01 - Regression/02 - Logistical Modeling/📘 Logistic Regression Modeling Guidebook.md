___

## 🎯 Purpose
This guidebook provides a complete reference for understanding, preparing, and modeling binary outcomes using **logistic regression**. It includes EDA, assumption checks, model building, diagnostics, and interpretation strategies.

---

## 🧭 1. Problem Setup

### ✅ Use Logistic Regression When:
- Your **dependent variable is binary** (e.g., 0/1, Yes/No)
- You want to estimate the **probability of an event**
- Predictors can be numerical or categorical

### 🔢 Model Formula:
$$
P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X_1 + \cdots + \beta_kX_k)}}
$$

### ✅ Use Binomial Logistic Regression When:
- Your **dependent variable is binary** (e.g., 0/1, Yes/No)
- You want to estimate the **probability of success vs failure**
- This is also called **binary** or **binomial logistic regression**

## 🧮 Variants of Logistic Regression

### 🔁 Multinomial Logistic Regression
- Use when the target has **3+ unordered categories** (e.g., 'Low', 'Medium', 'High')
- Models class probabilities using **softmax function**
- `sklearn.linear_model.LogisticRegression(multi_class='multinomial', solver='lbfgs')`

### 📊 Ordinal Logistic Regression (Proportional Odds)
- Use when the target has **ordered categories** (e.g., 'Poor', 'Fair', 'Good')
- Available via `statsmodels.miscmodels.ordinal_model.OrdinalModel`

### 🧮 Poisson and Negative Binomial Regression
- Used for **count outcomes** (0, 1, 2...)
- Poisson assumes equal mean and variance
- Negative Binomial handles **overdispersion** (variance > mean)
- Libraries: `statsmodels.genmod.generalized_linear_model.GLM` with Poisson/NegBinomial family
---

## 🔍 2. Pre-Model EDA Checklist

- ✅ Class balance (target variable)
- ✅ Boxplots or KDEs of numeric features by outcome
- ✅ Crosstabs of categorical features by outcome
- ✅ Check linearity of logit (binned plots)
- ✅ Multicollinearity (heatmap + VIF)

See: [[📊 Advanced Visual EDA Guide for Logistic Regression]], [[🧭 Logistic Regression EDA Quickref]]

---

## 📐 3. Fit the Model

### Using `statsmodels`
```python
import statsmodels.api as sm
X = sm.add_constant(X)
model = sm.Logit(y, X).fit()
model.summary()
```

### Using `sklearn`
```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train, y_train)
```
---

## 📈 4. Interpret Output

### `statsmodels`
| Element          | Meaning                                      |
|------------------|----------------------------------------------|
| coef             | Change in log odds per unit increase in X    |
| exp(coef)        | Odds ratio (effect on odds)                  |
| p-value          | Significance of predictor                    |
| conf. interval   | Range of expected effect                     |

```python
np.exp(model.params)  # Convert to odds ratios
```

### `sklearn`
| Attribute         | Meaning                                      |
|------------------|-----------------------------------------------|
| `clf.coef_`       | Coefficient estimates                        |
| `clf.intercept_`  | Intercept                                    |
| `clf.predict()`   | Class prediction                            |
| `clf.predict_proba()` | Predicted probabilities                |

---
## 📊 5. Model Evaluation and Classification Metrics

Model evaluation in classification involves understanding not just the overall accuracy, but the balance between true positives, false positives, false negatives, and the quality of probability-based predictions. Below are the most commonly used metrics and how to interpret them in practical use.

### Confusion Matrix
Used to visualize the actual vs. predicted class breakdown — useful for understanding how many true positives (TP), false positives (FP), false negatives (FN), and true negatives (TN) your model produced.
```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
```
- Useful for interpreting imbalance problems or misclassification types
- Should always be paired with class labels if imbalanced
---

### 📋 Important Note on `.predict_proba()` and Confusion Matrix

To generate a confusion matrix, you must supply **class labels (0 or 1)**, not probabilities.

There are two ways to obtain class labels:

- Use `.predict()` directly (applies default threshold of 0.5 internally)
- Use `.predict_proba()` and manually apply a custom threshold

Example (Custom Threshold):
```python
# Predict probabilities
proba = clf.predict_proba(X_test)[:, 1]

# Manually threshold probabilities to generate labels
y_pred_custom = (proba > 0.6).astype(int)

# Now you can evaluate
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred_custom)
### Classification Report
Summarizes **precision**, **recall**, **F1-score**, and **support** for each class.
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```
- **Precision**: What proportion of predicted positives are truly positive?
- **Recall**: What proportion of actual positives were identified correctly?
- **F1-Score**: Harmonic mean of precision and recall — good for imbalanced classes

### Accuracy, Precision, Recall, and F1-Score

Manually extract the core evaluation metrics for reporting, threshold tuning, or optimization.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
```

| Metric        | Meaning                                          | When to Prioritize |
|---------------|---------------------------------------------------|--------------------|
| **Accuracy**  | Overall percentage of correct predictions        | Balanced datasets with equal cost of FP/FN |
| **Precision** | How many predicted positives were correct         | High cost of false positives (e.g., spam detection) |
| **Recall**    | How many actual positives were identified         | High cost of false negatives (e.g., cancer screening) |
| **F1-Score**  | Harmonic mean of precision and recall             | Best for imbalanced datasets or uneven class importance |

---

### 🧠 Key Notes:
- Accuracy can be misleading if classes are imbalanced.
- Precision, Recall, and F1 are directly derived from the confusion matrix (TP, FP, FN).
- Use **F1-Score** if you need a balanced tradeoff between Precision and Recall.

✅ Use `.predict()` outputs (not `.predict_proba()`) to calculate these metrics.
___

### ROC Curve + AUC
Used for evaluating **probabilistic classifiers**. Measures the trade-off between TPR (Recall) and FPR at various threshold levels.
```python
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_test, y_proba[:, 1])
plt.plot(fpr, tpr)
```
- **ROC Curve**: Visualizes performance over all thresholds
- **AUC** (Area Under Curve): 1.0 = perfect, 0.5 = random guessing
- Ideal for comparing classifiers or tuning thresholds

---
### Visualizing Model Confidence with Disc Plot

After fitting your logistic model, you can plot the distribution of predicted probabilities for each true class.  
This helps diagnose **model certainty** and **threshold optimization** opportunities.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Predicted probability for positive class
proba = clf.predict_proba(X_test)[:, 1]
```
```python

# Disc plot
sns.histplot(proba, bins=30, kde=True, hue=y_test, stat='density', common_norm=False)
plt.axvline(x=0.5, color='red', linestyle='--', label='Default Threshold 0.5')
plt.xlabel('Predicted Probability of Class 1')
plt.title('Disc Plot of Predicted Probabilities')
plt.legend()
plt.show()
```

### **🧠 How to Interpret:**

| **Region**         | **Meaning**                                         |
| ------------------ | --------------------------------------------------- |
| Left of threshold  | Model predicts negative class (0)                   |
| Right of threshold | Model predicts positive class (1)                   |
| Overlap of classes | ⚠️ Model uncertainty — potential misclassifications |

- **Sharp separation**: High model confidence
    
- **Heavy overlap**: Possible threshold adjustment needed
    
### **🎯 When to Use:**

- Evaluate **how confident** your model is.
    
- Decide whether to **raise/lower threshold** based on business priorities (e.g., fraud detection, medical diagnosis).
___
## 🧪 6. Assumptions & Diagnostics

| Check                     | Tool                        | Insight                         |
|---------------------------|-----------------------------|----------------------------------|
| Linearity of logit        | Binned log-odds plot        | Transformation needed?          |
| Multicollinearity         | Heatmap + VIF               | Drop or combine predictors       |
| Influential observations  | Cook’s Distance             | Check outliers                   |
| Goodness of fit           | Pseudo R² / AIC             | Compare to null model            |
| Classification accuracy   | Confusion matrix, ROC       | Evaluate predictive performance  |

---
## 🧠 7. Probability Thresholding & Predictive Strategy

### Adjusting the Classification Threshold
```python
y_pred_custom = (clf.predict_proba(X_test)[:, 1] > 0.6).astype(int)
```
- Customize threshold based on domain (e.g., 0.6 instead of 0.5)
- Useful in imbalanced classes or risk-sensitive decisions

### Visualizing Precision-Recall Tradeoff
```python
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(y_test, y_proba[:, 1])
plt.plot(thresholds, precision[:-1], label='Precision')
plt.plot(thresholds, recall[:-1], label='Recall')
plt.legend()
```
___
## ✅ Summary

- Start with EDA: class balance, feature relationships
- Confirm assumptions: multicollinearity, logit linearity
- Fit logistic model with `Logit()` or `LogisticRegression()`
- Interpret coefficients using odds ratios
- Evaluate with confusion matrix, ROC, classification report
- Adjust thresholds to meet precision/recall needs


___

### 🔗 **Related Notes**

- [[Links]]