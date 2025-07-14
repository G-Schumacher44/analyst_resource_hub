___
🎯 Purpose

This QuickRef explains how to use **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** — an unsupervised algorithm that groups data based on point density.

---

## 📦 1. When to Use

| Condition                                  | Use DBSCAN?                 |
| ------------------------------------------ | --------------------------- |
| Clusters are non-spherical or uneven sizes | ✅ Yes                       |
| You want to find arbitrary-shaped clusters | ✅ Yes                       |
| You want to detect noise/outliers          | ✅ Yes                       |
| Dataset is large and high-dimensional      | ❌ Can be slow (use HDBSCAN) |

---

## 🧮 2. Core Logic

* Groups together points that are closely packed
* Labels points in low-density regions as outliers
* Requires no predefined number of clusters

---

## 🛠️ 3. Fitting in sklearn

```python
from sklearn.cluster import DBSCAN
model = DBSCAN(eps=0.5, min_samples=5)
model.fit(X)
labels = model.labels_  # -1 = noise points
```

✔️ Scale features before use (`StandardScaler` or `MinMaxScaler`)

---

## 🔧 4. Key Hyperparameters

| Param         | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `eps`         | Max distance for neighbors to be considered part of the same cluster |
| `min_samples` | Min number of neighbors required to form a dense region              |
| `metric`      | Distance function (default = Euclidean)                              |

---

## 📊 5. Evaluating Clusters

| Metric                                | Use When...                              |
| ------------------------------------- | ---------------------------------------- |
| Silhouette Score                      | Works if labels are ≥ 2 clusters         |
| Number of Noise Points (`label = -1`) | Helps assess purity vs over-segmentation |
| Visual Inspection                     | PCA, t-SNE, UMAP visual validation       |

---

## ⚠️ 6. Limitations

* Can be sensitive to `eps` selection
* Performance drops in high dimensions
* May fail if density varies too much between clusters

---

## ✅ Checklist

* [ ] Features scaled to uniform range
* [ ] `eps` and `min_samples` tuned or estimated with k-distance plot
* [ ] Outliers reviewed (`label == -1`)
* [ ] Dimensionality reduction used for visualization if needed
* [ ] Cluster evaluation interpreted contextually (not just scores)

---

## 💡 Tip

> “If KMeans needs structure, DBSCAN thrives in chaos — and outliers are part of the story.”
