___
🎯 Purpose

This guidebook teaches analysts how to use **Looker Studio (formerly Data Studio)** for creating **interactive dashboards** powered by **BigQuery**, with a focus on best practices for filters, layout, speed, and interpretation.

---

## 🔌 1. Connect to BigQuery

* Use "BigQuery" as your data source
* Navigate through project → dataset → table or custom query
* Recommended: **use a VIEW or saved query** to control logic outside Looker

✔️ Helps reduce dashboard load time and manage logic externally

---

## 🧱 2. Set Up a Reusable Dataset

* Use **a table or view with pre-filtered, pre-aggregated data**
* Include clear field names and calculated fields (like conversion\_rate, retention\_day, etc.)
* Avoid raw event-level logs if not needed

```sql
-- Ideal for Looker: Pre-aggregated metrics
SELECT cohort_month, days_since_signup, retained_users FROM my_project.my_dataset.cohort_summary;
```

---

## 📊 3. Core Visualization Types

| Chart        | Use Case                                  |
| ------------ | ----------------------------------------- |
| Scorecards   | KPIs like DAU, revenue, churn rate        |
| Time Series  | Trend tracking over days/weeks/months     |
| Bar + Column | Channel comparison, cohort volume         |
| Pie / Donut  | Share by segment or category              |
| Pivot Table  | Category breakdown over time or dimension |
| Tables       | Underlying drill-down for raw views       |

✔️ Add comparison metrics (vs previous period, % change)

---

## 🧭 4. Filters, Controls, and UX

| Feature                 | Notes                                                   |
| ----------------------- | ------------------------------------------------------- |
| Date Range Picker       | Add global or chart-level selectors                     |
| Dropdown Filter         | Segment by user type, region, channel                   |
| Custom Calculated Field | Build ratios or conditional flags inline                |
| Chart Filter            | Use filter controls on single charts for targeted views |

✔️ Label everything — filters, legends, and axis titles must be clear for stakeholders

---

## 🧪 5. Design Best Practices

* Group related metrics together (use layout grids)
* Color consistently across views (same colors for channels, statuses)
* Show last updated timestamp
* Use bold scorecards at top for high-priority KPIs
* Avoid overloading pages with too many visuals

---

## 📤 6. Sharing, Export, and Embedding

* Dashboards can be shared via Google permissions or public links
* Charts and tables can be exported (CSV, PDF)
* Embed dashboards in docs, sites, or email reports

---

## ✅ Dashboard Readiness Checklist

* [ ] Connected to clean BigQuery view or stable table
* [ ] Visual layout groups KPIs and trends logically
* [ ] Filters and dropdowns are intuitive and labeled
* [ ] Date ranges are consistent and default correctly
* [ ] Charts include legends, axis labels, and titles
* [ ] Dashboard optimized for speed (pre-aggregated views)

---

## 💡 Tip

> “Looker dashboards should answer questions at a glance — if it takes more than 10 seconds to explain, simplify it.”
