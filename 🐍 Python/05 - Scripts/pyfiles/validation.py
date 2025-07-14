"""
Validation utilities for categorical fields.
"""

import pandas as pd


def validate_categorical_field(df, column, expected_values, logger=None, clean=True):
    """
    Validates a categorical column against a set of expected values.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        column (str): Name of the column to check.
        expected_values (set): Set of allowed/expected values (case-insensitive).
        logger (Logger, optional): Logger instance for logging. If None, will not log.
        clean (bool): If True, strip and uppercase the column values before validation.

    Returns:
        pd.Series: Boolean mask of invalid rows.
    """
    if column not in df.columns:
        if logger:
            logger.warning(f"⚠️ Column '{column}' not found in dataframe.")
        return pd.Series([False] * len(df))

    series = df[column].dropna()
    if clean:
        series = series.str.strip().str.upper()

    invalid_mask = ~series.isin(expected_values)

    if logger:
        logger.info(f"🔍 Validating {column}: {series.nunique()} unique values")
        logger.warning(f"⚠️ Found {invalid_mask.sum()} invalid entries in '{column}'")
        # Log the actual unique invalid values (if not too many)
        if invalid_mask.sum() > 0:
            sample_invalid = series[invalid_mask].value_counts().head(10)
            logger.warning(f"🔎 Sample invalid entries for '{column}':\n{sample_invalid.to_string()}")

    return invalid_mask


def get_invalid_rows(df, column, expected_values, clean=True):
    """
    Returns a DataFrame of rows with invalid values in a categorical column.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        column (str): Name of the column to validate.
        expected_values (set): Expected valid values.
        clean (bool): If True, apply .strip().upper() before validation.

    Returns:
        pd.DataFrame: Subset of original DataFrame with invalid entries.
    """
    mask = validate_categorical_field(df, column, expected_values, clean=clean)
    return df.loc[mask]


def check_high_cardinality(df, threshold=10, logger=None):
    """
    Logs and returns a summary of object columns with high cardinality.

    Args:
        df (pd.DataFrame): Dataset to check.
        threshold (int): Threshold above which cardinality is flagged.
        logger (Logger, optional): Logger to use for warnings.

    Returns:
        List[str]: List of high-cardinality column names.
    """
    high_card_cols = []
    for col in df.select_dtypes(include='object'):
        n_unique = df[col].nunique()
        if n_unique > threshold:
            high_card_cols.append(col)
            if logger:
                logger.warning(f"⚠️ High cardinality in {col}: {n_unique} unique values")
    return high_card_cols


def clean_categorical_column(series):
    """
    Applies standard cleaning to a categorical pandas Series:
    strips whitespace and converts to uppercase.

    Args:
        series (pd.Series): Series to clean.

    Returns:
        pd.Series: Cleaned version.
    """
    return series.astype(str).str.strip().str.upper()

def validate_datetime_column(df, column, logger=None):
    """
    Validates and logs the number of valid and invalid entries in a datetime column.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        column (str): Name of the datetime column to validate.
        logger (Logger, optional): Logger for logging output.

    Returns:
        Tuple[int, int]: Count of valid and invalid datetime values.
    """
    if column not in df.columns:
        msg = f"⚠️ Column '{column}' not found in DataFrame."
        print(msg)
        if logger:
            logger.warning(msg)
        return 0, 0

    valid = df[column].notnull().sum()
    invalid = df[column].isnull().sum()

    print(f"\n📆 Valid '{column}' values: {valid} | ⚠️ Invalid: {invalid}")
    if logger:
        logger.info(f"📆 Valid '{column}' values: {valid}")
        if invalid > 0:
            logger.warning(f"⚠️ Invalid '{column}' values: {invalid}")

    return valid, invalid

def run_schema_validation(df, expected_columns, logger=None):
    """
    Runs high-level schema checks including:
    - Unexpected or missing columns
    - Duplicate rows

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        expected_columns (set): Set of expected column names.
        logger (Logger, optional): Logger instance for logging.
    """
    actual_columns = set(df.columns)
    extra_columns = actual_columns - expected_columns
    missing_columns = expected_columns - actual_columns

    if extra_columns and logger:
        logger.warning(f"⚠️ Unexpected columns found: {sorted(extra_columns)}")
    if missing_columns and logger:
        logger.warning(f"⚠️ Missing expected columns: {sorted(missing_columns)}")

    # Duplicate row check
    duplicate_rows = df.duplicated().sum()
    if duplicate_rows and logger:
        logger.warning(f"⚠️ Duplicate rows found: {duplicate_rows}")

def summarize_categorical_validation(df, validation_plan, logger=None, print_output=True):
    """
    Performs and summarizes categorical validation checks on specified columns.

    Args:
        df (pd.DataFrame): Input DataFrame.
        validation_plan (dict): Dictionary where keys are column names and values are sets of expected categories.
        logger (Logger, optional): Logger for warnings/info.
        print_output (bool): Whether to print output to console. If False, logs to logger if provided.

    Returns:
        dict: Summary of invalid entries by column (count and sample values).
    """
    summary = {}

    if print_output:
        print("\n🧪 Raw Categorical Validation Summary:")
    for col, expected in validation_plan.items():
        mask = validate_categorical_field(df, col, expected, logger=logger, clean=True)
        count = mask.sum()
        if count > 0:
            invalid_values = (
                df.loc[mask[mask].index, col]
                .dropna()
                .astype(str)
                .str.strip()
                .str.upper()
                .value_counts()
                .head(5)
            )
            formatted = ", ".join(f"{val} ({cnt})" for val, cnt in invalid_values.items())
            summary[col] = {"count": count, "top_values": formatted}
            if print_output:
                print(f" - {col}: {count} invalid — {formatted}")
            else:
                if logger:
                    logger.debug(f"{col}: {count} invalid — {formatted}")
        else:
            summary[col] = {"count": 0, "top_values": ""}
            if print_output:
                print(f" - {col}: ✓")
            else:
                if logger:
                    logger.debug(f"{col}: ✓")

    return summary

def validate_numeric_range(df, column, min_val=None, max_val=None, logger=None):
    """
    Validates that numeric values in a column fall within a specified range.

    Args:
        df (pd.DataFrame): DataFrame to check.
        column (str): Column name to validate.
        min_val (float, optional): Minimum allowed value.
        max_val (float, optional): Maximum allowed value.
        logger (Logger, optional): Logger instance for logging.

    Returns:
        pd.Series: Boolean mask of invalid entries.
    """
    if column not in df.columns:
        if logger:
            logger.warning(f"⚠️ Column '{column}' not found in dataframe.")
        return pd.Series([False] * len(df))

    series = pd.to_numeric(df[column], errors='coerce')
    valid_mask = series.notna()
    invalid_mask = pd.Series(False, index=series.index)

    if min_val is not None:
        invalid_mask |= valid_mask & (series < min_val)
    if max_val is not None:
        invalid_mask |= valid_mask & (series > max_val)

    count_invalid = invalid_mask.sum()
    if logger:
        logger.info(f"🔍 Validating range for '{column}': {count_invalid} out of range")
        if count_invalid > 0:
            logger.warning(f"⚠️ {count_invalid} values in '{column}' are outside the expected range ({min_val} to {max_val})")

    return invalid_mask

def summarize_nulls(df, logger=None, return_output=False, as_markdown=False):
    """
    Summarizes and optionally logs null counts per column.

    Args:
        df (pd.DataFrame): DataFrame to inspect.
        logger (Logger, optional): Logger for warning-level output.
        return_output (bool): Whether to return the summary dictionary.
        as_markdown (bool): Format output as a markdown-style block (notebook-friendly).

    Returns:
        dict (optional): {column_name: null_count}
    """
    nulls = df.isnull().sum()
    null_cols = nulls[nulls > 0]

    if null_cols.empty:
        msg = "✅ No missing values found."
        if logger:
            logger.info(msg)
        if as_markdown:
            print(f"\n🕳️ **Missing Values Summary:**\n- _None_")
        else:
            print(msg)
        return {} if return_output else None

    summary = {col: int(n) for col, n in null_cols.items()}

    if as_markdown:
        lines = ["\n🕳️ **Missing Values Summary:**"]
        total_rows = df.shape[0]
        lines += [f"- {col}: {n} missing ({(n/total_rows*100):.1f}%)" for col, n in summary.items()]
        print("\n".join(lines))
    else:
        formatted = ", ".join(f"{col} ({n})" for col, n in summary.items())
        print("🕳️ Columns with Missing Values:", formatted)

    if logger:
        for col, n in summary.items():
            logger.warning(f"⚠️ {col}: {n} missing values")

    return summary if return_output else None

def check_column_dtypes(df, expected_types, logger=None):
    """
    Checks whether each column matches its expected dtype.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        expected_types (dict): Dict of {column_name: expected_dtype_str}.
        logger (Logger, optional): Logger instance for logging.

    Returns:
        dict: Dictionary with mismatched columns and their actual types.
    """
    mismatches = {}
    for col, expected in expected_types.items():
        if col not in df.columns:
            continue
        actual = df[col].dtype.name
        if actual != expected:
            mismatches[col] = actual
            if logger:
                logger.warning(f"⚠️ Column '{col}' expected type '{expected}' but found '{actual}'")

    if not mismatches and logger:
        logger.info("✅ All column dtypes matched expectations.")

    return mismatches

import json

def summarize_validation_report(
    df,
    validation_plan,
    expected_dtypes=None,
    numeric_ranges=None,
    cardinality_threshold=10,
    logger=None,
    output_path=None
):
    """
    Runs all core validation checks and generates a summary report.
    Saves the report to the specified path if provided.

    Args:
        df (pd.DataFrame): DataFrame to validate.
        validation_plan (dict): Categorical validation map: {col: set(expected values)}.
        expected_dtypes (dict, optional): Dict of expected dtypes.
        numeric_ranges (dict, optional): Dict of {col: (min, max)}.
        cardinality_threshold (int): Threshold for high cardinality flag.
        logger (Logger, optional): Logger to use for detailed warnings.
        output_path (str or Path, optional): File path to save report as JSON.

    Returns:
        dict: Validation summary report.
    """
    report = {}

    # Schema + duplicates
    schema_issues = {}
    expected_cols = {
        'tag_id', 'species', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
        'body_mass_g', 'age_group', 'sex', 'colony_id', 'island', 'capture_date', 'health_status'
    }
    actual_cols = set(df.columns)
    schema_issues["unexpected"] = sorted(actual_cols - expected_cols)
    schema_issues["missing"] = sorted(expected_cols - actual_cols)
    schema_issues["duplicate_rows"] = int(df.duplicated().sum())
    schema_issues["duplicate_tag_ids"] = int(df['tag_id'].duplicated().sum())
    report["schema"] = schema_issues

    # Categorical
    cat_summary = summarize_categorical_validation(df, validation_plan, logger)
    report["categorical"] = cat_summary

    # Numeric Ranges
    if numeric_ranges:
        num_summary = {}
        for col, (min_val, max_val) in numeric_ranges.items():
            mask = validate_numeric_range(df, col, min_val, max_val, logger)
            num_summary[col] = int(mask.sum())
        report["numeric_ranges"] = num_summary

    # Cardinality
    card_cols = check_high_cardinality(df, threshold=cardinality_threshold, logger=logger)
    report["high_cardinality_fields"] = card_cols

    # Dtypes
    if expected_dtypes:
        type_issues = check_column_dtypes(df, expected_dtypes, logger)
        report["dtypes"] = type_issues

    # Save to file
    if output_path:
        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)
        if logger:
            logger.info(f"📄 Validation report saved to {output_path}")

    return report


# Notebook-friendly wrapper to display missing values summary as markdown
def display_missing_summary(df):
    """
    Notebook-friendly wrapper to display missing values summary
    as a clean markdown-style block.

    Args:
        df (pd.DataFrame): DataFrame to summarize.
    """
    summarize_nulls(df, as_markdown=True)
    
#print("\n🕳️ **Missing Values Summary:**")    
def summarize_missingness(df, logger=None, threshold=0.0, as_markdown=True):
    """
    Summarize missingness in a DataFrame.

    Args:
        df (pd.DataFrame): The dataframe to analyze.
        logger (logging.Logger, optional): Logger for recording results.
        threshold (float): Minimum percentage of missingness to include in the report.
        as_markdown (bool): Whether to print summary as a markdown-style block.

    Returns:
        pd.DataFrame: Summary of columns with missing data.
    """
    total_rows = len(df)
    missing = df.isnull().sum()
    percent_missing = 100 * missing / total_rows
    missing_summary = pd.DataFrame({
        "missing_count": missing,
        "missing_percent": percent_missing
    }).query("missing_count > 0")

    if threshold > 0:
        missing_summary = missing_summary[missing_summary["missing_percent"] >= threshold]

    missing_summary = missing_summary.sort_values(by="missing_percent", ascending=False)

    if logger:
        logger.info("🕳️ Missing Data Summary:\n" + missing_summary.to_string())

    if as_markdown:
        print("\n🕳️ **Missing Values Summary:**\n")
        for col, row in missing_summary.iterrows():
            print(f"- {col:<20}: {row['missing_count']:>5,.0f} missing ({row['missing_percent']:>5.1f}%)")
    else:
        print(missing_summary)

    return missing_summary

def standardize_and_flag_categorical(df, column, valid_values=None, unknown_label="UNKNOWN", logger=None):
    """
    Cleans a categorical column, adds a *_missing flag, and replaces NaNs or invalids with 'UNKNOWN'.

    Args:
        df (pd.DataFrame): The DataFrame.
        column (str): Name of the column to standardize.
        valid_values (iterable, optional): Accepted values (case-insensitive). If None, no filtering.
        unknown_label (str): Label to use for unknowns.
        logger (Logger, optional): Logger for tracking steps.

    Returns:
        pd.DataFrame: DataFrame with [column]_clean and [column]_missing added.
    """
    col_clean = f"{column}_clean"
    col_missing = f"{column}_missing"

    # Flag original NaNs
    df[col_missing] = df[column].isna()

    # Standardize values
    df[col_clean] = df[column].where(df[column].notna(), None)
    df[col_clean] = df[col_clean].apply(lambda x: str(x).strip().upper() if pd.notnull(x) else x)

    # Replace invalids
    if valid_values:
        valid_upper = set(v.upper() for v in valid_values)
        df[col_clean] = df[col_clean].apply(lambda x: x if x in valid_upper else unknown_label)
    else:
        df[col_clean] = df[col_clean].fillna(unknown_label)

    # Logging
    if logger:
        logger.info(f"🧼 Cleaned '{column}': {df[col_missing].sum()} missing → '{unknown_label}'")
        logger.info(f"🔎 '{col_clean}' distribution:\n{df[col_clean].value_counts().to_string()}")

    return df
def summarize_categorical_insights(
    df,
    columns,
    include_missing=True,
    include_cardinality=True,
    include_top_values=True,
    validation_plan=None,
    logger=None
):
    """
    Summarizes missingness, unique value counts, and distribution skew for given categorical columns.
    Optionally, audits for unexpected categorical values using a validation plan.

    Args:
        df (pd.DataFrame): The dataset to analyze.
        columns (list of str): List of categorical columns to summarize.
        include_missing (bool): Whether to include/report missingness summary.
        include_cardinality (bool): Whether to include/report unique counts.
        include_top_values (bool): Whether to include/report skew/top value frequencies.
        validation_plan (dict, optional): Mapping of columns to expected categories for unexpected value audit.
        logger (Logger, optional): Logger for logging (optional).

    Returns:
        dict: Dictionary containing DataFrames for the computed summaries and unexpected value audit (if any).
    """
    from tabulate import tabulate

    results = {}

    # 0. Unexpected category audit
    if validation_plan:
        unexpected_summary = summarize_unexpected_categories(df, validation_plan, logger=logger)
        if unexpected_summary:
            print("\n⚠️ Unexpected Category Values (Not in Validation Plan):")
            unexpected_table = [(col, ", ".join(vals)) for col, vals in unexpected_summary.items()]
            print(tabulate(unexpected_table, headers=["Column", "Unexpected Values"], tablefmt="pretty"))
        else:
            print("\n✅ All columns matched expected categories.")
        results["unexpected_values"] = unexpected_summary

    print("\n🧪 Categorical Summary Report")

    # 1. Missingness Rate
    if include_missing:
        missingness = {
            col: (df[col].isna().sum() + (df[col] == "UNKNOWN").sum()) / len(df) * 100
            for col in columns
        }
        missingness_df = pd.DataFrame.from_dict(missingness, orient="index", columns=["Missing %"]).round(2)
        print("\n✅ Missingness Rate (%):\n")
        print(tabulate(missingness_df, headers='keys', tablefmt='pretty'))
        results["missingness"] = missingness_df

    # 2. Unique Category Counts (Raw vs Clean)
    if include_cardinality:
        unique_counts = {
            col: {
                "Unique (Raw)": df[col].nunique(dropna=False),
                "Unique (Clean)": df.get(f"{col}_clean", df[col]).nunique(dropna=False)
            }
            for col in columns
        }
        unique_df = pd.DataFrame.from_dict(unique_counts, orient="index")
        print("\n🔢 Unique Category Counts (Raw vs Clean):\n")
        print(tabulate(unique_df, headers='keys', tablefmt='pretty'))
        results["unique_counts"] = unique_df

    # 3. Distribution Skew (Top 3 Frequencies)
    if include_top_values:
        skew_info = {}
        for col in columns:
            if col in df.columns:
                top_values = df[col].value_counts(normalize=True, dropna=False).head(3).round(3)
                skew_info[col] = top_values.to_dict()
        skew_df = pd.DataFrame(skew_info).fillna("")
        print("\n📊 Top 3 Value Distributions (Skew Check):\n")
        print(tabulate(skew_df, headers='keys', tablefmt='pretty'))
        results["skew"] = skew_df

    return results
def extract_date_labels(df, column, prefix=None, logger=None):
    """
    Cleans and extracts date labels from a datetime column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        column (str): The datetime column to process.
        prefix (str, optional): Optional prefix for new columns. If None, uses column name without '_date' suffix.
        logger (Logger, optional): Logger for status messages.

    Returns:
        pd.DataFrame: Modified DataFrame with [prefix]_date_clean, _year, and _year_label columns.
    """
    prefix = prefix or column.replace("_date", "")

    if column not in df.columns:
        if logger:
            logger.warning(f"⚠️ Column '{column}' not found in DataFrame.")
        return df

    df[column] = pd.to_datetime(df[column], errors="coerce")
    df[f"{prefix}_date_clean"] = df[column].dt.strftime("%Y-%m-%d").fillna("UNKNOWN")
    df[f"{prefix}_year"] = df[column].dt.year.astype("Int64")
    df[f"{prefix}_year_label"] = df[f"{prefix}_year"].astype(str).replace("<NA>", "UNKNOWN")

    if logger:
        logger.info(f"📆 Created '{prefix}_date_clean', '{prefix}_year', and '{prefix}_year_label' columns")

    return df
def summarize_unexpected_categories(df, validation_plan, logger=None):
    """
    Identifies unexpected values in categorical columns based on a validation plan.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        validation_plan (dict): Mapping of column names to sets of expected values.
        logger (Logger, optional): Logger for warnings/info.

    Returns:
        dict: Dictionary with unexpected values by column.
    """
    unexpected_summary = {}

    for col, expected in validation_plan.items():
        if col not in df.columns:
            if logger:
                logger.warning(f"⚠️ Column '{col}' not found in DataFrame.")
            continue

        actual_values = df[col].dropna().astype(str).str.upper().unique()
        unexpected = sorted(set(actual_values) - set(expected))
        if unexpected:
            unexpected_summary[col] = unexpected
            if logger:
                logger.warning(f"⚠️ Unexpected values in '{col}': {unexpected}")
        else:
            if logger:
                logger.info(f"✅ No unexpected values in '{col}'.")

    return unexpected_summary