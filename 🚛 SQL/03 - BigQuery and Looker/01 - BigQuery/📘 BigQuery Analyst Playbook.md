___
## 🎯 Purpose

A tactical guide for analysts using Google BigQuery in day-to-day querying, metric extraction, and dashboard support. Includes shortcuts, reusable query patterns, and production-aware habits.

---

## 📥 1. Data Access Patterns

### 🔹 Reference Table

```sql
SELECT column1, column2
FROM `project.dataset.table`
WHERE _PARTITIONTIME >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);
```

### 🔹 Query Preview (Dry Run)

```sql
-- In the UI: enable 'Dry Run' to preview bytes scanned
```

✔️ Helps avoid accidental large scans

### 🔹 Schema Inspection

```sql
SELECT *
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'your_table';
```

---

## 📊 2. KPI Snapshot Query Template

```sql
SELECT
  CURRENT_DATE() AS snapshot_date,
  COUNT(DISTINCT user_id) AS active_users,
  SUM(revenue) AS total_revenue
FROM `project.dataset.transactions`
WHERE event_date = CURRENT_DATE();
```

✔️ Useful for dashboards and automated tracking

---

## 🧮 3. Partition-Aware Aggregates

```sql
SELECT DATE(event_timestamp) AS event_day,
       COUNT(*) AS events
FROM `project.dataset.events`
WHERE _PARTITIONTIME BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) AND CURRENT_DATE()
GROUP BY event_day
ORDER BY event_day;
```

✔️ Partition filters reduce scan cost dramatically

---

## 🧱 4. Modular Query with CTEs

```sql
WITH daily AS (
  SELECT user_id, DATE(event_time) AS day
  FROM `project.dataset.events`
),
user_counts AS (
  SELECT day, COUNT(DISTINCT user_id) AS daily_active_users
  FROM daily
  GROUP BY day
)
SELECT * FROM user_counts ORDER BY day;
```

✔️ CTEs make logic testable and reusable

---

## 🧪 5. Debugging & Exploratory Tools

```sql
-- Preview 1k rows from partitioned slice
SELECT *
FROM `project.dataset.users`
WHERE _PARTITIONTIME >= '2023-01-01'
LIMIT 1000;

-- Find nulls in column
SELECT COUNT(*) FROM table WHERE column IS NULL;

-- Find unexpected values
SELECT column, COUNT(*) FROM table GROUP BY column;
```

---

## ✅ Analyst Workflow Checklist

* [ ] Verified query uses partitions (or limits scope)
* [ ] Column list scoped (no `SELECT *` in prod)
* [ ] Used CTEs or temp tables for clarity
* [ ] Checked bytes scanned before running heavy queries
* [ ] Documented assumptions or filters (esp. for handoff or dashboard)

---

## 💡 Tip

> “Use BigQuery like a cloud-based warehouse, not a spreadsheet. Modular SQL beats megasheets every time.”
