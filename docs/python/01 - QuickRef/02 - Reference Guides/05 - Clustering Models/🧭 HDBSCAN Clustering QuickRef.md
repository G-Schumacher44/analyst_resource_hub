---
## 🎯 Purpose

This QuickRef explains how to use **HDBSCAN** — a powerful clustering algorithm that extends DBSCAN to better handle **variable-density** clusters and large, high-dimensional datasets.

---

## 📦 1. When to Use

| Condition                                      | Use HDBSCAN?           |
| ---------------------------------------------- | ---------------------- |
| You want density-based clustering              | ✅ Yes                  |
| DBSCAN fails due to varying densities          | ✅ Yes                  |
| You want soft clustering (membership strength) | ✅ Yes                  |
| You want speed + scalability                   | ✅ Yes                  |
| Your data is small/simple                      | ❌ Use DBSCAN or KMeans |

---

## 🧮 2. Core Logic

* Builds a hierarchy of density-based clusters
* Condenses it into the most stable clusters
* Assigns **probability of membership** to each point (soft clustering)
* Automatically determines number of clusters (no k needed)

---

## 🛠️ 3. Fitting in Python

```python
import hdbscan
model = hdbscan.HDBSCAN(min_cluster_size=10)
model.fit(X)
labels = model.labels_  # -1 = noise
probs = model.probabilities_  # Soft cluster membership
```

✔️ Requires feature scaling before fitting

---

## 🔧 4. Key Parameters

| Param                      | Description                                   |
| -------------------------- | --------------------------------------------- |
| `min_cluster_size`         | Minimum size for a dense cluster              |
| `min_samples`              | Influences how conservative the clustering is |
| `metric`                   | Distance function (e.g. 'euclidean')          |
| `cluster_selection_method` | `'eom'` (default) or `'leaf'`                 |

---

## 📊 5. Evaluation + Visualization

| Tool                       | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| Soft cluster probabilities | Helps visualize fuzzy memberships        |
| t-SNE / UMAP               | Great for showing density hierarchy      |
| Outlier scores             | Points with low stability can be flagged |

---

## ⚠️ 6. Limitations

* Less intuitive than DBSCAN or KMeans
* Parameter tuning requires exploration
* No native `sklearn` support (third-party package)

---

## ✅ Checklist

* [ ] Data scaled before fitting
* [ ] `min_cluster_size` + `min_samples` tuned
* [ ] Noise points reviewed (`label = -1`)
* [ ] Membership probabilities visualized or used
* [ ] Dimensionality reduction (e.g. UMAP) used to assist interpretation

---

## 💡 Tip

> “HDBSCAN doesn’t ask for `k`. It lets your data tell you where the clusters live — and how sure it is.”
