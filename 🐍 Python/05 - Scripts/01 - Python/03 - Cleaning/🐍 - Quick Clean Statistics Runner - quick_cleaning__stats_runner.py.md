___
```python
# 🧹 Quick Cleaning Runner

def quick_cleaning_runner(df, numeric_cols=None):
    """
    Perform a basic quick-cleaning pass on a dataset.

    Args:
        df (DataFrame): Dataset.
        numeric_cols (list or None): List of numeric columns (if None, autodetect).

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
    for col in numeric_cols:
        skew_value = skew(df[col].dropna())
        print(f"{col}: {skew_value:.2f}")

    print("="*50)

    print("\n🔎 Kurtosis per Feature:")
    for col in numeric_cols:
        kurt_value = kurtosis(df[col].dropna())
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
```