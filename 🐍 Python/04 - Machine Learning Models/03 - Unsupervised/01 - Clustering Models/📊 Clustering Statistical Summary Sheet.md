___
🎯 Purpose

This reference provides statistical tools and interpretation guidelines to evaluate clustering models using both internal metrics and descriptive summaries. It supports unsupervised model inspection, profiling, and stakeholder-ready reporting.

---

## 📐 1. Internal Validation Metrics (No Ground Truth Needed)

### ✅ Silhouette Score

Measures cohesion vs separation:

* Closer to 1 = better-defined clusters
* 0 = overlapping boundaries
* < 0 = misassignment

```python
from sklearn.metrics import silhouette_score
silhouette_score(X_scaled, cluster_labels)
```

---

### ✅ Calinski-Harabasz Index

Ratio of between-cluster to within-cluster dispersion:

* Higher is better

```python
from sklearn.metrics import calinski_harabasz_score
calinski_harabasz_score(X_scaled, cluster_labels)
```

---

### ✅ Davies-Bouldin Index

Average similarity between clusters:

* Lower is better

```python
from sklearn.metrics import davies_bouldin_score
davies_bouldin_score(X_scaled, cluster_labels)
```

---

### ✅ Within-Cluster Sum of Squares (WCSS)

Used for elbow method in KMeans.

```python
inertia = model.inertia_  # For KMeans
```

---

### ✅ Average Distance to Centroid

Custom distance-based dispersion metric.

```python
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min
_, dists = pairwise_distances_argmin_min(model.cluster_centers_, X_scaled)
dists.mean()
```

---

## 📊 2. Descriptive Cluster Statistics (Per Group)

Summarize cluster structure using standard statistics.

```python
import pandas as pd
X['cluster'] = cluster_labels
X.groupby('cluster').agg(['mean', 'std', 'median', 'min', 'max'])
```

| Metric     | Purpose                   |
| ---------- | ------------------------- |
| Mean / Std | Centrality and spread     |
| Min / Max  | Range analysis            |
| Count      | Cluster size distribution |
| Median     | Robust central tendency   |

---

## 📋 3. Suggested Summary Table Columns

* Cluster label
* Sample count
* Top 3 distinguishing features (Z-score or absolute mean diff)
* Feature summaries (mean, std)

---

## 🔁 4. Reproducibility & Delta Tracking

* Save centroids or medoids for future comparisons
* Compare distributions over time or version
* Track silhouette or CH index over re-runs

```python
np.save('cluster_centroids_v1.npy', model.cluster_centers_)
```

---

## 🧪 5. Bonus: Cluster Quality Tiers (Silhouette Guidelines)

| Score Range | Interpretation              |
| ----------- | --------------------------- |
| 0.70–1.00   | Strong structure            |
| 0.50–0.70   | Reasonable structure        |
| 0.25–0.50   | Weak structure              |
| < 0.25      | Overlapping or noise-driven |

---

## 📦 Reporting Tip

> Pair statistical summaries with **visual diagnostics** (UMAP, silhouette plots, radar charts) for maximum interpretability.

Use this with: Clustering Visual Guide, Checklist, and Decision Card.
