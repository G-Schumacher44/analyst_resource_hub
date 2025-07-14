# `validation.py`

```python
import logging
import pandas as pd

def validate_schema(df, schema=None):
    """
    Validate DataFrame schema or log the detected schema.

    Args:
        df (pd.DataFrame): Input DataFrame.
        schema (dict or None): Expected schema in the form {'column_name': dtype}.
            If None, logs the detected schema without raising errors.

    Returns:
        bool: True if schema matches, logs detected schema otherwise.
    """
    if schema is None:
        detected_schema = detect_schema(df)
        logging.warning("No schema provided. Detected schema logged for reference.")
        return True

    for column, dtype in schema.items():
        if column not in df.columns:
            logging.error(f"Missing column: {column}")
            raise ValueError(f"Missing column: {column}")
        
        # Check for exact or compatible data types
        if not pd.api.types.is_dtype_equal(df[column].dtype, dtype):
            # Allow int64 if float64 is expected
            if dtype == 'float64' and pd.api.types.is_integer_dtype(df[column].dtype):
                continue
            # Allow other compatible cases if needed
            logging.error(f"Column '{column}' has incorrect type. Expected {dtype}, got {df[column].dtype}.")
            raise ValueError(f"Column '{column}' has incorrect type. Expected {dtype}, got {df[column].dtype}.")
    
    logging.info("Schema validation passed.")
    return True



def detect_schema(df):
    """
    Automatically detect the schema of a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        dict: Detected schema in the form {'column_name': dtype}.
    """
    detected_schema = {col: str(df[col].dtype) for col in df.columns}
    logging.info(f"Detected schema: {detected_schema}")
    return detected_schema


def validate_column_ranges(df, column_ranges=None):
    """
    Validate that columns fall within specified ranges, or log detected ranges.

    Args:
        df (pd.DataFrame): Input DataFrame.
        column_ranges (dict or None): Expected ranges in the form {'column_name': (min, max)}.
            If None, logs detected ranges without raising errors.

    Returns:
        bool: True if columns fall within ranges, logs detected ranges otherwise.
    """
    if column_ranges is None:
        detected_ranges = detect_column_ranges(df)
        logging.warning("No column ranges provided. Detected ranges logged for reference.")
        return True

    for column, (min_val, max_val) in column_ranges.items():
        if column not in df.columns:
            logging.error(f"Missing column: {column}")
            raise ValueError(f"Missing column: {column}")
        if not df[column].between(min_val, max_val).all():
            logging.error(f"Column '{column}' contains values outside the range ({min_val}, {max_val}).")
            raise ValueError(f"Column '{column}' contains values outside the range ({min_val}, {max_val}).")
    logging.info("Column range validation passed.")
    return True


def detect_column_ranges(df):
    """
    Automatically detect min and max ranges for each numeric column.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        dict: Ranges for numeric columns in the form {'column_name': (min, max)}.
    """
    numeric_columns = df.select_dtypes(include=['number'])
    ranges = {col: (df[col].min(), df[col].max()) for col in numeric_columns}
    logging.info(f"Detected column ranges: {ranges}")
    return ranges


def remove_duplicates(df, subset=None, keep='first', log_details=True, save_removed=False):
    """
    Remove duplicate rows from the DataFrame with detailed logging and options.

    Args:
        df (pd.DataFrame): Input DataFrame.
        subset (list or None): Columns to consider for duplicate detection. If None, consider all columns.
        keep (str): Which duplicates to keep. Options: 'first', 'last', False (drop all duplicates).
        log_details (bool): Whether to log detailed information about duplicates.
        save_removed (bool): Whether to save removed duplicates to a separate file.

    Returns:
        pd.DataFrame: DataFrame with duplicates removed.
    """
    if subset and not all(col in df.columns for col in subset):
        raise ValueError("One or more columns in `subset` are not in the DataFrame.")

    initial_count = len(df)
    duplicates = df[df.duplicated(subset=subset, keep=keep)]

    if duplicates.empty:
        logging.warning("No duplicates detected. No rows removed.")
        return df

    if save_removed:
        duplicates.to_csv('removed_duplicates.csv', index=False)
        logging.info(f"Saved {len(duplicates)} removed duplicate rows to 'removed_duplicates.csv'.")

    df = df.drop_duplicates(subset=subset, keep=keep)
    duplicates_removed = initial_count - len(df)

    if log_details:
        subset_columns = subset if subset else "all columns"
        logging.info(
            f"remove_duplicates: Removed {duplicates_removed} duplicate rows based on {subset_columns}. Kept rows: {keep}."
        )

    return df

def validate_data(df, config):
    """
    Validate a DataFrame using schema and column range configuration.
 
    Args:
        df (pd.DataFrame): The DataFrame to validate.
        config (dict): Configuration dictionary. Keys:
            - schema: dict of expected dtypes {'column': 'dtype'}
            - column_ranges: dict of allowed ranges {'column': (min, max)}
            - datetime_columns: list of columns to convert to datetime
            - strip_column_whitespace: bool
            - strict: bool (if True, raise errors; if False, log warnings)
 
    Returns:
        bool: True if validations pass, otherwise raises/logs errors.
    """
    strict = config.get("strict", True)

    # Strip whitespace from column names
    if config.get("strip_column_whitespace", True):
        df.columns = df.columns.str.strip()

    # Convert specified columns to datetime
    datetime_cols = config.get("datetime_columns", [])
    for col in datetime_cols:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception as e:
                msg = f"Failed to convert '{col}' to datetime: {e}"
                if strict:
                    raise ValueError(msg)
                else:
                    logging.warning(msg)

    # Schema validation
    if "schema" in config:
        try:
            validate_schema(df, config["schema"])
        except Exception as e:
            if strict:
                raise
            else:
                logging.warning(f"Schema validation warning: {e}")

    # Range validation
    if "column_ranges" in config:
        try:
            validate_column_ranges(df, config["column_ranges"])
        except Exception as e:
            if strict:
                raise
            else:
                logging.warning(f"Column range validation warning: {e}")

    return True

```