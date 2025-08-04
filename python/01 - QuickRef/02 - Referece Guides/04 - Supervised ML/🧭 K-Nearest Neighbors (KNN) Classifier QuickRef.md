___
## 🎯 Purpose

This QuickRef explains how to use the **K-Nearest Neighbors (KNN)** algorithm for classification tasks. It covers fit logic, distance metrics, scaling importance, and evaluation strategies.

---

## 📦 1. When to Use

| Condition                                 | Use KNN?                          |
| ----------------------------------------- | --------------------------------- |
| Small to medium dataset                   | ✅ Yes                             |
| Predictors are numeric + scale-consistent | ✅ Yes                             |
| Need interpretable local decisions        | ✅ Yes                             |
| High dimensional or noisy data            | ❌ Try trees or regularized models |

---

## 🧮 2. Core Logic

* KNN is a **lazy learner** — it stores training data and makes predictions **at inference time** based on proximity
* Uses majority vote among k closest training points to assign class

---

## 📏 3. Distance Metrics

| Metric              | Use When...                         |
| ------------------- | ----------------------------------- |
| Euclidean (default) | Standard numeric data               |
| Manhattan           | Grid-like or sparse data            |
| Minkowski           | Generalized form (power = 1 or 2)   |
| Cosine              | Text embeddings, angular similarity |

✔️ Always **scale features** before fitting to avoid distance bias

---

## 🛠️ 4. Fitting in sklearn

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
model.fit(X_train, y_train)
```

---

## 🔧 5. Key Hyperparameters

| Param         | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| `n_neighbors` | Number of nearest neighbors to use                                  |
| `weights`     | `'uniform'` (default) or `'distance'` (closer neighbors weigh more) |
| `metric`      | Distance function (Euclidean, Manhattan, etc.)                      |

---

## 📊 6. Evaluation Tips

* Use cross-validation to tune `k`
* Use confusion matrix, precision/recall, AUC if needed
* Sensitive to **class imbalance** → consider stratified sampling

---

## ✅ Modeling Checklist

* [ ] Features scaled before training (e.g., `StandardScaler`)
* [ ] `n_neighbors` tuned with validation set or CV
* [ ] Distance metric chosen based on feature type
* [ ] Class imbalance reviewed
* [ ] Evaluation scores visualized with multiple `k` values

---

## 💡 Tip

> “KNN makes no assumptions — but gives no explanations either.”
