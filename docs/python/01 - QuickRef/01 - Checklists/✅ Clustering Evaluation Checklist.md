___
 🎯 Purpose

This checklist helps analysts systematically evaluate clustering models. It includes practical considerations for data prep, model tuning, validation, and interpretability. It ensures clusters are meaningful, reproducible, and aligned with project goals.

---

## 🔍 1. Problem Framing

* [ ] What is the **primary goal** of clustering? (e.g., EDA, segmentation, anomaly detection)
* [ ] Are **overlapping** or **clearly separated** clusters expected?
* [ ] Is **domain knowledge** available to validate or name clusters?
* [ ] Are there **latent groups** or labels that may be compared post hoc?

---

## ⚙️ 2. Preprocessing

* [ ] Features are **numerical or properly encoded**
* [ ] **Scaling** applied to distance-based models (KMeans, DBSCAN, GMM)
* [ ] Dimensionality reduction (e.g., PCA, UMAP) considered for speed or interpretability
* [ ] **Outliers** reviewed or removed before fitting

---

## 🧪 3. Internal Validation

* [ ] Silhouette score computed and interpreted
* [ ] Calinski-Harabasz and/or Davies-Bouldin Index reviewed
* [ ] Cluster size distribution checked for imbalance or singletons
* [ ] Elbow or gap statistic used to select number of clusters (for KMeans, GMM, etc.)

---

## 📊 4. Visual Diagnostics

* [ ] PCA / UMAP / t-SNE plots checked for cluster separation
* [ ] Silhouette plots visualized
* [ ] Heatmap or radar plot used to compare cluster means/centroids
* [ ] Bar plot created for size distribution of clusters

---

## 🧰 5. Model-Specific Checks

* [ ] **K-Means**: spherical assumption checked, sensitivity to k tested
* [ ] **DBSCAN/HDBSCAN**: eps and min\_samples tuned, noise behavior reviewed
* [ ] **GMM**: covariance type validated, soft probabilities understood
* [ ] **Hierarchical**: dendrogram examined, cluster cut-off selected

---

## 🔁 6. Stability & Reproducibility

* [ ] Random seeds fixed (when supported)
* [ ] Clustering rerun and results compared (Adjusted Rand Index or consistency checks)
* [ ] Centroids / medoids / cluster centers saved
 * [ ] **Subsample Stability:** Re-run on a data subset to check if cluster structure holds.
* [ ] Label encoding scheme documented if reused downstream

---

## 🧾 7. External Validation (Optional)

* [ ] Ground truth labels (if any) compared using:

  * Adjusted Rand Index
  * Mutual Information Score
  * Homogeneity & Completeness
  * Fowlkes-Mallows Score
* [ ] Confusion matrix or label-overlay plots created

---

## 🧠 8. Interpretability & Communication

* [ ] Cluster profiles summarized with descriptive stats or visualizations
* [ ] Most influential features per cluster identified
* [ ] Cluster labels/descriptions drafted for stakeholders
* [ ] Visuals saved or exported for reporting (PDF, slides, dashboards)

---

!!! tip "Final Tip"

    “Clustering is a lens, not a labeler. Use it to reveal structure, not assert truth.”

Use this checklist in tandem with the Clustering Visual Guide and Decision Card for optimal analysis and communication.
