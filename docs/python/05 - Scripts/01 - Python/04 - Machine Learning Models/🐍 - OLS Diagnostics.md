
# 🛠️ Post-Modeling Evaluation for OLS


```python
# 🧹 model_diag_regression.py
# ---------------------------------------------------

# 📦 Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats
from sklearn.model_selection import train_test_split
from scipy.stats import jarque_bera
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# ---------------------------------------------------
# 🧪 Post-Model Evaluation
# ---------------------------------------------------

def plot_predicted_vs_actual(y_true, y_pred):
    ...

def plot_residuals_vs_fitted_with_trend(y_pred, residuals):
    ...

def plot_residuals_vs_fitted(y_pred, residuals):
    ...

def plot_residuals_histogram(residuals):
    ...

def plot_qq_residuals(residuals):
    ...

def durbin_watson_test(model):
    ...

def breusch_pagan_test(model):
    ...

def jarque_bera_test(model):
    ...
```

___ 
📈**OLS summary runner

📲 Imports and function calls
```python
# 📦imports
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.metrics import mean_squared_error, r2_score

# ☎️ Function calls
model = sm.OLS(y_train, X_train).fit()
y_pred = model.predict(X_test)

summarize_ols_diagnostics(model, X_test, y_test, y_pred)
```

# 🏃🏻‍♀️ OLS Summary Runner
```python
def summarize_ols_diagnostics(model, X_test, y_test, y_pred, show_plots=True):
    """
    Summarize diagnostics for OLS regression model.

    Args:
        model: fitted statsmodels OLS model
        X_test (pd.DataFrame): test features
        y_test (array-like): true target values
        y_pred (array-like): predicted target values
        show_plots (bool): whether to show diagnostic plots
    """
    residuals = y_test - y_pred

    print("📊 OLS Diagnostics Summary")
    print(f"🔹 R²: {r2_score(y_test, y_pred):.3f}")
    print(f"🔹 MSE: {mean_squared_error(y_test, y_pred):.3f}")
    print(f"🔹 Durbin-Watson: {durbin_watson(residuals):.3f}")

    jb_stat, jb_p, _, _ = jarque_bera(residuals)
    print(f"🔹 Jarque-Bera (Normality): stat={jb_stat:.2f}, p={jb_p:.3f}")

    if hasattr(model, "resid") and hasattr(model, "model"):
        lm_stat, lm_pvalue, _, _ = het_breuschpagan(model.resid, model.model.exog)
        print(f"🔹 Breusch-Pagan (Homoscedasticity): stat={lm_stat:.2f}, p={lm_pvalue:.3f}")
    else:
        print("⚠️ Breusch-Pagan skipped — model must be from statsmodels.OLS.")

    if show_plots:
        from diagnostics.model_diag_regression import (
            plot_residuals_histogram,
            plot_qq_residuals,
            plot_residuals_vs_fitted
        )

        plot_residuals_histogram(residuals)
        plot_qq_residuals(residuals)
        plot_residuals_vs_fitted(model, y_pred)

    print("✅ Diagnostics complete.\n")
```
___

##  📈**Predicted vs Actual Scatter Plot**

```python
def plot_predicted_vs_actual(y_true, y_pred):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_true, y=y_pred)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], color='red', linestyle='--')
    plt.xlabel('Actual Values', fontsize=14)
    plt.ylabel('Predicted Values', fontsize=14)
    plt.title('Predicted vs Actual Values', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___
# 📈 Residuals vs Fitted with Regression Line

```python
def plot_residuals_vs_fitted_with_trend(y_pred, residuals):
    """
    Scatter plot of residuals vs fitted values with trend line.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_pred, y=residuals, color='blue', alpha=0.6)
    sns.regplot(x=y_pred, y=residuals, scatter=False, color='red', lowess=True)  # Lowess smoother
    plt.axhline(0, color='black', linestyle='--')
    plt.xlabel('Fitted Values (Predictions)', fontsize=14)
    plt.ylabel('Residuals', fontsize=14)
    plt.title('Residuals vs Fitted Values with Trend Line', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___
## 📈**Residuals vs Fitted Values**

```python
def plot_residuals_vs_fitted(y_pred, residuals):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_pred, y=residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Fitted Values (Predictions)', fontsize=14)
    plt.ylabel('Residuals', fontsize=14)
    plt.title('Residuals vs Fitted Values', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___

## 📊**Histogram of Residuals**

```python
def plot_residuals_histogram(residuals):
    plt.figure(figsize=(8, 6))
    sns.histplot(residuals, kde=True, color='steelblue', bins=30)
    plt.xlabel('Residual', fontsize=14)
    plt.title('Histogram of Residuals', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___

## 📉  **Q-Q Plot of Residuals**

```python
def plot_qq_residuals(residuals):
    plt.figure(figsize=(8, 6))
    stats.probplot(residuals, dist="norm", plot=plt)
    plt.title('Q-Q Plot of Residuals', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
```

___

## **🧪 Durbin-Watson Test (Autocorrelation of Residuals)**

```python
def durbin_watson_test(model):
    """
    Perform Durbin-Watson test for autocorrelation in residuals.

    Parameters:
    model (RegressionResultsWrapper): Fitted statsmodels OLS model.
    """
    from statsmodels.stats.stattools import durbin_watson

    dw_stat = durbin_watson(model.resid)
    print(f"🔎 Durbin-Watson Statistic: {dw_stat:.3f}")
    print("-" * 50)
```

___
## **🧪 Breusch-Pagan Test (Heteroscedasticity)**
```python
def breusch_pagan_test(model):
    """
    Perform Breusch-Pagan test for heteroscedasticity.

    Parameters:
    model (RegressionResultsWrapper): Fitted statsmodels OLS model.
    """

    from statsmodels.stats.diagnostic import het_breuschpagan
    residuals = model.resid
    exog = model.model.exog
    bp_test = het_breuschpagan(residuals, exog)
    labels = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
    results = dict(zip(labels, bp_test))

    print("🔎 Breusch-Pagan Test Results:")
    for k, v in results.items():
        print(f"{k}: {v:.4f}")
    print("-" * 50)
```

___

## **🧪 Jarque-Bera Test (Normality of Residuals)**
```python
def jarque_bera_test(model):
    """
    Perform Jarque-Bera test for normality of residuals.

    Parameters:
    model (RegressionResultsWrapper): Fitted statsmodels OLS model.
    """
    from scipy.stats import jarque_bera

    jb_stat, jb_p, _, _ = jarque_bera(model.resid)

    print(f"🔎 Jarque-Bera Statistic: {jb_stat:.4f}")
    print(f"p-value: {jb_p:.4f}")
    print("-" * 50)
```

___
## 📉  **Classification Summary**
```python
# 📉  **Classification Summary**
def print_classification_summary(y_true, y_pred, average='binary'):
    """
    Prints accuracy, precision, recall, and F1-score for a classification task.

    Parameters:
    - y_true: Ground truth labels
    - y_pred: Predicted labels
    - average: Type of averaging performed. 'binary', 'macro', 'micro', or 'weighted'
    """
    print("📊 Classification Summary")
    print("-" * 35)
    print(f"✅ Accuracy : {accuracy_score(y_true, y_pred):.4f}")
    print(f"🎯 Precision: {precision_score(y_true, y_pred, average=average):.4f}")
    print(f"🔁 Recall   : {recall_score(y_true, y_pred, average=average):.4f}")
    print(f"🧮 F1 Score : {f1_score(y_true, y_pred, average=average):.4f}")
    print("-" * 35)
```