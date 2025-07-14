#GAD #Coursera #dataAnalytics #regression 
Regression Analysis
**Course:** [[Google Advanced Data Analytics Certificate]]  
**Module:** 4
___

## 🎯 Purpose
This guide outlines visual exploratory data analysis (EDA) techniques to prepare for conducting **ANOVA**, **MANOVA**, **ANCOVA**, and **MANCOVA**. Each method requires evaluating group differences in means, variance, and distributional assumptions.

---

## 🟦 ANOVA (Analysis of Variance)
### ✅ Use Case
Compare the means of a **single continuous dependent variable** across **2 or more categorical groups**.

### 📈 Visual Tools
- **Box Plot**:
  ```python
  sns.boxplot(x="group", y="outcome", data=df)
  ```
  ✔️ Highlights differences in medians and spread

- **Violin Plot**:
  ```python
  sns.violinplot(x="group", y="outcome", data=df)
  ```
  ✔️ Combines KDE with boxplot for richer shape comparison

- **Strip/Swarm Plot**:
  ```python
  sns.stripplot(x="group", y="outcome", data=df, jitter=True)
  ```
  ✔️ Reveals individual observations and clustering

- **Histogram by Group**:
  ```python
  sns.histplot(data=df, x="outcome", hue="group", kde=True, element="step")
  ```
  ✔️ Compares distribution overlap

---

## 🟩 MANOVA (Multivariate ANOVA)
### ✅ Use Case
Compare the means of **2+ continuous dependent variables** across **groups**.

### 📈 Visual Tools
- **Pair Plot by Group**:
  ```python
  sns.pairplot(df, hue="group", vars=["outcome1", "outcome2"])
  ```
  ✔️ Visualize interactions between multiple DVs by group

- **Group Mean Plot (Centroids)**:
  Plot average values for each DV per group using scatter

- **Correlation Heatmap (DVs only)**:
  ```python
  sns.heatmap(df[["outcome1", "outcome2"]].corr(), annot=True)
  ```
  ✔️ Check for collinearity between dependent variables

---

## 🟨 ANCOVA (Analysis of Covariance)
### ✅ Use Case
Compare group means of a continuous DV **while controlling for a continuous covariate**.

### 📈 Visual Tools
- **Scatter Plot with Regression Lines**:
  ```python
  sns.lmplot(x="covariate", y="outcome", hue="group", data=df)
  ```
  ✔️ Show linear trends by group, adjusting for covariate

- **Box Plot + Covariate Distribution**:
  - Plot covariate distribution per group to ensure no confounding imbalance

- **Interaction Plot (optional)**:
  Shows how slope of DV vs covariate changes per group

---

## 🟥 MANCOVA (Multivariate ANCOVA)
### ✅ Use Case
Compare **2+ dependent variables** across **groups**, **controlling for one or more covariates**.

### 📈 Visual Tools
- **Facet Grid Regression**:
  Visualize each DV against covariate, by group

- **Multivariate Scatter or PCA Plot**:
  Reduce DVs to 2D (via PCA) and color by group for pattern detection

- **Partial Residual Plot**:
  Show adjusted effects of group differences post-covariate adjustment

---

## 📌 Summary Table

| Method   | Visual Focus                                    |
|----------|--------------------------------------------------|
| ANOVA    | Box/violin plots, histograms, stripplots         |
| MANOVA   | Pair plots, mean centroids, DV correlation map   |
| ANCOVA   | lmplot (scatter w/ covariate), covariate hist     |
| MANCOVA  | Faceted plots by DV, partial plots, PCA clustering |

---

## ✅ Final Tips
- Always start with **distribution and spread checks**
- Use color to encode group membership
- Ensure covariates are **balanced and linear** across groups (for ANCOVA/MANCOVA)

---


___

### 🔗 **Related Notes**

- [[Links]]