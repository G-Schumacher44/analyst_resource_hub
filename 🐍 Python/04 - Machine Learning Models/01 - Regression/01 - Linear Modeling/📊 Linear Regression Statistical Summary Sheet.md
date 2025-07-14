___
## 🎯 Purpose

This reference provides statistical evaluation tools and interpretation guidelines for linear regression models, including OLS, Ridge, and Lasso. It supports supervised learning workflows with model summaries, diagnostic metrics, and regression-specific visuals.

---

## 📐 1. Linear Regression Metrics

### ✅ R² (Coefficient of Determination)

Proportion of variance in target explained by the model.

```python
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)
```

* Range: 0–1 (higher is better)
* Adjusted R² preferred when comparing models with different numbers of predictors

---

### ✅ Mean Squared Error (MSE) / Root MSE

Measures average squared error (and its square root).

```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y_true, y_pred)          # MSE
mean_squared_error(y_true, y_pred, squared=False)  # RMSE
```

* Lower is better
* RMSE is in same units as target

---

### ✅ Mean Absolute Error (MAE)

Average of absolute errors (robust to outliers).

```python
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_true, y_pred)
```

---

### ✅ Residual Standard Error (RSE)

Standard deviation of the residuals (from statsmodels OLS).

```python
model = sm.OLS(y, X).fit()
np.sqrt(model.mse_resid)
```

---

### ✅ Durbin-Watson Statistic

Detects autocorrelation in residuals.

```python
from statsmodels.stats.stattools import durbin_watson
durbin_watson(model.resid)
```

* Values near 2 suggest no autocorrelation

---

### ✅ Breusch-Pagan / White Tests

Detect heteroscedasticity (non-constant variance).

```python
from statsmodels.stats.diagnostic import het_breuschpagan
het_breuschpagan(model.resid, model.model.exog)
```

---

## 📊 2. Visual + Residual Diagnostics

* Residuals vs Fitted Plot (check linearity & homoscedasticity)
* Histogram of residuals (normality)
* QQ Plot (normal residual assumption)
* Leverage vs residual plot (outlier detection)
* VIF summary (detect multicollinearity)

---

## 🧾 3. Suggested Report Summary Table

| Field                | Description                             |
| -------------------- | --------------------------------------- |
| Model Type           | Linear / Ridge / Lasso                  |
| R² / Adj. R²         | Variance explained                      |
| MSE / RMSE / MAE     | Model fit metrics                       |
| Residual Std. Error  | From statsmodels OLS                    |
| Residual Diagnostics | DW stat, BP/White test                  |
| Feature Diagnostics  | VIF, collinearity summary               |
| Visuals Reviewed     | Residuals vs fitted, QQ, leverage plots |
| Notes or Limitations | Summary of assumption checks            |

---

## 🧠 Final Tip

> “Regression is about patterns and assumptions — validate both with numbers and visuals.”

Use with: Residual Diagnostics Runner, Visual Regression Guide, and Evaluation Checklists.
