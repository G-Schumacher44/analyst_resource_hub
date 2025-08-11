___
## 🎯 Purpose

This guidebook expands your BigQuery fluency with advanced features: **ARRAYs**, **STRUCTs**, **UNNEST**, **ARRAY\_AGG**, `WITH OFFSET`, nested joins, and multi-level aggregation logic — all commonly found in GA4, Firebase, and modern analytics tables.

---

## 🧺 1. Working with ARRAYs

### 🔹 UNNEST an array

```sql
SELECT user_id, item
FROM `project.dataset.orders`, UNNEST(items) AS item;
```

✔️ Required when querying arrays or GA4-style events

### 🔹 Count array elements

```sql
SELECT user_id, ARRAY_LENGTH(items) AS item_count
FROM orders;
```

---

## 🏗️ 2. STRUCTs and Nested Fields

### 🔹 Access nested STRUCT fields

```sql
SELECT
  user_info.name AS name,
  user_info.address.city AS city
FROM users;
```

✔️ Common in event data, especially user/device metadata

### 🔹 STRUCTs inside ARRAYs

```sql
SELECT
  user_id,
  product.name AS product_name
FROM orders, UNNEST(products) AS product;
```

✔️ Use dot notation after UNNEST

---

## 🧮 3. ARRAY\_AGG + Deduplication

### 🔹 Collect items into an array

```sql
SELECT user_id, ARRAY_AGG(item) AS items
FROM purchases
GROUP BY user_id;
```

### 🔹 Deduplicate with DISTINCT

```sql
SELECT user_id, ARRAY_AGG(DISTINCT item) AS unique_items
FROM purchases
GROUP BY user_id;
```

---

## 🔢 4. WITH OFFSET (Indexing Inside Arrays)

```sql
SELECT
  user_id,
  interest,
  offset AS interest_rank
FROM users,
UNNEST(interests) WITH OFFSET AS offset;
```

✔️ Useful for top-N ranking within flattened fields

---

## 🪜 5. Nested Aggregations (2-Level)

```sql
-- Example: most purchased item per user
WITH item_counts AS (
  SELECT user_id, item, COUNT(*) AS cnt
  FROM orders
  GROUP BY user_id, item
),
ranked AS (
  SELECT *,
         RANK() OVER (PARTITION BY user_id ORDER BY cnt DESC) AS rnk
  FROM item_counts
)
SELECT *
FROM ranked
WHERE rnk = 1;
```

✔️ Use CTEs + RANK to simulate FIRST\_VALUE or top-1 logic

---

## 📚 6. Flattened Event Table Tips

| Feature                          | Tip                                                 |
| -------------------------------- | --------------------------------------------------- |
| `event_params` is an ARRAY       | Use `UNNEST(event_params)` and filter by `key`      |
| `user_properties` are nested     | Use `UNNEST()` + dot notation + OFFSET if needed    |
| Always filter large arrays early | Apply `WHERE` clause **after** UNNEST or inside CTE |

---

## ✅ Patterns Covered

* Querying nested and repeated fields (ARRAY + STRUCT)
* Flattening GA4-style event schemas
* Aggregating inside groups
* Simulating top-1 selection with `RANK()`

---

## 💡 Tip

> “In BigQuery, flat queries break fast. Nested logic + UNNEST is the key to modeling modern event data.”
