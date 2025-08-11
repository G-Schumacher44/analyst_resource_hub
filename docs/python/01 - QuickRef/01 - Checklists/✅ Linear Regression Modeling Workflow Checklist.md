## 🎯 Purpose

This checklist outlines the core workflow for building and evaluating a linear regression model. It covers pre-modeling checks, model fitting, evaluation, and common extensions.

---

## 🔍 Before Modeling
- [ ] Histogram + skew/kurtosis of outcome
- [ ] Scatterplots for linearity
- [ ] Checked collinearity (heatmap + VIF)
- [ ] Outlier/influence points assessed
- [ ] Features are scaled (especially for regularized models like Ridge/Lasso).

## 🏗️ Build Model
- [ ] Fitted OLS with `statsmodels` or `sklearn`
- [ ] Examined residual plots (QQ, histogram, fitted vs residuals)
- [ ] Added polynomial or interaction terms if needed

## 🧪 Evaluate & Diagnose
- [ ] AIC/BIC for model selection
- [ ] Train/test RMSE comparison
- [ ] **Normality of Residuals:** Checked with QQ plot or Shapiro-Wilk test.
- [ ] **Homoscedasticity:** Checked residuals vs. fitted plot for constant variance (no funnel shape).
- [ ] **Influential Points:** Checked Cook's distance to identify points that disproportionately affect the model.
- [ ] Considered Ridge/Lasso if overfitting/collinearity observed

## 🧰 Extensions
- [ ] Used robust regression if outliers impacted fit
- [ ] Interpreted coefficients and confidence intervals

---

## 🧠 Final Tip

> "A good linear model isn't just about a high R-squared; it's about satisfying the underlying assumptions. Diagnostics are as important as the fit itself."