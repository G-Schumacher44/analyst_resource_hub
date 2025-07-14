# `quick_clean_stats_runner.py`

```python
import os
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import missingno as msno

# 🧹 Quick Cleaning Runner

def quick_cleaning_runner(df, numeric_cols=None, export_path=None):
    """
    Perform a basic quick-cleaning pass on a dataset.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list or None): List of numeric columns (if None, autodetect).
        export_path (str or None): Path to export summary text file (if None, no export).

    Returns:
        None (prints results and shows visuals)
    """

    # --- Basic Overview ---
    print("="*50)
    print("🔎 Dataset Shape:", df.shape)
    print("="*50)
    
    print("\n🔎 Column Data Types:\n", df.dtypes)
    print("="*50)
    
    print("\n🔎 Missing Values per Column:\n", df.isnull().sum().sort_values(ascending=False))
    print("="*50)
    
    print("\n🔎 Descriptive Statistics:\n", df.describe())
    print("="*50)
    
    # --- Detect Numeric Columns if Needed ---
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # --- Skewness and Kurtosis ---
    from scipy.stats import skew, kurtosis

    print("\n🔎 Skewness per Feature:")
    skewness_dict = {}
    for col in numeric_cols:
        skew_value = skew(df[col].dropna())
        skewness_dict[col] = skew_value
        print(f"{col}: {skew_value:.2f}")

    print("="*50)

    print("\n🔎 Kurtosis per Feature:")
    kurtosis_dict = {}
    for col in numeric_cols:
        kurt_value = kurtosis(df[col].dropna())
        kurtosis_dict[col] = kurt_value
        print(f"{col}: {kurt_value:.2f}")

    print("="*50)

    # --- Outlier Check ---
    outlier_summary = {}
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
        outlier_summary[col] = outliers.sum()

    print("\n🔎 Outlier Counts (IQR Method):\n", pd.Series(outlier_summary))
    print("="*50)

    # --- Missing Data Visualization ---
    import missingno as msno
    msno.matrix(df)

    # --- Export summaries if export_path is provided ---
    if export_path is not None:
        # Ensure directory exists
        dir_name = os.path.dirname(export_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        missing_values = df.isnull().sum().sort_values(ascending=False)

        with open(export_path, 'w') as f:
            f.write("# Quick Cleaning Summary\n\n")
            f.write(f"## Dataset Shape\n\n{df.shape}\n\n")
            f.write("## Column Data Types\n\n")
            for col, dtype in df.dtypes.items():
                f.write(f"- **{col}**: {dtype}\n")
            f.write("\n## Missing Values per Column\n\n")
            for col, miss_count in missing_values.items():
                f.write(f"- **{col}**: {miss_count}\n")
            f.write("\n## Skewness per Feature\n\n")
            for col, val in skewness_dict.items():
                f.write(f"- **{col}**: {val:.2f}\n")
            f.write("\n## Kurtosis per Feature\n\n")
            for col, val in kurtosis_dict.items():
                f.write(f"- **{col}**: {val:.2f}\n")
            f.write("\n## Outlier Counts (IQR Method)\n\n")
            for col, val in outlier_summary.items():
                f.write(f"- **{col}**: {val}\n")
```