___
## 🎯 Purpose

This guidebook helps analysts design SQL that flows cleanly into **dashboards or BI tools** like Looker Studio. It focuses on writing performant, readable queries that produce stable, shareable, and visualization-ready outputs.

---

## 🧱 1. Use Views or Saved Queries

| Reason                 | Benefit                                                 |
| ---------------------- | ------------------------------------------------------- |
| Reusable logic         | Don't repeat joins, filters, or groupings in dashboards |
| Pre-aggregation        | Reduces dashboard lag + query costs                     |
| Easier version control | Track in Git or docs                                    |

### 🧪 Best Practice

```sql
CREATE OR REPLACE VIEW clean_dashboard_metrics AS
SELECT
  DATE(event_date) AS date,
  region,
  COUNT(DISTINCT user_id) AS active_users,
  SUM(spend) AS total_revenue
FROM project.dataset.raw_events
WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY date, region;
```

---

## 🔍 2. Column Naming Conventions

| Pattern             | Example                             |
| ------------------- | ----------------------------------- |
| snake\_case         | `total_users`, `avg_order_value`    |
| readable dimensions | `region`, `channel`, `cohort_month` |
| metric clarity      | `revenue_usd`, `session_count`      |

✔️ Avoid ambiguous labels like `value`, `amount`, `type`

---

## 📊 3. Output Shape by Dashboard Type

| Dashboard Layer | SQL Output                              |
| --------------- | --------------------------------------- |
| KPI Cards       | One row per date or region with metrics |
| Trend Charts    | Time series format (date + metric)      |
| Cohort Tables   | cohort\_id + time\_step + value         |
| Tables          | Clean, joined, deduplicated flat format |

---

## 🧪 4. Aggregation Strategy

| Recommendation       | Why                          |
| -------------------- | ---------------------------- |
| Pre-aggregate in SQL | Faster, simpler dashboards   |
| Apply CASE for flags | Easy to chart segment slices |
| Create bucket fields | For histogram/facet charts   |

```sql
CASE
  WHEN spend > 1000 THEN 'high spender'
  WHEN spend > 100 THEN 'moderate'
  ELSE 'low'
END AS spender_segment
```

---

## ⛔ 5. Where *Not* to Filter in SQL

| Filter Type                              | Apply In SQL?                             |
| ---------------------------------------- | ----------------------------------------- |
| Security filter (e.g. internal only)     | ✅ Yes                                     |
| Dashboard dropdown filter (e.g. channel) | ❌ No (Let dashboard do it)                |
| Date scoping (fixed vs dynamic)          | ⚠️ SQL for heavy views, UI for user needs |

---

## 🗂️ 6. Export-Ready Tips

| Format            | Tool                                        |
| ----------------- | ------------------------------------------- |
| `.csv`            | Use for snapshots, simple metrics           |
| `.json`           | For API-pull dashboards or audit logs       |
| Materialized View | Fastest dashboard backend                   |
| Temp Table        | Testing only — don’t use in prod dashboards |

---

## ✅ Dashboard Pipeline Checklist

* [ ] SQL view created and named cleanly
* [ ] Column names readable and scoped to dashboard
* [ ] Output shaped by dashboard (KPI/trend/table)
* [ ] Pre-aggregation, flags, CASE fields added
* [ ] Filters pushed to dashboard unless business-critical
* [ ] Export tested for `.csv` or view refresh

---

## 💡 Tip

> “Dashboards shouldn’t decode SQL logic — SQL should deliver dashboard-ready answers.”
