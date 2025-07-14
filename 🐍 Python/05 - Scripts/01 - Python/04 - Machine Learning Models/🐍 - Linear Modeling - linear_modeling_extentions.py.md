___
## 📲 **Function Calls & Imports
```python
# 📦 Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

#OLS
# 📦 Import
from linear_modeling_extensions import ols_regression_runner

# Train/test already split
model = ols_regression_runner(X_train, y_train, X_test, y_test, robust=True, robust_type='HC3')

#Ridge
# 📦 Import
from linear_modeling_extensions import ridge_regression_runner

# Train/test already split
ridge_model = ridge_regression_runner(X_train, y_train, X_test, y_test, alpha=1.0)

#Lasso
# 📦 Import
from linear_modeling_extensions import lasso_regression_runner

# Train/test already split
lasso_model = lasso_regression_runner(X_train, y_train, X_test, y_test, alpha=0.5)

#Elastic Net
# 📦 Import
from linear_modeling_extensions import elasticnet_regression_runner

# Train/test already split
elasticnet_model = elasticnet_regression_runner(X_train, y_train, X_test, y_test, alpha=1.0, l1_ratio=0.5)

# Polynomial 
# 📦 Import
from linear_modeling_extensions import polynomial_regression_runner

# Assuming X_train, y_train, X_test, y_test already created:
poly_model = polynomial_regression_runner(X_train, y_train, X_test, y_test, degree=2)
```

___

📈 OLS Modeling with Optional Robust Standard Errors Runner
```python
# 📈 OLS Modeling with Optional Robust Standard Errors Runner
def ols_regression_runner(X_train, y_train, X_test, y_test, robust=False, robust_type='HC1'):
    """
    Run OLS regression with optional robust standard errors.

    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training target.
        X_test (DataFrame): Testing features.
        y_test (Series): Testing target.
        robust (bool): If True, use robust standard errors (HC1, HC3, etc).
        robust_type (str): Robust covariance type ('HC1', 'HC2', 'HC3').

    Returns:
        model (RegressionResultsWrapper): Fitted statsmodels model.
    """

    # Add constant to X (for intercept)
    X_train_sm = sm.add_constant(X_train)
    X_test_sm = sm.add_constant(X_test)

    # Fit model
    model = sm.OLS(y_train, X_train_sm).fit()

    # Apply robust if needed
    if robust:
        model = model.get_robustcov_results(cov_type=robust_type)

    # Predict on Test
    y_pred = model.predict(X_test_sm)

    # Evaluation
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n📈 Model Performance on Test Set:")
    print(f"🔵 R² Score: {r2:.4f}")
    print(f"🟠 MAE: {mae:.4f}")
    print(f"🟣 RMSE: {rmse:.4f}")
    print("-" * 50)

    # Summary
    print("\n📋 Model Summary:")
    print(model.summary())

    return model
```

___
# 📈 Ridge Regression Runner
```python
# 📈 Ridge Regression Runner

from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

def ridge_regression_runner(X_train, y_train, X_test, y_test, alpha=1.0):
    """
    Fit Ridge Regression model and evaluate on test data.

    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training target.
        X_test (DataFrame): Test features.
        y_test (Series): Test target.
        alpha (float): Regularization strength.

    Returns:
        model (Ridge): Fitted Ridge model.
    """
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n📈 Ridge Regression Performance:")
    print(f"🔵 R² Score: {r2:.4f}")
    print(f"🟠 MAE: {mae:.4f}")
    print(f"🟣 RMSE: {rmse:.4f}")
    print("-" * 50)

    return model
```

___

# **📈** # **lasso_regression_runner**  **— L1 Regularization**
```python
# 📈 Lasso Regression Runner

from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

def lasso_regression_runner(X_train, y_train, X_test, y_test, alpha=1.0):
    """
    Fit Lasso Regression model and evaluate on test data.

    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training target.
        X_test (DataFrame): Test features.
        y_test (Series): Test target.
        alpha (float): Regularization strength (L1 penalty).

    Returns:
        model (Lasso): Fitted Lasso model.
    """
    model = Lasso(alpha=alpha, max_iter=10000)  # add high max_iter to avoid convergence warnings
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n📈 Lasso Regression Performance:")
    print(f"🔵 R² Score: {r2:.4f}")
    print(f"🟠 MAE: {mae:.4f}")
    print(f"🟣 RMSE: {rmse:.4f}")
    print("-" * 50)

    return model
```

___

# **📈** **elasticnet_regression_runner** — Mix of Lasso and Ridge (L1 + L2 Regularization)
```python
# 📈 ElasticNet Regression Runner

from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

def elasticnet_regression_runner(X_train, y_train, X_test, y_test, alpha=1.0, l1_ratio=0.5):
    """
    Fit ElasticNet Regression model and evaluate on test data.

    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training target.
        X_test (DataFrame): Test features.
        y_test (Series): Test target.
        alpha (float): Overall regularization strength.
        l1_ratio (float): Mix between Lasso (1.0) and Ridge (0.0).

    Returns:
        model (ElasticNet): Fitted ElasticNet model.
    """
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, max_iter=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n📈 ElasticNet Regression Performance:")
    print(f"🔵 R² Score: {r2:.4f}")
    print(f"🟠 MAE: {mae:.4f}")
    print(f"🟣 RMSE: {rmse:.4f}")
    print("-" * 50)

    return model
```

___

# 📈 Polynomial Regression Runner
```python
# 📈 Polynomial Regression Runner
def polynomial_regression_runner(X_train, y_train, X_test, y_test, degree=2):
    """
    Fit Polynomial Regression model and evaluate on test data.

    Args:
        X_train (DataFrame): Training features.
        y_train (Series): Training target.
        X_test (DataFrame): Test features.
        y_test (Series): Test target.
        degree (int): Degree of polynomial transformation.

    Returns:
        model (LinearRegression): Fitted polynomial regression model.
    """
    # Expand features to polynomial terms
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    # Fit a simple Linear Regression on expanded features
    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    # Predict
    y_pred = model.predict(X_test_poly)

    # Evaluate
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n📈 Polynomial Regression Performance:")
    print(f"🔵 Degree: {degree}")
    print(f"🔵 R² Score: {r2:.4f}")
    print(f"🟠 MAE: {mae:.4f}")
    print(f"🟣 RMSE: {rmse:.4f}")
    print("-" * 50)

    return model
```