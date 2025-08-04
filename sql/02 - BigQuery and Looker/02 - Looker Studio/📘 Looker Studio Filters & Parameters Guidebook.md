___
## 🎯 Purpose

This guidebook explains how to use **filters, controls, and parameters** in Looker Studio (Data Studio) to create interactive dashboards with dynamic user input, cross-chart filtering, and calculated field flexibility.

---

## 🧭 1. Filter Types in Looker Studio

| Filter Type                     | Purpose                                                 |
| ------------------------------- | ------------------------------------------------------- |
| Date range filter               | Global or per-chart control of time windows             |
| Dimension filter (dropdown)     | Select categories like region, channel, segment         |
| Chart-level filter              | Narrow filter on single visualization (override global) |
| Filter control with search      | Allows searching values in dropdowns                    |
| Hidden filter (default applied) | Applied silently for scoped views                       |

✔️ Filters can apply globally (top of report), to a page, or individual chart

---

## 🧮 2. Parameter Controls

Parameters allow dashboard users to enter **custom input values** that can influence calculations or filtering.

### 🔹 Example Use Cases

* Input revenue goal to calculate pacing
* Choose currency multiplier or exchange rate
* Toggle flag field (0/1) to turn on/off visuals or fields

### 🔹 Creating a Parameter

1. Create parameter → name, data type, default value
2. Bind parameter to a calculated field
3. Add input control to dashboard (text box, dropdown, slider)

### 🔹 Parameter Example (Pacing Goal)

```text
Parameter: user_goal (type: number)
Calculated field:
  % to Goal = SUM(revenue) / user_goal
```

---

## 🛠️ 3. Best Practices for Filters & Parameters

| Practice                             | Why                                                        |
| ------------------------------------ | ---------------------------------------------------------- |
| Always label filter controls clearly | Users should understand what they’re changing              |
| Use consistent naming                | Avoid filter mismatch across pages or tabs                 |
| Test filter cascading                | Ensure segment filters don’t hide all data unintentionally |
| Combine with calculated fields       | Dynamic % changes, toggles, conditional formatting         |
| Avoid over-filtering small datasets  | Reduces empty visuals, improves performance                |

---

## 🧪 4. Use Cases in Analyst Dashboards

* Campaign performance filter by source, UTM, or platform
* Funnel by product category, date range, or region
* Retention dashboards with month selector
* Executive dashboards with KPI toggles (e.g., by channel)
* QA dashboards with date sliders and debug flags

---

## ✅ Filter/Parameter Design Checklist

* [ ] Date filter defaults to relevant time window
* [ ] Category filters scoped to relevant charts/pages
* [ ] Parameters bound to clear calculations or visuals
* [ ] All controls labeled and positioned with intention
* [ ] Tested for edge cases (nulls, empty filters)

---

## 💡 Tip

> “Great dashboards feel interactive — filters and parameters are how users *ask questions* without touching SQL.”
