___
🎯 Purpose

This guidebook explains how to design SQL logic specifically for **use in dashboards** like Looker Studio. It focuses on the pipeline from raw table → clean view → dashboard-ready layer — balancing clarity, performance, and stakeholder usability.

---

## 🧱 1. Build Views, Not Ad-Hoc Queries

> Always stage logic into **views** or **saved queries** in BigQuery.

### 🔹 Why?

| Benefit        | Description                                      |
| -------------- | ------------------------------------------------ |
| ✅ Reusability  | Avoid rewriting logic across dashboards          |
| ✅ Auditability | Easy to QA inputs + test changes                 |
| ✅ Performance  | Pre-filters and aggregates reduce dashboard load |

```sql
-- GOOD: Save this as a view
CREATE OR REPLACE VIEW project.dataset.kpi_snapshot AS
SELECT
  CURRENT_DATE() AS snapshot_date,
  COUNT(DISTINCT user_id) AS active_users,
  SUM(revenue) AS total_revenue
FROM raw.events
WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY);
```

---

## 🧹 2. Clean Column Names for Business Use

> Rename fields in your SQL to match business language — not dev column names.

| Dev Field | Rename To      |
| --------- | -------------- |
| `cust_id` | `customer_id`  |
| `ord_amt` | `order_amount` |
| `dt`      | `event_date`   |

✔️ Use snake\_case or camelCase, but stay **consistent**.

---

## 🧮 3. Pre-Aggregate What You Can

> Summarize at the level your dashboard needs — not row-level data unless required.

### Examples:

| Dashboard View    | SQL Shape                             |
| ----------------- | ------------------------------------- |
| KPI cards         | 1 row with COUNT, SUM, AVG            |
| Retention chart   | Cohort ID, days\_since\_signup, count |
| Revenue by region | Region, total\_revenue                |

```sql
SELECT channel, COUNT(*) AS users, SUM(revenue) AS revenue
FROM raw.sessions
GROUP BY channel;
```

---

## 🧪 4. Use Snapshots for Time-Stamped Metrics

> Dashboards work best with stable, reproducible values. Use timestamped snapshot tables.

```sql
-- Daily snapshot
INSERT INTO project.dataset.kpi_snapshots
SELECT CURRENT_DATE(), COUNT(*), SUM(revenue)
FROM ...
```

✔️ Use for daily exec dashboards, trendlines, pacing metrics

---

## 🛠️ 5. Handle Nulls & Types Carefully

* Use `IFNULL()` or `COALESCE()` to prevent blank chart rows
* Use `SAFE_CAST()` to avoid runtime errors in Looker Studio

```sql
SELECT
  COALESCE(region, 'unknown') AS region,
  SAFE_CAST(revenue AS FLOAT64) AS revenue
FROM cleaned.events;
```

---

## 🧩 6. Apply Filters in SQL or in Looker — But Not Both

| Filter Type                | Best Location                                   |
| -------------------------- | ----------------------------------------------- |
| Security or access filters | ✅ SQL (hardcoded or policy-based)               |
| UX dropdowns, toggles      | ✅ Looker Studio (dashboard filter)              |
| Date scoping               | ✅ SQL for performance, Looker for interactivity |

✔️ Don’t apply the same filter in both places unless required

---

## ✅ SQL-to-Dashboard Pipeline Checklist

* [ ] Views created for each dashboard component
* [ ] Column names clean and business-friendly
* [ ] Logic tested separately before Looker use
* [ ] Aggregations scoped to use case (KPI vs trend vs table)
* [ ] Snapshots added for time-based reports
* [ ] Nulls and types safely handled for visual output

---

## 💡 Tip

> “Dashboards don’t need clever SQL — they need stable, testable views that give people answers fast.”
