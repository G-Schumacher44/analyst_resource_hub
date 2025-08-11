## 🎯 Purpose

This checklist provides a visual workflow for the exploratory data analysis (EDA) phase of a linear regression project. Each step uses a plot to check a key assumption or relationship.

---

## Step 1: Target Variable Distribution
- [ ] Histogram + KDE
- [ ] Skewness / Kurtosis calculation

## Step 2: Baseline OLS Modeling
- [ ] Fit model and assess residual plots
- [ ] QQ plot for normality
- [ ] Residuals vs Fitted

## Step 3: Model Integrity Checks
- [ ] VIF for multicollinearity
- [ ] Influence plot / Cook’s Distance
- [ ] Boxplot of residuals by group

## Step 4: Model Extensions
- [ ] Polynomial fit comparison
- [ ] Try RLM (Robust Linear Model)
- [ ] Apply Ridge / Lasso / Elastic Net

## Step 5: Model Selection
- [ ] Plot RMSE vs alpha or complexity
- [ ] AIC/BIC curve
- [ ] Residual comparison (train/test)

## Step 6: Final Summary & Visual Audit
- [ ] Screenshot diagnostic visuals

---

## 🧠 Final Tip

> "Visual EDA for regression is about finding the story in the scatter plots. Look for trends, curves, and clumps before you ever fit a line."