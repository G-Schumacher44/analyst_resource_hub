___
## 🎯 Purpose

This guidebook outlines a production-aligned, modular workflow for analysts who combine **SQL + Python in notebooks**. It emphasizes separation of logic, reproducibility, and efficient transitions between data querying, EDA, and modeling.

---

## 🧱 1. Use SQL to Prepare — Not Model

| Use SQL For        | Avoid Doing in SQL         |
| ------------------ | -------------------------- |
| Joins + filtering  | Full-feature normalization |
| Pre-aggregation    | Custom feature generation  |
| Cohorting, funnels | Modeling or residual logic |
| Deduplication      | Outlier transformations    |

✔️ SQL should stage structured, clean inputs — leave exploration for Python

---

## 🔄 2. Pulling SQL into Python

### 🔹 BigQuery Example

```python
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()
query = """
    SELECT user_id, event_date, spend
    FROM project.dataset.transactions
    WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
"""
df = client.query(query).to_dataframe()
```

### 🔹 Postgres or Snowflake Example (via SQLAlchemy)

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://user:password@host/db")
df = pd.read_sql("SELECT * FROM users", engine)
```

---

## 🧪 3. Notebook Structure for Analytics

```text
[ Cell 1: Imports ]
[ Cell 2: SQL Query or Data Import ]
[ Cell 3: Initial sanity checks (df.head(), df.info()) ]
[ Cell 4: EDA — value_counts, describe(), histograms ]
[ Cell 5: Cleaning — nulls, dtypes, mapping ]
[ Cell 6: Feature generation ]
[ Cell 7: Modeling or export ]
```

✔️ Use markdown cells to label each phase clearly
✔️ Save query text in markdown cell or `.sql` file for versioning

---

## 🧹 4. SQL View + Python Transform Pattern

> Use SQL to stage a **view** and Python to finish the analysis.

### SQL View Example:

```sql
-- Create a view in BigQuery or DB
CREATE OR REPLACE VIEW cohort_summary AS
SELECT cohort_month, days_since_signup, COUNT(*) AS retained_users
FROM raw.events
GROUP BY 1, 2;
```

### Python:

```python
df = client.query("SELECT * FROM cohort_summary").to_dataframe()
sns.lineplot(data=df, x="days_since_signup", y="retained_users", hue="cohort_month")
```

---

## 🛠️ 5. Best Practices

* Use **parameterized queries** to dynamically fetch different timeframes
* Store SQL queries in separate `.sql` files or markdown cells
* Version-control final notebooks, but treat exploration as flexible
* Use `.query()` or `.loc[]` with readable filters (`df[df["country"] == "US"]`)

---

## ✅ SQL + Python Workflow Checklist

* [ ] Data pulled from SQL using tested/staged view or saved query
* [ ] Notebook includes import, structure, and EDA cells
* [ ] SQL only handles structural prep (joins, filters, grouping)
* [ ] Python handles flexible EDA, feature work, plotting
* [ ] Comments and markdown explain workflow clearly

---

## 💡 Tip

> “Write SQL like a database engineer. Explore like a scientist. Ship notebooks like a product analyst.”
