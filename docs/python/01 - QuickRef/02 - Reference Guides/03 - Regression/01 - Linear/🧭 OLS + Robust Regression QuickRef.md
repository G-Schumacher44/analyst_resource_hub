___
## 🎯 Purpose

This QuickRef consolidates EDA prep, model fitting, diagnostics, and decision rules for using Ordinary Least Squares (OLS) and Robust Linear Regression. Designed for modelers who need a single, notebook-friendly reference.

---

## 📦 1. EDA Prep for Linear Regression**

|**Step**|**Code**|
|---|---|
|Check distributions|df.hist() or sns.histplot()|
|Skew/kurtosis|df.skew(), df.kurtosis()|
|Correlation heatmap|sns.heatmap(df.corr())|
|VIF check|variance_inflation_factor(X.values, i)|

✔️ Flag skewed variables for log/sqrt transform

✔️ Remove or combine highly correlated variables (VIF > 5–10)

---

## 🔧 2. Feature Transformation Triggers**

|**Condition**|**Suggestion**|
|---|---|
|Skew > 1 or < -1|Try log or Yeo-Johnson|
|Correlation > 0.85|Drop one or use PCA/interactions|
|Heteroskedasticity (BP test fail)|Consider log transform or robust fit|

---

## 📐 3. Model Assumptions (OLS)**

|**Assumption**|**Diagnostic**|
|---|---|
|Linearity|Residuals vs Fitted plot|
|Normality|Histogram / QQ plot of residuals|
|No multicollinearity|VIF < 5–10|
|Homoscedasticity|Breusch-Pagan, White’s test|
|No influential outliers|Cook’s D, leverage plot|

```
# Breusch-Pagan test
from statsmodels.stats.diagnostic import het_breuschpagan
het_breuschpagan(residuals, model.model.exog)
```

---

## ⚖️ 4. When to Use Robust Regression**

|**Problem**|**Use Robust If…**|
|---|---|
|Heteroskedasticity persists|Use HC0–HC3 covariance correction|
|High-leverage points|Use RLM (M-estimators)|
|Many small violations of OLS|Consider robust SE before switching model|

```
# Robust SE example
model.get_robustcov_results(cov_type='HC3')

# Robust Regression
import statsmodels.api as sm
sm.RLM(y, X).fit()
```

---

## 📊 5. Output Interpretation (OLS & Robust)**

|**Coefficient**|**Interpretation**|
|---|---|
|Positive β|1-unit ↑ in X → β unit ↑ in Y (holding others fixed)|
|Negative β|1-unit ↑ in X → β unit ↓ in Y|
|p < 0.05|Statistically significant predictor|
|Adj. R²|Better for comparing models with different # predictors|

✔️ Robust regression affects SE and t-stats — not coefficients

---

## ✅ Final Model Checklist**

• Residuals reviewed (linearity + normality)

• VIF < 10 for all features

• Heteroskedasticity test passed OR robust SE used

• Outliers flagged, Cook’s D < 1

• Model fit (Adj. R², F-stat) interpreted in context

---

**💡 Tip**

  

> “OLS tells you what’s ideal — robust tells you what survives reality.”