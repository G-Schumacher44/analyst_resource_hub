___
## 🎯 Purpose

This QuickRef explains how to use **KMeans Clustering** — a foundational unsupervised learning algorithm that groups data into `k` clusters based on similarity.

---

## 📦 1. When to Use

| Condition                              | Use KMeans?             |
| -------------------------------------- | ----------------------- |
| You want to segment data by similarity | ✅ Yes                   |
| Clusters are spherical, evenly sized   | ✅ Yes                   |
| Features are numeric and scaled        | ✅ Yes                   |
| Irregularly shaped clusters exist      | ❌ Use DBSCAN or HDBSCAN |

---

## 🧮 2. Core Logic

* Randomly initializes `k` centroids
* Iteratively assigns points to closest centroid
* Updates centroids until convergence
* Minimizes **within-cluster sum of squares (WCSS)**

---

## 🛠️ 3. Fitting in sklearn

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)
labels = model.labels_
centroids = model.cluster_centers_
```

✔️ Always scale data before fitting (`StandardScaler` or `MinMaxScaler`)

---

## 🔧 4. Key Hyperparameters

| Param        | Description                                        |
| ------------ | -------------------------------------------------- |
| `n_clusters` | Number of clusters (k)                             |
| `init`       | Initialization method (`'k-means++'` recommended)  |
| `n_init`     | Number of runs to choose best model (default = 10) |
| `max_iter`   | Max number of iterations (default = 300)           |

---

## 📊 5. Evaluating Clusters

| Metric           | Use When...                                           |
| ---------------- | ----------------------------------------------------- |
| Elbow Method     | Plot inertia vs k to find optimal point               |
| Silhouette Score | Measures cohesion + separation (closer to 1 = better) |
| Davies-Bouldin   | Lower = better clustering separation                  |

```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X, model.labels_)
```

---

## ⚠️ 6. Limitations

* Assumes **spherical clusters** of equal variance
* Sensitive to **initialization and outliers**
* Requires **predefined k** (not data-driven)

---

## ✅ Checklist

* [ ] Data scaled appropriately
* [ ] `k` chosen via Elbow or Silhouette method
* [ ] Initialization method set to `k-means++`
* [ ] Labels interpreted and assigned post-fit
* [ ] Visualizations used to confirm structure (e.g. PCA plot)

---

## 💡 Tip

> “KMeans is simple, scalable, and fast — but it’s only as smart as your choice of k.”
