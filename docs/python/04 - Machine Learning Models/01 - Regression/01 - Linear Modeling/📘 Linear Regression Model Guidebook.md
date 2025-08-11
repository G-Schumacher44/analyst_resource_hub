___

## 🎯 Purpose
This guidebook provides a comprehensive overview of **exploratory data analysis (EDA)** and **model-specific tools** for linear regression. It focuses first on foundational **OLS modeling and interpretation**, then expands to cover **robust modifications**, **regularization techniques**, and **advanced model diagnostics**. A separate companion will cover **visual-only EDA and interpretation guidance**.

---

## 🟦 Section 1: Ordinary Least Squares (OLS) Regression

### 📌 Goal
Model a continuous dependent variable assuming a linear relationship with predictors.

### 📊 Key Visuals
- **Histogram of Residuals**
- **QQ Plot** (normality check)
- **Residuals vs Fitted Plot**
- **Boxplot of Residuals by Group** (for categorical variables)

### 📈 Interpretation Checklist
- R² and Adjusted R² for variance explained
- Coefficients: interpret as change in predicted Y per 1-unit X
- p-values: assess significance of predictors
- Confidence intervals: assess estimate precision

### 📉 Assumption Diagnostics
| Assumption         | Visual Tool                      | What to Look For                            |
|--------------------|----------------------------------|---------------------------------------------|
| Linearity          | Scatterplot / Residuals vs Fit   | Flat horizontal band                        |
| Normality          | QQ Plot / Histogram              | Points on 45° line / Bell shape             |
| Homoscedasticity   | Residuals vs Fitted              | Constant spread (no funnel shape)           |
| No Multicollinearity | Correlation matrix / VIF       | Low off-diagonal correlations / VIF < 5     |

---

## 🟨 Section 2: Robust and Modified OLS Variants

### 📉 Heteroskedasticity-Consistent Standard Errors (HC1, HC2, HC3)

These adjustments provide **robust standard errors** for OLS without changing the coefficient estimates. They are useful when the assumption of **homoscedasticity** (constant variance) is violated.

#### ✅ Purpose:
- Maintain valid inference (p-values, confidence intervals) under heteroskedasticity

#### 🔢 Common Variants:
| Method | Description |
|--------|-------------|
| **HC0** | White’s original robust estimator |
| **HC1** | Scaled HC0 (accounts for degrees of freedom) |
| **HC2** | Adjusts based on leverage values (better for small n) |
| **HC3** | Stronger correction, like jackknife; often recommended |

#### 🐍 Example (Python):
```python
model = sm.OLS(y, X).fit()
robust_model = model.get_robustcov_results(cov_type='HC3')
print(robust_model.summary())
```

✔️ Useful in applied work when using OLS but facing **heteroskedastic residuals**.

---

### 🛠 Robust Linear Models (RLM)
- Use when outliers or non-normal residuals distort OLS
- Fit via Huber loss or M-estimators

#### 🔍 Visual Tools
- **Influence Plot (Cook’s Distance)**
- **Leverage vs Residuals Plot**
- **Comparison of OLS vs RLM fits**

#### 📈 Interpretation:
- Coefficients are **less sensitive to outliers**
- Use to validate the stability of findings from OLS

### 📐 Weighted Least Squares (WLS)
- Use when variance of residuals is **not constant**
- Weights reduce impact of high-variance points

---

## **🟥 Section 3: Regularization Techniques (Ridge, Lasso, and Elastic Net)**

  ### **🎯 Purpose**

  Shrink and regularize coefficients to avoid overfitting or reduce redundancy.

| Method      | Penalty                                                                   | Effect                                 |
| ----------- | ------------------------------------------------------------------------- | -------------------------------------- |
| Ridge       | $\lambda \sum \beta^2$                                                    | Shrinks all coefficients               |
| Lasso       | $\lambda \sum \|\beta\|$                                                  | Shrinks and selects (forces some to 0) |
| Elastic Net | $\lambda\left[ \alpha \sum \|\beta\| + (1 - \alpha) \sum \beta^2 \right]$ | Mixes Ridge and Lasso                  |

### 📊 Visual Tools
- Coefficient Path Plot
    
- Feature Importance Ranking
    
- RMSE vs Alpha (validation curve)

### ✅ When to Use
- Many correlated predictors
- Concern for overfitting
- Preference for model parsimony (Lasso)
- 
## Examples 
**Elastic Net Example (Python):**
```python
from sklearn.linear_model import ElasticNetCV
model = ElasticNetCV(l1_ratio=[.1, .5, .9], alphas=[0.01, 0.1, 1.0], cv=5).fit(X, y)
```

**Ridge Example (Python):**
```python
from sklearn.linear_model import RidgeCV
model = RidgeCV(alphas=[0.01, 0.1, 1.0], cv=5).fit(X, y)
```

**Lasso Example (Python):**
```python
from sklearn.linear_model import LassoCV
model = LassoCV(alphas=[0.01, 0.1, 1.0], cv=5).fit(X, y)
```


---

# 🧪 Section 4: Assumption Tests

Assumption tests help validate the reliability of linear regression results beyond visual inspections. These tests provide statistical evidence for model trustworthiness.

### 🧪 Normality of Residuals
- **Shapiro-Wilk Test**: Tests if residuals come from a normal distribution
- **Kolmogorov-Smirnov Test**: Compares empirical distribution with theoretical normal
- **Anderson-Darling Test**: More sensitive to tail behavior

**Python Example:**
```python
from scipy.stats import shapiro, kstest
shapiro(residuals)
kstest(residuals, 'norm')
```

### 📉 Homoscedasticity (Equal Variance)
- **Breusch-Pagan Test**: Tests if variance of residuals depends on predictors
- **White Test**: General test for heteroskedasticity (includes non-linearities)

**Python Example:**
```python
from statsmodels.stats.diagnostic import het_breuschpagan
het_breuschpagan(residuals, model.model.exog)
```

### 🔁 Autocorrelation of Residuals
- **Durbin-Watson Test**: Tests for first-order autocorrelation in residuals
- **Ljung-Box Test**: More general test for autocorrelation at multiple lags

**Python Example:**
```python
from statsmodels.stats.stattools import durbin_watson
durbin_watson(residuals)
```

### 📌 When to Use
- To **confirm visual observations** (e.g., funnel shapes or curved patterns)
- Before **drawing conclusions** from p-values or confidence intervals
- When **presenting** findings to stakeholders who require rigorous validation

### 🔍 Interpretation Guide
| Test                 | Low p-value Means...                      |
|----------------------|--------------------------------------------|
| Shapiro/K-S          | Residuals are **not** normally distributed |
| Breusch-Pagan/White  | Variance of residuals **is not constant**  |
| Durbin-Watson < 2    | Positive autocorrelation in residuals      |

| Assumption        | Test (in addition to visual)            |
|-------------------|------------------------------------------|
| Normality         | Shapiro-Wilk, Kolmogorov-Smirnov        |
| Heteroskedasticity| Breusch-Pagan, White test               |
| Autocorrelation   | Durbin-Watson                           | Durbin-Watson                           |

Use these to confirm visual trends are statistically significant.

---

## 🧮 Section 5: Residual Types

Residuals represent the difference between observed values and model predictions. Understanding different types of residuals helps diagnose outliers, leverage points, and model fit issues.

### 🔹 Raw Residuals
- Basic difference: $e_i = y_i - \hat{y}_i$
- Used in plots like residuals vs fitted

### 🔹 Standardized Residuals
- Raw residuals divided by their standard deviation
- Useful for identifying relative deviation
- Rule of thumb: $|\text{standardized residual}| > 2$ may indicate outliers

### 🔹 Studentized Residuals
- Standardized with an estimate of their own variance
- More accurate than standardized residuals
- Used for **outlier testing** and model diagnostics

**Python Example:**
```python
import statsmodels.api as sm
influence = model.get_influence()
studentized_residuals = influence.resid_studentized_internal
```

---

## 🔁 Section 6: Interaction Terms

Interaction terms capture effects that emerge **only when two predictors are considered together**. They help detect whether the relationship between one variable and the outcome depends on another variable.

### 🧠 Why Use Them
- Uncover **non-additive effects**
- Model group-specific slopes
- Improve prediction in heterogeneous data

### 🛠 How to Add Interactions
- **In formulas**: use `*` for main + interaction terms, or `:` for interaction only
  - `X1 * X2` → includes `X1`, `X2`, and `X1:X2`
  - `X1:X2` → includes only the interaction

### 📉 Example: Income by Gender
```python
import statsmodels.formula.api as smf
model = smf.ols('income ~ experience * gender', data=df).fit()
```
✔️ Captures different effects of experience on income by gender

### 📊 Visual Interpretation
- **Grouped scatter plots with regression lines**
- **Simple slopes plots** (visualize slope of one variable at levels of another)
- **Interaction plots** for categorical × continuous combos

### 🧪 Model Interpretation Tips
- Significant interaction term → the slope of one variable **depends** on the level of the other
- Always interpret interaction terms **in context with their main effects**

### 🔍 Common Pitfalls
- **Overfitting** with too many interaction terms
- **Multicollinearity** if predictors are correlated — consider centering variables first

---
**Visuals:**
- Overlay regression lines by group
- Slope difference (simple slopes plots)

---

## 🔄 Section 7: Feature Transformation

Feature transformations are used to fix violations of linear regression assumptions and improve model interpretability and predictive performance.

### 🧠 When to Use
- **Skewed distributions** in the target or predictors
- **Non-linear relationships** with the dependent variable
- **Heteroskedasticity** (non-constant variance of residuals)

### 🛠 Common Transformations

| Transformation  | When to Use                                    | Effect                                      |
|-----------------|------------------------------------------------|---------------------------------------------|
| Log             | Positive-skewed data, exponential growth       | Compresses large values                     |
| Square Root     | Count data or moderate skew                    | Reduces range while preserving order        |
| Box-Cox         | Positive, non-normal distributions             | Stabilizes variance and normalizes          |
| Yeo-Johnson     | Like Box-Cox, but supports 0 and negatives     | Flexible for a broader range of data        |
| Z-Score Scaling | Features on different scales                   | Normalizes for models sensitive to scale    |
| Min-Max Scaling | Keep values between 0 and 1                    | Preserves shape, shifts scale               |

### 📉 Python Examples
```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import PowerTransformer, StandardScaler

# Log Transformation
df['log_x'] = np.log(df['x'] + 1)

# Box-Cox and Yeo-Johnson
pt = PowerTransformer(method='yeo-johnson')
df['yj_x'] = pt.fit_transform(df[['x']])

# Standardization
scaler = StandardScaler()
df['z_x'] = scaler.fit_transform(df[['x']])
```

### 📊 Visual Checks Before/After
- Histograms (check for skew reduction)
- Scatter plots (check linearity improvement)
- Residual vs Fitted (check for constant variance)

### ⚠️ Notes
- **Don’t transform test set independently** — always fit transformation on training data
- Log and Box-Cox require positive inputs — use shifts or Yeo-Johnson when needed
- Check interpretation impact — transformed variables may lose intuitive meaning

---
**Examples:**
- Log
- Square root
- Box-Cox (Yeo-Johnson for 0s and negatives)


---

## 📏 Section 8: Model Evaluation and Comparison

### 📈 Visuals
- Actual vs Predicted Scatter Plot
- Residuals vs Predicted Values
- RMSE / MAE vs Model Complexity (degree, alpha, etc.)

### 📊 Core Evaluation Metrics
| Metric     | Description                                     |
|------------|-------------------------------------------------|
| RMSE       | Root Mean Squared Error — penalizes large errors|
| MAE        | Mean Absolute Error — interpretable in same units as Y |
| R²         | Proportion of variance explained by model       |
| Adjusted R²| Adjusts for number of predictors                |
| AIC / BIC  | Penalize complexity, used for model selection   |

---

## 🧪 Train/Test Split

### 🎯 Purpose
Split your dataset into **training** and **testing** sets to evaluate how well your model generalizes to unseen data.

### 🐍 Python Example
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```
- `test_size=0.2`: 80/20 split
- `random_state`: ensures reproducibility

### 📊 Evaluate on Test Set
```python
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
```

### ✅ Best Practices
- Always scale and fit only on the **training set**, then transform the test set
- Don't tune on the test set — use **validation sets** or **cross-validation**
- Helps detect overfitting and underfitting

### 🔁 Optional Extensions
- **K-Fold Cross-Validation** for small datasets
- **Stratified Split** if working with classification-type grouping


---

## ✅ Summary Table

| Component          | Tool / Concept                   | Purpose                                |
|--------------------|----------------------------------|----------------------------------------|
| OLS Fit            | Residual, QQ, Histogram          | Assumption validation                  |
| Robust Methods     | RLM, WLS, HC3                    | Handle outliers or variance changes    |
| Regularization     | Ridge, Lasso, Elastic Net        | Reduce overfit, enhance generalization |
| Statistical Tests  | Shapiro, BP, DW                  | Quantify assumption fit                |
| Residual Types     | Standardized, studentized        | Outlier and leverage diagnostics       |
| Interaction Terms  | Grouped slope plots              | Detect interaction effects             |
| Model Selection    | AIC, BIC, RMSE, validation curves| Evaluate and compare models            |

---




### 🔗 **Related Notes**

- [[Links]]