# `SQL.py`

```python
from pandas_gbq import read_gbq

def query_bigquery_dataset(
    project_id: str,
    dataset: str,
    table: str,
    fields: list = None,
    where_clause: str = "",
    rename_map: dict = None
) -> "pd.DataFrame":
    """
    General-purpose BigQuery query utility.

    Parameters:
        project_id (str): Your GCP project ID
        dataset (str): BigQuery dataset name or full dataset path including project ID (e.g., "bigquery-public-data.ml_datasets")
        table (str): Table name within the dataset
        fields (list, optional): List of fields to select (default: all)
        where_clause (str, optional): Optional SQL WHERE clause without 'WHERE'
        rename_map (dict, optional): Dictionary to rename columns after pull

    Returns:
        pd.DataFrame: A DataFrame containing the queried result
    """
    selected_fields = ", ".join(fields) if fields else "*"
    where_sql = f"WHERE {where_clause}" if where_clause else ""

    query = f"""
    SELECT {selected_fields}
    FROM `{dataset}.{table}`
    {where_sql}
    """
    df = read_gbq(query, project_id=project_id, use_bqstorage_api=False)

    if rename_map:
        df.rename(columns=rename_map, inplace=True)

    return df
```