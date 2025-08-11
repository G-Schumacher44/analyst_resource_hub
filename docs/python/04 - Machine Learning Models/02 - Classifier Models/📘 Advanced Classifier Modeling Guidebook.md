## 🌟 Purpose

This guidebook expands on the standard ML & Classifier Models Guidebook, focusing on advanced strategies for building, optimizing, and validating classification models within the Analyst Toolkit Vault. It is intended to deepen analyst proficiency and improve decision-making in real-world modeling scenarios.

---

## 📊 1. Model Selection Strategy

### ✅ Core Considerations:

* **Problem framing**: binary, multiclass, multilabel
* **Data size and shape**: small tabular vs large/high-dimensional
* **Model interpretability**: white-box vs black-box preference
* **Computation budget**: lightweight models vs ensemble stacks
* **Downstream usage**: automation, risk scoring, reporting

### 🎯 Flowchart: Choosing a Classifier

* [ ] (Add visual: binary vs multiclass ➔ interpretability needed? ➔ ensemble / kernel / neural?)
* E.g.:

  * Binary, interpretable → Logistic Regression
  * Multiclass, nonlinear, scalable → Gradient Boosting
  * Text data, categorical → Naive Bayes / Random Forest

---

## 📉 2. Handling Class Imbalance

### Techniques:

* **Resampling Methods**:

  * SMOTE / Borderline-SMOTE / ADASYN
  * Random Oversampling / Undersampling
  * SMOTE + Tomek Links (combine oversampling and cleaning)
* **Model-Side Fixes**:

  * Class weights (`class_weight='balanced'`)
  * Custom loss weighting (in neural nets, XGBoost, LightGBM)
  * Adjusting decision thresholds (post-model tuning)

### Diagnostics:

* Precision-Recall Curve (better than ROC in skewed settings)
* PR-AUC vs ROC-AUC
* Confusion matrix heatmap with per-class accuracy
* Sensitivity/specificity matrix for medical/risk contexts

---

## ⚖️ 3. Cross-Validation & Evaluation Strategy

### Common CV Methods:

* **K-Fold CV** (standard): evenly splits data, assumes i.i.d.
* **Stratified K-Fold**: preserves class ratios in classification
* **Repeated Stratified K-Fold**: adds robustness
* **TimeSeriesSplit**: prevents leakage in temporal datasets
* **Leave-One-Out CV (LOOCV)**: high variance, slow but thorough

### Nested CV

Used when both **model tuning** and **model selection** need evaluation.

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
cv = StratifiedKFold(n_splits=5)
scores = cross_val_score(model, X, y, cv=cv, scoring='f1_macro')
```

### Metric Strategy:

Use multiple metrics:

* `accuracy` + `f1_macro` (imbalanced)
* `roc_auc_ovr` for multiclass
* `log_loss` for probability-calibrated models

---

## ⚙️ 4. Hyperparameter Tuning

### Search Tools:

* `GridSearchCV` — exhaustive, slow but thorough
* `RandomizedSearchCV` — efficient sampling, good baseline
* `optuna`, `skopt`, `bayes_opt` — modern Bayesian optimization

### Ensemble-Aware Parameters:

| Model Type        | Important Params                                                              |
| ----------------- | ----------------------------------------------------------------------------- |
| Logistic          | `C`, `penalty`, `solver`                                                      |
| Random Forest     | `max_depth`, `n_estimators`, `min_samples_leaf`                               |
| Gradient Boosting | `learning_rate`, `n_estimators`, `max_depth`, `subsample`, `colsample_bytree` |
| SVM               | `C`, `kernel`, `gamma`, `degree`                                              |
| KNN               | `n_neighbors`, `weights`, `metric`                                            |

### Example:

```python
from sklearn.model_selection import GridSearchCV
params = {'max_depth': [3, 5, 7], 'min_samples_leaf': [1, 5]}
search = GridSearchCV(RandomForestClassifier(), params, cv=5, scoring='f1_macro')
search.fit(X_train, y_train)
```

---

## 🔢 5. Feature Selection & Multicollinearity

### Manual Techniques:

* Correlation heatmaps / pairwise inspection
* Drop high-VIF columns (`VIF > 5` or `VIF > 10`)
* Domain knowledge pruning

### Automated Feature Selection:

* `SelectKBest`, `SelectPercentile`
* `f_classif` (ANOVA F-test), `chi2`, mutual information
* `RFE`, `RFECV` (recursive feature elimination)
* L1-penalized models (Logistic with `penalty='l1'`)

### Sample:

```python
from sklearn.feature_selection import SelectKBest, mutual_info_classif
selector = SelectKBest(mutual_info_classif, k=20)
X_selected = selector.fit_transform(X, y)
```

---

## 👁️ 6. Interpreting Black-Box Classifiers

### SHAP — Shapley Additive Explanations:

* Explains global and local prediction impact
* Works on tree-based models and deep learning via KernelSHAP

```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

### LIME — Local Interpretable Model-agnostic Explanations:

* Explains single predictions by approximating with interpretable surrogate

```python
from lime.lime_tabular import LimeTabularExplainer
explainer = LimeTabularExplainer(X_train.values, feature_names=X.columns)
exp = explainer.explain_instance(X_test.iloc[0].values, model.predict_proba)
exp.show_in_notebook()
```

### Other:

* Permutation importance
* Feature impact over time (model monitoring)

---

## 🏛️ 7. Production Readiness & Risk Control

### Probability Calibration:

Ensure `predict_proba` values are well aligned with reality:

* Platt scaling (fit a logistic model on outputs)
* Isotonic regression (non-parametric)

```python
from sklearn.calibration import CalibratedClassifierCV
calibrated = CalibratedClassifierCV(model, method='isotonic', cv=5)
calibrated.fit(X_train, y_train)
```

### Cutoff Selection:

* Use ROC curve to choose operating point
* Use cost-based matrix to define loss by FP/FN

### Drift Monitoring:

* Track input distribution drift (using PSI or KS test)
* Track model performance decay (ROC, PR, log-loss)
* Store snapshots of data profiles during training

---

## 📚 8. Reference Patterns & Notebook Templates

* Logistic regression grid search + ROC thresholding
* Random Forest with SMOTE + SHAP summary
* Tree boosting pipeline with GridSearchCV + calibration
* KNN with scaling, voting heatmap, PR curve
* Model comparison template: ROC, PR, confusion matrix
* Notebook for SHAP + permutation plots for production audit

---

## 📅 TODO:

* [ ] Add calibration threshold visualizer template
* [ ] Add classification cost matrix integration examples
* [ ] Add fast model audit checklist for field deployment
* [ ] Create flowchart cheat sheet: "Which Classifier Should I Use?"
