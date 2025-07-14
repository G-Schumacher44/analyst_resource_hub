## 🌟 Purpose

This guidebook documents practical machine learning strategies for classification tasks. It complements the EDA Guidebook series and supports modeling decisions, diagnostics, and deployment-readiness in your Analyst Toolkit Vault.

---

## 📆 1. Classifier Overview

| Model               | Use Case                           | Notes                                   |
| ------------------- | ---------------------------------- | --------------------------------------- |
| Logistic Regression | Baseline binary classification     | Interpretable, fast, good for audit     |
| Naive Bayes         | Text, categorical-rich datasets    | Assumes conditional independence        |
| K-Nearest Neighbors | Small datasets, intuitive clusters | Not scalable, sensitive to scaling      |
| Decision Tree       | Explainable rules                  | Prone to overfitting                    |
| Random Forest       | Robust baseline                    | Better generalization, less explainable |
| Gradient Boosting   | Tabular SOTA                       | Powerful, less interpretable            |
| SVM                 | High-dim linear separation         | Harder to scale or tune                 |
| Neural Networks     | Complex, large-scale patterns      | Requires more data, tuning, and infra   |

---

## 🔍 2. Model Fit & Evaluation Metrics

### Standard Metrics

* Accuracy
* Precision / Recall
* F1 Score
* ROC-AUC
* Log-Loss
* Confusion Matrix

### Metric Guidelines

| Metric    | Best for                            |
| --------- | ----------------------------------- |
| Precision | Avoiding false positives            |
| Recall    | Avoiding false negatives            |
| F1 Score  | Balancing precision and recall      |
| ROC-AUC   | Ranking power of predictions        |
| Log-Loss  | Accuracy of predicted probabilities |

---

## 📊 3. Classifier Breakdowns

### 🔷 Logistic Regression

* Assumes linear relationship between predictors and log-odds
* Uses sigmoid function to map values to probabilities

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)
```

**Key Strengths:**

* Interpretable coefficients (odds ratios)
* Fast and stable for binary classification

**Watch for:**

* Multicollinearity (use VIF)
* Assumes linearity in log-odds
* Doesn’t handle non-linearity well

**Best for:**

* Risk scoring, churn prediction, interpretable pipelines

---

### 🔷 Naive Bayes Classifier

#### Types of Naive Bayes

* **GaussianNB** – continuous features (assumes normality)
* **MultinomialNB** – count data (e.g., word counts)
* **BernoulliNB** – binary features (e.g., yes/no, present/absent)

```python
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)
```

**Assumptions:**

* Features are conditionally independent
* Each feature follows a known distribution

**Best for:**

* Text classification (spam, sentiment)
* Categorical/tabular data with low correlation

**Cautions:**

* Doesn’t model feature interaction
* Overconfident if assumptions are violated

---

### 🔷 K-Nearest Neighbors (KNN)

* Distance-based voting classifier
* No training phase — all work done during prediction

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

**Best for:**

* Clean, small datasets
* Non-linear boundaries

**Needs:**

* Scaled features (Euclidean distance)
* Sensitivity to irrelevant features

---

### 🔷 Decision Trees

* Rule-based model that recursively splits data

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)
```

**Strengths:**

* Fully interpretable
* Handles categorical and numeric data

**Watch for:**

* Overfitting on small datasets
* Poor generalization without pruning

---

### 🔷 Random Forest

* Ensemble of decision trees (bagging)

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

**Strengths:**

* Better generalization than single tree
* Handles missing data well

**Drawbacks:**

* Slower than logistic or NB
* Less interpretable (needs feature importance plots)

---

### 🔷 Gradient Boosting (XGBoost, LightGBM)

* Builds trees sequentially, optimizing for error

```python
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train, y_train)
```

**Pros:**

* High accuracy
* Works well with numeric + categorical data

**Cons:**

* Less interpretable
* Can overfit if not tuned

---

### 🔷 Support Vector Machine (SVM)

```python
from sklearn.svm import SVC
model = SVC(probability=True)
model.fit(X_train, y_train)
```

**Notes:**

* Works well in high-dim spaces
* Needs scaling
* Doesn’t scale well with large data

---

### 🔷 Neural Networks (MLPClassifier)

```python
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
model.fit(X_train, y_train)
```

**Best for:**

* Complex patterns, nonlinear data
* Requires large dataset + tuning

**Not ideal for:**

* Interpretability
* Small tabular datasets

---

## 🔢 4. Visual & Diagnostic Tools

| Tool                   | Purpose                                        | Notes                              |
| ---------------------- | ---------------------------------------------- | ---------------------------------- |
| ROC Curve              | Rank-based performance (y\_proba)              | Best for binary classifiers        |
| Confusion Matrix       | Classification accuracy by class               | Text or heatmap format             |
| Precision/Recall Curve | Performance under imbalance                    | Complements ROC in skewed datasets |
| Calibration Plot       | How well predicted probabilities match reality | Good for risk modeling             |
| Log-Loss Distribution  | Understanding prediction confidence            | Lower is better                    |
| SHAP / Feature Import  | Interpretability for black-box models          | Best for tree-based models         |

---

## 🛠️ 5. Preprocessing Needs by Model

| Model             | Needs Scaling? | Handles Categorical?        | Notes                                   |
| ----------------- | -------------- | --------------------------- | --------------------------------------- |
| Logistic          | Yes            | No                          | Use encoding                            |
| Naive Bayes       | Sometimes      | Yes (Multinomial/Bernoulli) | GaussianNB requires scaling             |
| KNN               | Yes            | No                          | Highly sensitive to feature scale       |
| Decision Tree     | No             | Yes                         | Native handling of categoricals         |
| Random Forest     | No             | Yes                         | Encoding optional for sklearn trees     |
| Gradient Boosting | No             | Yes                         | Encode ordinal/categorical thoughtfully |
| SVM               | Yes            | No                          | Requires numeric, scaled input          |
| Neural Net (MLP)  | Yes            | No                          | Standardize inputs for stability        |

---

## 🏃‍♂️ Next Steps

* [ ] Add classifier-specific runner functions (logistic, NB, tree, etc.)
* [ ] Add diagnostic quickrefs per model (conf matrix, AUC, etc.)
* [ ] Add SHAP + interpretability demos for tree models
* [ ] Add flowcharts for choosing a classifier
