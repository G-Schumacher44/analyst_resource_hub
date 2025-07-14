___
## 🎯 Purpose

This guidebook introduces foundational unsupervised clustering models and their real-world applications. It serves as the entry point to the clustering section of the Analyst Toolkit Vault and is designed for analysts exploring structure in unlabeled data.

---

## 🧠 1. What is Clustering?

Clustering is the process of grouping similar observations together based on feature similarity. It is:

* **Unsupervised**: no labeled target variable
* **Exploratory**: often part of EDA or segmentation
* **Flexible**: used in customer segmentation, anomaly detection, pattern discovery

---

## 📦 2. Common Clustering Algorithms

| Model                   | Best For                           | Notes                                |
| ----------------------- | ---------------------------------- | ------------------------------------ |
| K-Means                 | Well-separated, spherical clusters | Fast, needs `k`, sensitive to scale  |
| Hierarchical Clustering | Small datasets, dendrogram needs   | Good for nested patterns             |
| DBSCAN                  | Arbitrary shape, noise handling    | Density-based, auto-detects clusters |
| Gaussian Mixture (GMM)  | Overlapping clusters               | Probabilistic, soft clustering       |
| HDBSCAN                 | Complex, hierarchical structures   | Robust alternative to DBSCAN         |
| Spectral Clustering     | Graph-based clusters               | Useful for non-convex shapes         |
| K-Medoids               | Robust to outliers                 | Like K-Means but more stable         |

---

## ⚙️ 3. Preprocessing for Clustering

| Step                     | Why It Matters                      |
| ------------------------ | ----------------------------------- |
| Feature Scaling          | K-Means, GMM are distance-based     |
| Dimensionality Reduction | PCA/UMAP for visualization or speed |
| Encoding Categoricals    | Required for mixed-type data        |
| Outlier Removal          | Affects DBSCAN, K-Means boundaries  |

```python
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)
```

---

## 📈 4. K-Means Clustering

### How It Works

* Assigns `k` cluster centroids
* Iteratively minimizes within-cluster variance

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(X_scaled)
labels = model.labels_
```

### Strengths:

* Fast, scalable
* Interpretability of centroids

### Limitations:

* Assumes spherical clusters
* Must choose `k`
* Sensitive to scale & initialization

---

## 🌲 5. Hierarchical Clustering

### How It Works

* Computes all pairwise distances
* Iteratively merges closest clusters (linkage)

```python
from scipy.cluster.hierarchy import linkage, dendrogram
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix)
```

### Use When:

* You need a dendrogram
* Want to explore cluster granularity at multiple levels

---

## 🌊 6. DBSCAN (Density-Based)

### How It Works

* Forms clusters by detecting dense regions
* Labels noise and outliers

```python
from sklearn.cluster import DBSCAN
model = DBSCAN(eps=0.3, min_samples=5)
labels = model.fit_predict(X_scaled)
```

### Strengths:

* Detects arbitrary shapes
* Handles noise automatically

### Limitations:

* Needs parameter tuning (eps, min\_samples)
* Struggles in varying density

---

## 🎲 7. Gaussian Mixture Models (GMM)

### How It Works

* Fits multiple Gaussian distributions
* Each point gets a probability of belonging to each cluster

```python
from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components=3)
labels = model.fit_predict(X_scaled)
```

### Use When:

* You expect soft cluster boundaries
* Data is more overlapping or elliptical

---

## 📊 8. Comparing Cluster Results

| Tool              | Purpose                                  |
| ----------------- | ---------------------------------------- |
| Silhouette Score  | Measures cohesion vs separation          |
| Calinski-Harabasz | Ratio of between/within dispersion       |
| Davies-Bouldin    | Lower = better separation/compact        |
| Visual Inspection | Dimensionality-reduced plots (PCA, UMAP) |

```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X_scaled, labels)
```

---

## 📌 9. Tips for Analysts

* Always scale your data unless using tree-based distances
* Use PCA or UMAP for 2D cluster plotting
* Don’t assume clustering is “correct” — it’s often exploratory
* Validate with multiple metrics AND domain context

---

## 📅 Next Steps

* [ ] Build advanced clustering guide (validation, deep methods)
* [ ] Add visual clustering guide (PCA, UMAP, silhouette visual)
* [ ] Create checklist + decision card for clustering model choice
