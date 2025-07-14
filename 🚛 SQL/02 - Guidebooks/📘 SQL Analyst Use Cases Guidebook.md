___
🎯 Purpose

This guidebook focuses on **practical SQL patterns** used to solve real-world analytics problems — especially for retention, churn, funnel analysis, cohorts, and customer metrics.

---

## 🧍‍♂️ 1. Retention & Churn Tracking

### 🔹 Active/Inactive Labeling

```sql
SELECT user_id,
       MAX(event_date) AS last_seen,
       CASE WHEN MAX(event_date) >= CURRENT_DATE - INTERVAL '30 days'
            THEN 'active'
            ELSE 'churned' END AS status
FROM events
GROUP BY user_id;
```

### 🔹 Retention Cohort Table

```sql
WITH signup_cohort AS (
  SELECT user_id,
         DATE_TRUNC('month', MIN(signup_date)) AS cohort_month
  FROM users
  GROUP BY user_id
),
activity AS (
  SELECT user_id,
         DATE_TRUNC('month', event_date) AS activity_month
  FROM events
)
SELECT cohort_month,
       activity_month,
       COUNT(DISTINCT activity.user_id) AS retained_users
FROM signup_cohort
JOIN activity USING (user_id)
GROUP BY 1, 2;
```

---

## 📈 2. Funnel Analysis

### 🔹 Step-Based Funnel

```sql
WITH base AS (
  SELECT user_id,
         MIN(CASE WHEN event = 'view' THEN event_time END) AS view_time,
         MIN(CASE WHEN event = 'signup' THEN event_time END) AS signup_time,
         MIN(CASE WHEN event = 'purchase' THEN event_time END) AS purchase_time
  FROM events
  GROUP BY user_id
)
SELECT
  COUNT(DISTINCT user_id) AS total,
  COUNT(DISTINCT signup_time) AS signed_up,
  COUNT(DISTINCT purchase_time) AS purchased
FROM base;
```

---

## 👥 3. Cohort Metrics

### 🔹 LTV by Cohort

```sql
WITH cohorts AS (
  SELECT user_id,
         DATE_TRUNC('month', signup_date) AS cohort_month
  FROM users
),
revenue AS (
  SELECT user_id,
         SUM(revenue) AS lifetime_value
  FROM orders
  GROUP BY user_id
)
SELECT cohort_month,
       AVG(lifetime_value) AS avg_ltv
FROM cohorts
JOIN revenue USING (user_id)
GROUP BY cohort_month;
```

---

## 💰 4. Revenue & Conversion Metrics

### 🔹 Conversion by Segment

```sql
SELECT marketing_channel,
       COUNT(DISTINCT user_id) AS total_users,
       COUNT(DISTINCT CASE WHEN converted THEN user_id END) AS conversions,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN converted THEN user_id END) /
                   COUNT(DISTINCT user_id), 2) AS conversion_rate
FROM user_profiles
GROUP BY marketing_channel;
```

---

## ✅ Use Cases You Can Adapt

* Trial → paid conversion, upgrade funnels
* Day 1 / 7 / 30 retention by cohort
* LTV tracking across regions or segments
* Campaign or channel attribution

---

## 💡 Tip

> “The best SQL queries for analytics aren’t clever — they’re *repeatable, explainable, and outcome-focused*.”
