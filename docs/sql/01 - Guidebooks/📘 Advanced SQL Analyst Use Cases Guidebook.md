---
🎯 Purpose

This guidebook provides **battle-tested, advanced analyst SQL patterns** for real-world production and investigative workflows: LTV segmentation, behavioral funnel drop-off, anomaly detection, and stacked cohort-layered metrics.

---

## 📊 1. Multi-Step Funnel Drop-Off with Delta Metrics

```sql
WITH base AS (
  SELECT user_id,
         MIN(CASE WHEN event = 'visit' THEN event_time END) AS visited,
         MIN(CASE WHEN event = 'signup' THEN event_time END) AS signed_up,
         MIN(CASE WHEN event = 'purchase' THEN event_time END) AS purchased
  FROM events
  GROUP BY user_id
),
funnel AS (
  SELECT COUNT(*) AS visited_count,
         COUNT(signed_up) AS signup_count,
         COUNT(purchased) AS purchase_count
  FROM base
)
SELECT *,
       ROUND(100.0 * signup_count / visited_count, 2) AS signup_rate,
       ROUND(100.0 * purchase_count / signup_count, 2) AS purchase_rate
FROM funnel;
```

✔️ Captures user-level funnel timing and step conversion rate

---

## 🧠 2. Rolling Retention with Sliding Window

```sql
WITH daily_events AS (
  SELECT user_id, DATE(event_time) AS event_date
  FROM events
),
cohorts AS (
  SELECT user_id, MIN(event_date) AS cohort_day
  FROM daily_events
  GROUP BY user_id
),
activity AS (
  SELECT e.user_id, c.cohort_day, e.event_date,
         DATE_PART('day', e.event_date - c.cohort_day) AS days_since_signup
  FROM daily_events e
  JOIN cohorts c ON e.user_id = c.user_id
)
SELECT cohort_day,
       days_since_signup,
       COUNT(DISTINCT user_id) AS retained_users
FROM activity
GROUP BY cohort_day, days_since_signup;
```

✔️ Builds retention matrix across cohorts by signup day

---

## 📈 3. Behavioral Segmentation via Event Combinations

```sql
SELECT user_id,
       CASE
         WHEN COUNT(DISTINCT CASE WHEN event = 'purchase' THEN 1 END) > 0 AND
              COUNT(DISTINCT CASE WHEN event = 'return' THEN 1 END) > 0 THEN 'churn-risk'
         WHEN COUNT(DISTINCT CASE WHEN event = 'purchase' THEN 1 END) > 2 THEN 'power-user'
         ELSE 'casual'
       END AS segment
FROM events
GROUP BY user_id;
```

✔️ Tag behavioral patterns from event logs

---

## 🧾 4. Anomaly Detection Using Z-Scores

```sql
WITH daily_agg AS (
  SELECT DATE(event_time) AS day, COUNT(*) AS events
  FROM events
  GROUP BY day
),
stats AS (
  SELECT AVG(events) AS mean, STDDEV(events) AS stddev FROM daily_agg
)
SELECT d.*,
       ROUND((events - mean) / stddev, 2) AS z_score,
       CASE WHEN ABS((events - mean) / stddev) > 3 THEN 'outlier' ELSE 'normal' END AS status
FROM daily_agg d, stats;
```

✔️ Flag traffic or event anomalies using statistical deviation

---

## 📉 5. Cross-Slice LTV Comparison

```sql
WITH ltv_raw AS (
  SELECT user_id, region, SUM(amount) AS total_spend
  FROM orders
  GROUP BY user_id, region
),
avg_ltv AS (
  SELECT region, ROUND(AVG(total_spend), 2) AS avg_ltv
  FROM ltv_raw
  GROUP BY region
)
SELECT * FROM avg_ltv ORDER BY avg_ltv DESC;
```

✔️ Stack regions, cohorts, or source channels to compare performance

---

## ✅ Advanced Patterns This Covers

* Multi-path funnels & rate breakdowns
* Layered cohort retention logic
* Dynamic behavior classification
* Outlier flagging at interval level
* Grouped performance benchmarking

---

## 💡 Tip

> “Advanced SQL means more than syntax — it’s knowing how to reshape messy, transactional data into clear decision-ready insight.”
