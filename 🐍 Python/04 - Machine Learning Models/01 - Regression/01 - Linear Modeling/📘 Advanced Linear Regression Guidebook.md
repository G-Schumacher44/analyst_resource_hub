___
## 🎯 Purpose

This guidebook expands on the core linear regression modeling guide by detailing advanced techniques, assumptions, diagnostic methods, and specialized modeling extensions. It is intended for analysts building interpretable, assumption-validated, and production-ready linear models.

---

## 🧠 1. Model Fit vs Inference vs Prediction

| Goal        | Focus                              | Tools                               |
| ----------- | ---------------------------------- | ----------------------------------- |
| Explanation | Interpret coefficients             | OLS, WLS, RLM                       |
| Inference   | Validate statistical relationships | P-values, confidence intervals      |
| Prediction  | Minimize test error                | Regularization, CV, transformations |

✔️ Frame model usage before optimization.

---

## 🧮 2. Advanced Assumption Testing

### 🔍 Normality of Residuals

* Shapiro-Wilk, Anderson-Darling, KS Test
* Histogram + QQ plot

### 📉 Homoscedasticity

* Breusch-Pagan, White Test
* Residuals vs Fitted visual

### 🔁 Autocorrelation

* Durbin-Watson, Ljung-Box
* Residual lag plots

### 🔢 Multicollinearity

* VIF (Variance Inflation Factor)
* Correlation heatmap, condition index

### ✅ Python Snippets

```python
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy.stats import shapiro
```

---

## 🛠 3. Robust and Modified Linear Models

| Method             | Use Case                          |
| ------------------ | --------------------------------- |
| RLM (M-estimators) | Outliers distort OLS              |
| WLS                | Non-constant error variance       |
| HC3 Errors         | Heteroskedasticity, small samples |

```python
model = sm.OLS(y, X).fit()
robust_model = model.get_robustcov_results(cov_type='HC3')
```

---

## 🧪 4. Residual Diagnostics

| Diagnostic         | Plot / Test                      | Goal                           |
| ------------------ | -------------------------------- | ------------------------------ |
| Residual Linearity | Residuals vs Fitted              | Flat band, no trend            |
| Normality          | QQ plot, histogram, Shapiro test | Bell shape, diagonal line      |
| Constant Variance  | BP / White, scale-location plot  | Uniform spread                 |
| Autocorrelation    | DW stat, residual autocorr. plot | No serial correlation          |
| Influential Obs.   | Leverage vs residual, Cook's D   | Flag outliers or high leverage |

---

## 🔁 5. Transformations & Nonlinear Patterns

| Transformation | Use Case                              | Visual Test                    |
| -------------- | ------------------------------------- | ------------------------------ |
| Log(y)         | Right-skewed response                 | Histogram, Residuals vs Fitted |
| Log(x)         | Exponential predictor pattern         | X vs Y scatter                 |
| Box-Cox        | Non-normal target, heteroscedasticity | QQ, residual plot              |
| Polynomial     | Curved relationships                  | X vs Residuals, LOESS          |

```python
from sklearn.preprocessing import PolynomialFeatures
```

---

## 🧠 6. Interaction Effects

✔️ Capture variable relationships that **change by group** or depend on other predictors.

```python
smf.ols('y ~ X1 * X2', data=df).fit()
```

### Visuals:

* Simple slopes plot
* Grouped regression lines

---

## 🧩 7. Regularization Extensions

| Method     | Goal                           |
| ---------- | ------------------------------ |
| Ridge      | Shrink correlated coefficients |
| Lasso      | Shrink and select (some to 0)  |
| ElasticNet | Blend Ridge + Lasso            |

```python
from sklearn.linear_model import LassoCV, RidgeCV, ElasticNetCV
```

### Visuals:

* Coefficient paths
* Validation curves (RMSE vs Alpha)

---

## 📊 8. Model Comparison Tools

| Tool             | Purpose                               |
| ---------------- | ------------------------------------- |
| Adjusted R²      | Compare fit with penalty for features |
| AIC/BIC          | Penalized log-likelihood criteria     |
| Cross-Validation | Estimate test error                   |
| RMSE/MAE         | Fit error on holdout/test             |

```python
from sklearn.model_selection import cross_val_score
```

---

## 📋 9. Reporting Template Elements

| Field                   | Description                                 |
| ----------------------- | ------------------------------------------- |
| Model Type              | OLS / Ridge / RLM / Elastic Net             |
| Fit Metrics             | R², Adj R², RMSE, MAE                       |
| Assumption Results      | Normality, Homoskedasticity, VIF            |
| Residual Plots Reviewed | QQ, Residuals vs Fitted, Cook’s D           |
| Coefficient Table       | With CIs and p-values                       |
| Regularization Path     | Optional (if used)                          |
| Notes / Caveats         | Outliers, limitations, transformation notes |

---

## 🧠 Final Tip

> “Linear regression isn't fragile — it's transparent. Use diagnostics to tune it, not discard it.”

Use with: Linear Regression Summary Sheet, Visual Guide, and Residual Diagnostics Runner.
