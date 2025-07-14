____
# 🛠️ Function Calls & Imports

```python
# 📦 Imports
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

from utils import train_test_split_simple  # Import the function

# Define your feature columns and target
feature_cols = ['feature1', 'feature2', 'feature3']  # <-- Customize
target_col = 'target'  # <-- Customize

# Run the train-test split
X_train, X_test, y_train, y_test = train_test_split_simple(df, feature_cols, target_col)

#VIF helper(threhold0.5)
# Drop constant if present
X = sm.add_constant(X_train)
X = X.drop(columns="const", errors="ignore")

summarize_vif(X)
```

___

# **📚 Train/test Split**

```python
# 🧹 train_test_split_utils.py
from sklearn.model_selection import train_test_split

# --- Basic Train/Test Split ---
def train_test_split_simple(df, feature_cols, target_col, test_size=0.2, random_state=42):
    """
    Simple train-test split.

    Args:
        df (DataFrame): The full dataset.
        feature_cols (list): List of feature column names.
        target_col (str): Name of target column.
        test_size (float): Fraction of data to reserve for test.
        random_state (int): Random seed.

    Returns:
        X_train, X_test, y_train, y_test
    """
    X = df[feature_cols]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    print(f"🔵 Training samples: {X_train.shape[0]}")
    print(f"🟠 Testing samples: {X_test.shape[0]}")
    print("-" * 50)

    return X_train, X_test, y_train, y_test
```

___
# **🧠 Function: summarize_vif(X, threshold=5.0)**
```python
def summarize_vif(X, threshold=5.0):
    """
    Print a VIF summary table for each feature.

    Args:
        X (pd.DataFrame): DataFrame of input features (must not include constant column)
        threshold (float): Optional threshold to flag high multicollinearity

    Returns:
        pd.DataFrame: VIF table with warnings for high values
    """
    if not isinstance(X, pd.DataFrame):
        raise ValueError("X must be a pandas DataFrame")

    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    print("📊 Variance Inflation Factor (VIF) Summary:")
    display = vif_data.sort_values("VIF", ascending=False)
    print(display.to_string(index=False))

    if any(display["VIF"] > threshold):
        print(f"\n⚠️ Warning: Some features exceed VIF threshold of {threshold}. Consider checking multicollinearity.")
    else:
        print("\n✅ All VIFs are within acceptable range.")

    return display
```