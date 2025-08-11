___
🎯 Purpose

This guidebook expands your SQL skillset with intermediate-to-advanced techniques: **window functions**, **CTEs**, **subqueries**, **CASE logic**, **date math**, and **analytics-friendly patterns**.

---

## 🪟 1. Window Functions

### 🔹 ROW\_NUMBER / RANK / DENSE\_RANK

```sql
SELECT user_id,
       signup_date,
       RANK() OVER (PARTITION BY region ORDER BY signup_date) AS regional_rank
FROM users;
```

✔️ Use to find top-N per group, tie-breakers, or recency

### 🔹 LAG / LEAD

```sql
SELECT user_id,
       event_date,
       LAG(event_date) OVER (PARTITION BY user_id ORDER BY event_date) AS prev_event
FROM events;
```

✔️ Useful for session tracking, churn windows, retention

### 🔹 SUM / AVG OVER WINDOW

```sql
SELECT user_id,
       revenue,
       SUM(revenue) OVER (PARTITION BY user_id ORDER BY event_date) AS cumulative_revenue
FROM orders;
```

---

## 🧱 2. CTEs (Common Table Expressions)

```sql
WITH recent_orders AS (
  SELECT *
  FROM orders
  WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT customer_id, COUNT(*)
FROM recent_orders
GROUP BY customer_id;
```

✔️ Improves readability, allows modular queries

---

## 🔍 3. Subqueries

### 🔹 Inline Scalar

```sql
SELECT id, (SELECT MAX(score) FROM scores WHERE user_id = u.id) AS top_score
FROM users u;
```

### 🔹 Derived Tables

```sql
SELECT region, AVG(spend)
FROM (
  SELECT region, user_id, SUM(amount) AS spend
  FROM transactions
  GROUP BY region, user_id
) t
GROUP BY region;
```

---

## 📅 4. Date + Time Functions

```sql
-- Extract month from timestamp
SELECT EXTRACT(MONTH FROM signup_date) AS signup_month

-- Date difference in days
SELECT DATE_PART('day', CURRENT_DATE - signup_date) AS days_since_signup
```

✔️ Use `DATE_TRUNC`, `EXTRACT`, `DATE_DIFF`, `INTERVAL`, `NOW()` as needed

---

## 🧠 5. Advanced CASE Patterns

```sql
SELECT user_id,
       CASE
         WHEN spend > 1000 THEN 'high'
         WHEN spend > 100 THEN 'mid'
         ELSE 'low'
       END AS segment
FROM user_totals;
```

✔️ Often used with windows, bins, and funnel logic

---

## 📈 6. Percentile + Quantile Logic

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY revenue) AS median_revenue
FROM orders;
```

✔️ Use for medians, quartiles, decile bucketing

---

## ✅ Analyst Use Cases

* Rank cohorts by conversion or spend
* Calculate LTV or retention windows
* Create derived metrics with `WITH` blocks
* Build funnel or session-based tracking

---

## 💡 Tip

> “CTEs + windows = SQL superpowers. Learn them once, reuse them forever.”
