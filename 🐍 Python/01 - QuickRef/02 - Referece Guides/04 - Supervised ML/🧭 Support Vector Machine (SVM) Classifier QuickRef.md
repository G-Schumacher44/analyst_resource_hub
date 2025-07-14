___
## 🎯 Purpose

This QuickRef outlines how to use **Support Vector Machine (SVM)** classifiers. It covers decision boundaries, kernels, hyperparameters, and practical usage for binary and multiclass classification.

---

## 📦 1. When to Use

| Condition                             | Use SVM?                        |
| ------------------------------------- | ------------------------------- |
| Linear boundary works well            | ✅ Yes (linear SVM)              |
| You need clear margin between classes | ✅ Yes                           |
| Nonlinear boundary needed             | ✅ Yes (use kernels)             |
| Huge dataset or sparse input          | ❌ Can be slow; use SGD or trees |

---

## ✂️ 2. Core Logic

* Finds hyperplane that **maximally separates** classes
* Only **support vectors** (borderline points) influence boundary
* Uses kernel trick to map inputs to higher dimensions

---

## 🛠️ 3. Fitting in sklearn

```python
from sklearn.svm import SVC
model = SVC(kernel='rbf', C=1.0, probability=True)
model.fit(X_train, y_train)
```

✔️ Use `probability=True` for `predict_proba()` (not on by default)

---

## 🔧 4. Key Hyperparameters

| Param         | Description                                                           |
| ------------- | --------------------------------------------------------------------- |
| `C`           | Regularization strength (low = wider margin, more misclassifications) |
| `kernel`      | Mapping function: `'linear'`, `'rbf'`, `'poly'`, `'sigmoid'`          |
| `gamma`       | Controls curvature of decision boundary (higher = more flexible)      |
| `probability` | Enables `predict_proba()` (slower training)                           |

---

## 🌐 5. Common Kernels

| Kernel          | Use When...                             |
| --------------- | --------------------------------------- |
| `linear`        | Data is roughly linearly separable      |
| `rbf` (default) | General-purpose nonlinear mapping       |
| `poly`          | Polynomial relationships exist          |
| `sigmoid`       | Rarely used (like a shallow neural net) |

---

## 📊 6. Evaluation Tips

* Use `accuracy`, `precision`, `recall`, `AUC`
* Use `GridSearchCV` to tune `C` and `gamma`
* Normalize or standardize features before fitting

---

## ✅ Checklist

* [ ] Target is binary or multiclass
* [ ] Feature scaling applied
* [ ] Kernel chosen based on linearity needs
* [ ] `C` and `gamma` tuned via cross-validation
* [ ] If `predict_proba` needed, enable in `SVC`

---

## 💡 Tip

> “Support Vector Machines don’t memorize your data — they focus only on what matters: the boundary.”
