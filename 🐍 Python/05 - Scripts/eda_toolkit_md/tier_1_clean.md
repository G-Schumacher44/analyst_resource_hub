# `tier_1_clean.py`

```python
#Tier 1 Data Cleaning Functions

def fix_typos_cat_column(df, column, output_column=None, fixes=None, logger=None):
    """
    Generic cleaner for categorical columns with known typos or variations.

    Returns:
        tuple: (updated DataFrame, number of values changed)
    """
    changed_count = 0
    target = output_column or column

    # Ensure working on a copy of the DataFrame to avoid side effects
    df = df.copy()
    df[target] = df[column].str.upper().str.strip()

    if fixes:
        before = df[target].copy()
        df[target] = df[target].replace(fixes)
        changed_count = (before != df[target]).sum()

        if logger:
            logger.info(f"🧼 Applied categorical corrections on '{column}': {fixes}")
            logger.info(f"📊 Summary: {changed_count} values changed in '{target}'")

    return df, changed_count
```