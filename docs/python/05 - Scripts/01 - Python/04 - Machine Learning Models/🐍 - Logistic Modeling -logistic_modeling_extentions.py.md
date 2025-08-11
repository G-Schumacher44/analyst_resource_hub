____
# logistic_modeling_extensions.py

##📲 **Function calls and Imports**
```python
#📦Imports
import statsmodels.api as sm
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import NotFittedError
from sklearn.metrics import classification_report

#funtion calls

#bianry regression
from modeling.logistic_modeling_extensions import logistic_regression_runner
model, y_pred, y_proba = logistic_regression_runner(X_train, y_train, X_test, y_test)

#multinomial
from modeling.multinomial_logistic_runner import multinomial_logistic_runner
model, y_pred, y_proba = multinomial_logistic_runner(X_train, y_train, X_test, y_test)

#poisson
from modeling.poisson_regression_runner import poisson_regression_runner
model, y_pred = poisson_regression_runner(X_train, y_train, X_test)

# NB regression
from modeling.nb_regression_runner import nb_regression_runner
model, y_pred = nb_regression_runner(X_train, y_train, X_test)

#ordinal
from modeling.ordinal_regression_runner import ordinal_regression_runner
model, y_pred = ordinal_regression_runner(X_train, y_train_cat, X_test)

#predict proba helper for ordinal
from modeling.ordinal_regression_runner import ordinal_regression_runner
from modeling.helpers.ordinal_predict_proba_helper import convert_cumulative_to_class_probs
# Fit model
model, _ = ordinal_regression_runner(X_train, y_train, X_test)
# Get cumulative probabilities from OrderedModel
cum_probs = model.predict(X_test)
# Convert to class probabilities
class_probs = convert_cumulative_to_class_probs(cum_probs)
# Optional: Predict most probable class
y_pred = class_probs.idxmax(axis=1)
```

## 📈 **Logistic Regression Runner**

```python
## 📈 **Logistic Regression Runner**
def logistic_regression_runner(X_train, y_train, X_test, y_test, solver='liblinear', penalty='l2', C=1.0, max_iter=100):
    """
    Fit a logistic regression model and return it.

    Args:
        X_train, y_train: training features and labels
        X_test, y_test: testing features and labels (optional for later evaluation)
        solver (str): Optimization algorithm ('liblinear' good for small datasets)
        penalty (str): Regularization ('l1', 'l2', or 'elasticnet')
        C (float): Inverse regularization strength (smaller = stronger penalty)
        max_iter (int): Max training iterations

    Returns:
        model: fitted LogisticRegression model
        y_pred: predicted labels on test set
        y_proba: predicted probabilities (class 1) on test set
    """
    model = LogisticRegression(solver=solver, penalty=penalty, C=C, max_iter=max_iter)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("✅ Logistic model fitted.")
    return model, y_pred, y_proba
    ```

___
## 📈 Multinomial Regression Runner**

```python
# multinomial_logistic_runner.py
def multinomial_logistic_runner(X_train, y_train, X_test, y_test=None, C=1.0, max_iter=200):
    """
    Fit a multinomial logistic regression model using scikit-learn.

    Args:
        X_train (pd.DataFrame): Feature matrix
        y_train (pd.Series): Multiclass categorical target (3+ classes)
        X_test (pd.DataFrame): Test features
        y_test (optional): Ground truth labels for evaluation
        C (float): Inverse of regularization strength
        max_iter (int): Max training iterations

    Returns:
        model: fitted LogisticRegression object
        y_pred: predicted class labels
        y_proba: class probability estimates (softmax)
    """
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=C, max_iter=max_iter)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)

    print("✅ Multinomial logistic model fitted.")

    if y_test is not None:
        print("📊 Classification Report:")
        print(classification_report(y_test, y_pred))

    return model, y_pred, y_proba
```
____

# **📂** **poisson regression

```python
# poisson_regression_runner.py
def poisson_regression_runner(X_train, y_train, X_test, y_test=None, add_constant=True):
    """
    Fit a Poisson regression model using statsmodels GLM.

    Args:
        X_train (pd.DataFrame): Feature matrix (train)
        y_train (pd.Series): Target variable (count outcome)
        X_test (pd.DataFrame): Feature matrix (test)
        y_test (optional): Ground truth for test set
        add_constant (bool): Whether to add intercept term

    Returns:
        model: fitted statsmodels GLM Poisson model
        y_pred: predicted counts for X_test
    """
    if add_constant:
        X_train = sm.add_constant(X_train)
        X_test = sm.add_constant(X_test, has_constant='add')

    model = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()
    y_pred = model.predict(X_test)

    print("✅ Poisson regression model fitted.")
    return model, y_pred
```

___

# **📂** **negative binomial regression**
```python
# nb_regression_runner.py
def nb_regression_runner(X_train, y_train, X_test, y_test=None, add_constant=True):
    """
    Fit a Negative Binomial regression model using statsmodels GLM.

    Args:
        X_train (pd.DataFrame): Feature matrix (train)
        y_train (pd.Series): Target variable (count outcome)
        X_test (pd.DataFrame): Feature matrix (test)
        y_test (optional): Ground truth for test set
        add_constant (bool): Whether to add intercept term

    Returns:
        model: fitted statsmodels GLM NegativeBinomial model
        y_pred: predicted counts for X_test
    """
    if add_constant:
        X_train = sm.add_constant(X_train)
        X_test = sm.add_constant(X_test, has_constant='add')

    model = sm.GLM(y_train, X_train, family=sm.families.NegativeBinomial()).fit()
    y_pred = model.predict(X_test)

    print("✅ Negative Binomial regression model fitted.")
    return model, y_pred
```

___

# **📂** **ordinal regression
```python
# ordinal_regression_runner.py
def ordinal_regression_runner(X_train, y_train, X_test, y_test=None, method='logit'):
    """
    Fit an Ordinal Logistic Regression model using statsmodels OrderedModel.

    Args:
        X_train (pd.DataFrame): Features
        y_train (pd.Series): Ordinal target (must be ordered categorical)
        X_test (pd.DataFrame): Features to predict
        y_test (optional): True values
        method (str): 'logit' or 'probit' (link function)

    Returns:
        model: Fitted model
        y_pred: Predicted ordinal class labels
    """
    if not pd.api.types.is_categorical_dtype(y_train):
        raise ValueError("y_train must be an ordered categorical dtype (pd.CategoricalDtype with ordered=True)")

    model = OrderedModel(y_train, X_train, distr=method)
    fitted = model.fit(method='bfgs', disp=False)

    y_pred = fitted.predict(X_test).idxmax(axis=1)

    print("✅ Ordinal regression model fitted.")
    return fitted, y_pred
```

___

# **📂** **ordinal predict proba helper**
```python
# ordinal_predict_proba_helper.py
def convert_cumulative_to_class_probs(cum_probs_df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert cumulative probabilities output by statsmodels OrderedModel.predict()
    into class-level probabilities.

    Args:
        cum_probs_df (pd.DataFrame): Output of OrderedModel.predict(X_test)
            Each column should represent P(Y ≤ class_k)

    Returns:
        class_probs_df (pd.DataFrame): Each column is the probability of class_k
    """
    class_probs = cum_probs_df.copy()

    # Compute class probabilities from cumulative ones
    class_probs.iloc[:, 1:] = cum_probs_df.iloc[:, 1:].values - cum_probs_df.iloc[:, :-1].values
    class_probs.iloc[:, 0] = cum_probs_df.iloc[:, 0]
    class_probs.iloc[:, -1] = 1 - cum_probs_df.iloc[:, -2]

    return class_probs
```