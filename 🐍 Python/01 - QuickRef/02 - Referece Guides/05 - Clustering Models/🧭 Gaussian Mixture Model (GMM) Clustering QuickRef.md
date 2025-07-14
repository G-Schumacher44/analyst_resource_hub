___
🎯 Purpose

This QuickRef explains how to use **Gaussian Mixture Models (GMMs)** for soft, probabilistic clustering based on a mixture of Gaussian distributions.

---

## 📦 1. When to Use

| Condition                                         | Use GMM?                |
| ------------------------------------------------- | ----------------------- |
| You want probabilistic (soft) cluster assignments | ✅ Yes                   |
| Data clusters have elliptical shape               | ✅ Yes                   |
| You assume underlying normal distributions        | ✅ Yes                   |
| Clusters are non-Gaussian or arbitrary shape      | ❌ Use DBSCAN or HDBSCAN |

---

## 🧮 2. Core Logic

* Models data as a mixture of `k` multivariate Gaussian distributions
* Uses **Expectation-Maximization (EM)** to estimate parameters
* Returns **probability of membership** in each cluster

---

## 🛠️ 3. Fitting in sklearn

```python
from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components=3, covariance_type='full')
model.fit(X)
labels = model.predict(X)
probs = model.predict_proba(X)
```

✔️ Standardize features before fitting

---

## 🔧 4. Key Parameters

| Param             | Description                                 |
| ----------------- | ------------------------------------------- |
| `n_components`    | Number of clusters (mixture components)     |
| `covariance_type` | `'full'`, `'tied'`, `'diag'`, `'spherical'` |
| `init_params`     | `'kmeans'` or `'random'` initialization     |
| `random_state`    | For reproducibility                         |

---

## 📊 5. Evaluation & Selection

| Tool                            | Purpose                            |
| ------------------------------- | ---------------------------------- |
| AIC / BIC                       | Choose optimal `n_components`      |
| Visualize ellipses in PCA space | Validate cluster shape assumptions |
| Check `predict_proba()` spread  | Look for uncertain memberships     |

---

## ⚠️ 6. Limitations

* Assumes Gaussian-shaped clusters
* Sensitive to outliers and initialization
* Not ideal for high-dimensional or non-convex data

---

## ✅ Checklist

* [ ] Features standardized
* [ ] `n_components` selected using AIC/BIC
* [ ] Soft cluster probabilities reviewed
* [ ] Visual validation using PCA or 2D plots
* [ ] Cluster assumptions (elliptical, Gaussian) reviewed

---

## 💡 Tip

> “GMM is where statistics meets clustering — it gives you clusters, but also how confident it is about them.”
