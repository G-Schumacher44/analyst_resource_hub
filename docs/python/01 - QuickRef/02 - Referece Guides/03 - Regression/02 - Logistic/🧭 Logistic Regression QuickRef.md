 🎯 Purpose

This QuickRef guides you through EDA prep, fitting, diagnostics, and interpretation for binary logistic regression. Designed for notebook use, it merges statistical intuition with model-readiness.

---

## 📦 1. EDA Prep for Logistic Regression

| Check                   | Code                                        |
| ----------------------- | ------------------------------------------- |
| Target balance          | `df['target'].value_counts(normalize=True)` |
| Class imbalance warning | >80% in one class → stratify or use SMOTE   |
| Correlation matrix      | `sns.heatmap(df.corr())`                    |
| VIF check               | `variance_inflation_factor(X.values, i)`    |
| Feature skew            | `df.skew()` or histograms                   |

✔️ Ensure target is binary (0/1 or Yes/No encoded)
✔️ Drop or flag highly imbalanced fields

---

## 🔄 2. Logit Linearity & Transform Triggers

| Problem               | Action                                |
| --------------------- | ------------------------------------- |
| X vs logit not linear | Use log/sqrt transform or binning     |
| Predictor skewed      | Consider log or Yeo-Johnson transform |
| Interaction suspected | Add interaction term (X1 \* X2)       |

```python
# Visual: Box-Tidwell or residual plots
sns.regplot(x='X', y=np.log(p / (1 - p)))
```

---

## 🔍 3. Model Fitting (statsmodels or sklearn)

```python
# statsmodels
import statsmodels.api as sm
model = sm.Logit(y, sm.add_constant(X)).fit()
model.summary()

# sklearn
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(X_train, y_train)
```

✔️ Use `C=1/lambda` for sklearn regularization tuning

---

## 📐 4. Output Interpretation

| Metric     | Interpretation                                 |
| ---------- | ---------------------------------------------- |
| Coef > 0   | Predictor ↑ → higher odds of event             |
| Coef < 0   | Predictor ↑ → lower odds of event              |
| p < 0.05   | Statistically significant effect               |
| Odds Ratio | `np.exp(coef)` = multiplicative change in odds |

```python
# Odds ratio calculation
np.exp(model.params)
```

---

## 📊 5. Model Evaluation

| Metric    | Use When...                                   |
| --------- | --------------------------------------------- |
| Accuracy  | Balanced classes and cost-insensitive task    |
| Precision | False positives are costly                    |
| Recall    | False negatives are costly                    |
| AUC/ROC   | General ranking ability (probabilistic power) |

```python
from sklearn.metrics import roc_auc_score, confusion_matrix, classification_report
```

✔️ Use threshold tuning (`predict_proba() > t`) when needed

---

## ✅ Logistic Modeling Checklist

* [ ] Target class checked for balance
* [ ] Predictors tested for logit linearity
* [ ] Model fit using proper library (statsmodels/sklearn)
* [ ] Coefficients interpreted and odds calculated
* [ ] Evaluation metric selected based on real-world cost

---

## 💡 Tip

> “Logistic regression doesn’t just predict events — it explains the odds of them.”
