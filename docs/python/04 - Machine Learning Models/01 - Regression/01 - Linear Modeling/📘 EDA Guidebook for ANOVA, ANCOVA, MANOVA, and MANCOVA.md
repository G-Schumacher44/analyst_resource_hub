
___
## 🎯 Purpose
This guide outlines how to perform **exploratory data analysis (EDA)** when preparing for statistical models that test group mean differences, including:

- **ANOVA** (single DV, multiple groups)
- **ANCOVA** (DV with covariate adjustment)
- **MANOVA** (multiple DVs across groups)
- **MANCOVA** (multiple DVs with covariates)

It focuses on preparing and understanding the data *before* modeling begins.

---

## 🟦 1. EDA for ANOVA

### 📌 Goal
Explore how a single dependent variable differs across categories.

### 🔍 Key EDA Steps
- Identify the **categorical group variable** (independent variable)
- Explore **distribution of the DV by group**
- Assess **group balance** (sample sizes)

### ✅ EDA Tools
- Descriptive statistics by group (mean, std, count)
- Boxplots or violin plots of DV
- Levene's test for equal variance

### 📊 Python Example
```python
df.groupby('group')['outcome'].describe()
sns.boxplot(x='group', y='outcome', data=df)
```

---

## 🟨 2. EDA for ANCOVA

### 📌 Goal
Explore group differences in DV while adjusting for a **continuous covariate**.

### 🔍 Key EDA Steps
- Confirm the covariate is **linearly related** to the DV
- Assess whether the covariate varies across groups
- Test for **group × covariate interaction** visually and numerically

### ✅ EDA Tools
- Scatterplot of DV vs covariate, color-coded by group
- Correlation matrix or regression line per group
- Group means of the covariate

### 📊 Python Example
```python
sns.lmplot(x='covariate', y='outcome', hue='group', data=df)
df.groupby('group')['covariate'].mean()
```

---

## 🟩 3. EDA for MANOVA

### 📌 Goal
Understand how **multiple dependent variables** vary across groups.

### 🔍 Key EDA Steps
- Check correlation among DVs (they should not be independent)
- Explore DV patterns by group using pairwise plots
- Standardize DVs if they differ in scale

### ✅ EDA Tools
- Pairplot of DVs with group hue
- Correlation matrix of DVs
- Z-scoring if necessary

### 📊 Python Example
```python
sns.pairplot(df, vars=['dv1', 'dv2', 'dv3'], hue='group')
df[['dv1', 'dv2', 'dv3']].corr()
```

---

## 🟥 4. EDA for MANCOVA

### 📌 Goal
Explore multiple DVs across groups, adjusting for one or more covariates.

### 🔍 Key EDA Steps
- Follow MANOVA EDA (correlation, scaling)
- Assess how covariates relate to each DV
- Examine whether covariate distributions are similar across groups

### ✅ EDA Tools
- Scatterplots of each DV vs each covariate by group
- Covariate summary stats by group
- PCA to visually reduce complexity (optional)

### 📊 Python Sketch
```python
for dv in ['dv1', 'dv2']:
    sns.lmplot(x='covariate', y=dv, hue='group', data=df)
```

---

## 📘 Summary Table

| Method   | EDA Focus                             | Tools Used                               |
|----------|----------------------------------------|-------------------------------------------|
| ANOVA    | DV by group (1 DV)                    | Boxplots, descriptive stats, Levene's     |
| ANCOVA   | DV + covariate by group               | lmplot, covariate means by group          |
| MANOVA   | 2+ DVs by group                       | Pairplot, correlation matrix, scaling     |
| MANCOVA  | 2+ DVs + covariates by group          | Scatter matrix, group summaries, PCA      |

---

Let me know if you want to add dataset-ready templates or checklists for running these steps efficiently!

___

### 🔗 **Related Notes**

- [[Links]]