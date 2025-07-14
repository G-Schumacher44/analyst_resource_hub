#GAD #Coursera #dataAnalytics #regression 
Regression Analysis
**Course:** [[Google Advanced Data Analytics Certificate]]  
**Module:** 5
___
## 🔢 Purpose
This companion focuses on **visual evaluation and diagnostics after fitting a linear regression model**. It complements pre-modeling EDA workflows and ensures your model outputs are thoroughly analyzed before final acceptance.

---

## 🔢 1. Actual vs Predicted Plot
**Goal:** Check how well predicted values match true values.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 45-degree line
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted')
plt.show()
```

| What to Look For |
|------------------|
| Points clustered around red line ✅ Good predictions |
| Systematic deviation from line ⚠️ Bias or underfitting |

---

## 📊 2. Residuals vs Predicted Plot
**Goal:** Check homoscedasticity (constant variance of errors).

```python
residuals = y_test - y_pred

plt.figure(figsize=(6,4))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Values')
plt.show()
```

| What to Look For |
|------------------|
| Random cloud around 0 ✅ Homoscedastic |
| Funnel shape ⚠️ Heteroskedasticity |
| Curve shape ⚠️ Misspecified model |

---

## 📁 3. Histogram of Residuals
**Goal:** Check if residuals are approximately normally distributed.

```python
sns.histplot(residuals, kde=True)
plt.title('Histogram of Residuals')
plt.xlabel('Residual')
plt.show()
```

| What to Look For |
|------------------|
| Bell-shaped curve ✅ Normality assumption good |
| Skewed or multi-modal ⚠️ Possible issues |

---

## 📋 4. QQ Plot of Residuals
**Goal:** Further assess normality of errors.

```python
import statsmodels.api as sm

sm.qqplot(residuals, line='45')
plt.title('QQ Plot of Residuals')
plt.show()
```

| What to Look For |
|------------------|
| Points along 45° line ✅ Good normality |
| Systematic bends ⚠️ Skewness or heavy tails |

---

## 📊 5. Key Model Metrics
**Goal:** Report numerical evaluation of model quality.

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'RMSE: {rmse:.4f}')
print(f'MAE: {mae:.4f}')
print(f'R²: {r2:.4f}')
```

| Metric | Meaning |
|--------|---------|
| RMSE | Root mean square error (penalizes big errors) |
| MAE | Mean absolute error (straight average error) |
| R² | Variance explained by model |

---

## 📖 6. Model Complexity and Selection (Optional)
**Goal:** Compare models if fitting multiple.

```python
print(f'AIC: {model.aic}')
print(f'BIC: {model.bic}')
```
_(for statsmodels fitted OLS objects)_

| What to Look For |
|------------------|
| Lower AIC/BIC ✅ Better model fit given complexity |
| Big drop moving to higher-order polynomials? ⚠️ Risk of overfitting |

---

# 📈 Visual Evaluation Checklist
- [ ] Actual vs Predicted: Points along 45° line?
- [ ] Residuals vs Predicted: Random spread around 0?
- [ ] Histogram of Residuals: Bell-shaped?
- [ ] QQ Plot: Points fall along line?
- [ ] RMSE, MAE, R² reported?
- [ ] AIC/BIC if comparing models?

---

# 💚 Final Analyst Tip
> Always combine **visual evaluation** + **metric reporting** to build the most credible, transparent, and defensible linear regression models!