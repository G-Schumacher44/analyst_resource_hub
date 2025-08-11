___
## 🎯 Purpose

This QuickRef outlines how to use **Decision Tree Classifiers** for supervised classification tasks. It covers fit logic, splitting rules, hyperparameters, and interpretation essentials.

---

## 📦 1. When to Use

| Condition                      | Use DT Classifier?               |
| ------------------------------ | -------------------------------- |
| You need interpretable splits  | ✅ Yes                            |
| Non-linear relationships exist | ✅ Yes                            |
| Mixed data types (cat + num)   | ✅ Yes                            |
| Small data with fast results   | ✅ Yes                            |
| You need top-tier performance  | ❌ Consider ensemble (RF/XGBoost) |

---

## 🌳 2. Core Logic

* Recursively splits data to minimize **impurity** in child nodes
* Each leaf = class prediction

### 🔍 Splitting Criteria

| Criterion      | Meaning                |
| -------------- | ---------------------- |
| Gini (default) | Measures node impurity |
| Entropy        | Information gain       |

---

## 🛠️ 3. Fitting in sklearn

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth=3)
model.fit(X_train, y_train)
```

```python
# Visualization (simple trees)
from sklearn.tree import plot_tree
plot_tree(model, feature_names=X.columns)
```

---

## 🧪 4. Key Hyperparameters

| Param               | Description                              |
| ------------------- | ---------------------------------------- |
| `max_depth`         | Limits tree depth (reduces overfitting)  |
| `min_samples_split` | Min samples required to split a node     |
| `min_samples_leaf`  | Min samples in a leaf node               |
| `max_features`      | Limits features considered at each split |

---

## 📊 5. Evaluation

| Metric           | Use When...                                 |
| ---------------- | ------------------------------------------- |
| Accuracy         | Balanced classes                            |
| Precision/Recall | Imbalanced classes                          |
| AUC/ROC          | Probabilistic ranking (via `predict_proba`) |

✔️ Use cross-validation or pruning to reduce overfitting

---

## ✅ Checklist

* [ ] Split criterion chosen (gini or entropy)
* [ ] Tree depth and node size parameters tuned
* [ ] Class imbalance reviewed (consider weighted class option)
* [ ] Visual interpretation exported (tree plot)
* [ ] Overfitting controlled via early stopping or pruning

---

## 💡 Tip

> “Decision Trees let you explain your predictions — one split at a time.”
