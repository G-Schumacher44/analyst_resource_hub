

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import statsmodels.api as sm
from scipy import stats
from scipy.stats import kurtosis

def load_data(filepath):
    return pd.read_csv(filepath)

def generate_basic_summary(df):
    print("="*50)
    print("🔎 Dataset Shape:", df.shape)
    print("="*50)
    print("\n🔎 Column Data Types:\n", df.dtypes)
    print("="*50)
    print("\n🔎 Missing Values per Column:\n", df.isnull().sum().sort_values(ascending=False))
    print("="*50)
    print("\n🔎 Descriptive Statistics (Numerical Only):\n", df.describe())
    print("="*50)
    print("\n🔎 Duplicate Rows:", df.duplicated().sum())
    print("="*50)
    print("\n🔎 Memory Usage (in MB): {:.3f}".format(df.memory_usage(deep=True).sum() / 1_000_000))
    print("="*50)
    print("\n🔎 Random Sample (5 Rows):\n", df.sample(n=5, random_state=42))
    print("="*50)

def plot_missingness(df_raw, title="Missing Data Matrix (Field View)"):
    plt.figure(figsize=(16, 8))
    msno.matrix(df_raw, color=(0.2, 0.4, 0.8))
    plt.xlabel("Features", fontsize=12)
    plt.ylabel("Samples", fontsize=12)
    plt.xticks(rotation=45, ha='left')
    plt.yticks(fontsize=10)
    plt.gca().set_title(f"{title}\nSimulated Post-Expedition Survey - May 2025", fontsize=16)
    ax = plt.gca()
    ax.annotate('Missingness per Feature', xy=(1.05, 0.5), xycoords='axes fraction', rotation=90, fontsize=12, va='center')
    plt.show()

def plot_numeric_distributions(df, numeric_cols, bins=30, kde_bw=1.0, xlims=None):
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(
            df[col],
            kde=True,
            bins=bins,
            color='steelblue',
            edgecolor='black',
            kde_kws={'bw_adjust': kde_bw}
        )
        if xlims and col in xlims:
            plt.xlim(xlims[col])
        plt.title(f"Distribution of {col}", fontsize=12)
        plt.xlabel(col, fontsize=10)
        plt.ylabel("Frequency", fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

def scatter_with_regression(df, x_col, y_col):
    """
    Create a scatter plot with a regression line.
    
    Args:
        df (DataFrame): Dataset
        x_col (str): Column name for X
        y_col (str): Column name for Y
    """
    plt.figure(figsize=(8, 6))
    sns.regplot(x=x_col, y=y_col, data=df, ci=95, line_kws={"color": "red"})
    plt.title(f"Scatter Plot of {y_col} vs {x_col} with Regression Line", fontsize=16)
    plt.xlabel(x_col, fontsize=14)
    plt.ylabel(y_col, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df, numeric_cols, title="Feature Correlation Matrix"):
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title(title, fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_scatter_matrix(df, numeric_cols, title="Scatterplot Matrix"):
    sns.pairplot(df[numeric_cols])
    plt.tight_layout()
    plt.show()

def plot_boxplots_with_outliers(df, numeric_cols):
    for col in numeric_cols:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[col], color='lightblue')
        plt.title(f"Boxplot of {col}", fontsize=16)
        plt.xlabel(col, fontsize=14)
        plt.ylabel("Frequency", fontsize=14)
        plt.tight_layout()
        plt.show()

def boxplot_cat_vs_numeric(df, categorical_cols, numeric_cols):
    for cat_col in categorical_cols:
        for num_col in numeric_cols:
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=df[cat_col], y=df[num_col], hue=df[cat_col], palette="Set1", showfliers=True)
            plt.legend().set_visible(False)
            plt.title(f"Boxplot of {num_col} by {cat_col}", fontsize=16)
            plt.xlabel(cat_col, fontsize=14)
            plt.ylabel(num_col, fontsize=14)
            plt.xticks(rotation=45, fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()

def plot_feature_vs_target_boxplots(df, numeric_cols, target_col):
    """
    For classification: Boxplots of numeric features by target class.
    """
    for num_col in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=target_col, y=num_col, data=df, palette="Set2")
        plt.title(f"{num_col} vs {target_col}", fontsize=14)
        plt.xlabel(target_col, fontsize=12)
        plt.ylabel(num_col, fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

def plot_qq(df, numeric_cols):
    for col in numeric_cols:
        if df[col].dtype in [np.float64, np.int64]:
            print(f"Generating Q-Q plot for {col}")
            plt.figure(figsize=(8, 6))
            stats.probplot(df[col], dist="norm", plot=plt)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.title(f"Q-Q Plot of {col}", fontsize=16)
            plt.xlabel('Theoretical quantiles', fontsize=14)
            plt.ylabel('Ordered Values', fontsize=14)
            plt.tight_layout()
            plt.show()
        else:
            print(f"Skipping {col} as it is not numeric.")

def detect_outliers(df, numeric_cols, method='iqr', threshold=3.0):
    outlier_summary = {}
    for col in numeric_cols:
        if df[col].dtype in [np.float64, np.int64]:
            if method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
            elif method == 'zscore':
                z_scores = (df[col] - df[col].mean()) / df[col].std()
                outliers = np.abs(z_scores) > threshold
            outlier_summary[col] = outliers.sum()
    print(f"\n🔎 Outlier Counts ({method.upper()} Method):\n", pd.Series(outlier_summary))


# New function: summarize_outliers
def summarize_outliers(df, numeric_cols, method='iqr', threshold=3.0, return_df=False):
    """
    Summarizes and optionally flags outliers in a new column per feature.

    Args:
        df (DataFrame): Dataset to analyze.
        numeric_cols (list): List of numeric columns.
        method (str): 'iqr' or 'zscore' for outlier detection.
        threshold (float): z-score threshold if using zscore method.
        return_df (bool): If True, returns a copy of df with new outlier flags.

    Returns:
        Optional DataFrame: Original df + outlier flags if return_df=True.
    """
    df_out = df.copy()
    outlier_summary = {}

    for col in numeric_cols:
        if df[col].dtype in [np.float64, np.int64]:
            if method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
            elif method == 'zscore':
                z_scores = (df[col] - df[col].mean()) / df[col].std()
                outliers = np.abs(z_scores) > threshold
            else:
                raise ValueError("Invalid method. Use 'iqr' or 'zscore'.")

            flag_col = f"{col}_outlier"
            df_out[flag_col] = outliers
            outlier_summary[col] = outliers.sum()

    print(f"\n🔎 Outlier Summary ({method.upper()} Method):")
    print(pd.Series(outlier_summary).sort_values(ascending=False))

    if return_df:
        return df_out

def calculate_kurtosis_scipy(df, numeric_cols):
    kurtosis_summary = {}
    for col in numeric_cols:
        kurt_value = kurtosis(df[col], nan_policy='omit')
        kurtosis_summary[col] = kurt_value
    return kurtosis_summary

def calculate_vif(df, numeric_cols):
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    from statsmodels.tools.tools import add_constant
    X = df[numeric_cols].dropna()
    X = add_constant(X)
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print("\n🔎 Variance Inflation Factors (VIF):\n", vif_data.drop(index=0))

def check_high_cardinality(df, categorical_cols, threshold=10):
    for col in categorical_cols:
        unique_count = df[col].nunique()
        print(f"Processing column: {col}")
        if unique_count > threshold:
            print(f"⚠️ High Cardinality in {col}: {unique_count} unique categories")
        else:
            print(f"{col} has {unique_count} unique categories and is within the threshold.")

def calculate_skewness_scipy(df, numeric_cols):
    from scipy.stats import skew
    skewness_summary = {}
    for col in numeric_cols:
        skew_value = skew(df[col].dropna())  # Drop NaNs for accurate calculation
        skewness_summary[col] = skew_value
    return skewness_summary

def run_eda_suite(df, numeric_cols, target_col=None, categorical_cols=None, outlier_method='iqr', outlier_threshold=3.0):
    """
    Runs a full EDA suite: summary, distributions, outliers, correlation, and optional boxplots.
    
    Args:
        df (DataFrame): The dataset.
        numeric_cols (list): List of numeric columns.
        target_col (str, optional): Target column for supervised boxplots.
        categorical_cols (list, optional): List of categorical columns for grouped boxplots.
        outlier_method (str): Method for outlier detection ('iqr' or 'zscore').
        outlier_threshold (float): Threshold for z-score method.
    """
    print("\n🔍 Running Basic Summary")
    generate_basic_summary(df)
    
    print("\n📊 Plotting Numeric Distributions")
    plot_numeric_distributions(df, numeric_cols)
    
    print("\n📦 Checking for Outliers")
    detect_outliers(df, numeric_cols, method=outlier_method, threshold=outlier_threshold)
    
    print("\n🔗 Correlation Heatmap")
    plot_correlation_matrix(df, numeric_cols)
    
    if categorical_cols:
        print("\n📦 Boxplots: Categorical vs Numeric")
        boxplot_cat_vs_numeric(df, categorical_cols, numeric_cols)
    
    if target_col:
        print(f"\n🎯 Boxplots: Numeric Features vs Target ({target_col})")
        plot_feature_vs_target_boxplots(df, numeric_cols, target_col)

def plot_categorical_distributions(df, categorical_cols, hue=None):
    """
    Plots count distributions for categorical columns.

    Args:
        df (DataFrame): The dataset.
        categorical_cols (list): List of categorical column names.
        hue (str, optional): Column name to use for color grouping (e.g. 'left').
    """
    for col in categorical_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col, hue=hue, order=df[col].value_counts().index, palette="Set2")
        plt.title(f"Distribution of {col}" + (f" by {hue}" if hue else ""), fontsize=14)
        plt.xlabel(col, fontsize=12)
        plt.ylabel("Count", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()


# New function: flag_outliers
def flag_outliers(df, column, method='iqr', threshold=3.0, flag_column_name=None):
    """
    Flags outliers in a specific column using IQR or Z-score method.

    Args:
        df (DataFrame): The dataset.
        column (str): Column to check for outliers.
        method (str): 'iqr' or 'zscore'.
        threshold (float): Z-score threshold (only applies if method='zscore').
        flag_column_name (str, optional): Name of the new column. Defaults to {column}_outlier.

    Returns:
        DataFrame: Original df with new boolean outlier flag column.
    """
    df_out = df.copy()

    if df[column].dtype not in [np.float64, np.int64]:
        raise ValueError(f"{column} must be numeric.")

    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (df[column] < lower_bound) | (df[column] > upper_bound)
    elif method == 'zscore':
        z_scores = (df[column] - df[column].mean()) / df[column].std()
        outliers = np.abs(z_scores) > threshold
    else:
        raise ValueError("Invalid method. Use 'iqr' or 'zscore'.")

    if not flag_column_name:
        flag_column_name = f"{column}_outlier"

    df_out[flag_column_name] = outliers
    print(f"✅ Added column: {flag_column_name} using {method.upper()} method")

    return df_out