___
## 🎯 Purpose

This guidebook covers foundational SQL skills for analysts — focusing on querying, filtering, joining, grouping, and handling common data types and null logic.

---

## 1️⃣ SELECT and Filtering

### 🔹 Basic Query

```sql
SELECT column1, column2
FROM table_name;
```

### 🔹 WHERE Clause

```sql
SELECT *
FROM users
WHERE age >= 18 AND status = 'active';
```

* Use `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, and `LIKE` as needed

### 🔹 ORDER BY

```sql
ORDER BY created_at DESC;
```

### 🔹 LIMIT (Top N Rows)

```sql
LIMIT 10;
```

---

## 2️⃣ JOINs (Core Tool for Analysts)

### 🔹 INNER JOIN

```sql
SELECT u.id, o.order_id
FROM users u
JOIN orders o ON u.id = o.user_id;
```

* Returns only matching rows between both tables

### 🔹 LEFT JOIN

```sql
SELECT u.id, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

* Includes all users, even those with no orders (NULL-filled)

### 🔹 FULL OUTER JOIN

* Includes all rows from both tables
* Note: Not all SQL dialects support this join type.

### 🔹 SELF JOIN

* A table joined to itself, useful for hierarchical data like user referral networks.
```sql
SELECT a.name, b.name AS referred_by
FROM users a
JOIN users b ON a.referred_by = b.id;
```

---

## 3️⃣ GROUP BY + Aggregations

### 🔹 Basic GROUP BY

```sql
SELECT status, COUNT(*)
FROM users
GROUP BY status;
```

### 🔹 HAVING Clause (Filter post-aggregation)

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;
```

### 🔹 Common Aggregates

* `COUNT(*)`, `SUM()`, `AVG()`, `MAX()`, `MIN()`

---

## 4️⃣ Null Handling

### 🔹 COALESCE (Fallback value)

```sql
SELECT COALESCE(email, 'missing@example.com') AS email_cleaned
FROM users;
```

### 🔹 IS NULL / IS NOT NULL

```sql
WHERE deleted_at IS NULL
```

---

## 5️⃣ CASE Statements

```sql
SELECT
  user_id,
  CASE
    WHEN score >= 90 THEN 'gold'
    WHEN score >= 70 THEN 'silver'
    ELSE 'bronze'
  END AS tier
FROM scores;
```

* Useful for tiering, segmentation, conditional logic

---

## 6️⃣ Set Operators (UNION, INTERSECT, EXCEPT)

Set operators combine the results of two or more `SELECT` statements into a single result set. The columns in each `SELECT` must have the same number of columns and compatible data types.

| Operator      | Purpose                                                              | Example Query                                            |
| ------------- | -------------------------------------------------------------------- | -------------------------------------------------------- |
| `UNION`       | Combines results and removes duplicate rows.                         | `SELECT email FROM list_a UNION SELECT email FROM list_b;`      |
| `UNION ALL`   | Combines results but **keeps** all duplicate rows. Faster.           | `SELECT email FROM list_a UNION ALL SELECT email FROM list_b;`  |
| `INTERSECT`   | Returns only the rows that appear in **both** result sets.           | `SELECT id FROM group_a INTERSECT SELECT id FROM group_b;`      |
| `EXCEPT`      | Returns rows from the first query that are **not** in the second.    | `SELECT id FROM all_users EXCEPT SELECT id FROM banned_users;`  |

✔️ **Tip:** `UNION ALL` is almost always preferred over `UNION` unless you specifically need to deduplicate, as it avoids the performance cost of the duplicate check.

---

## ✅ Analyst Use Cases This Covers

* Pulling raw data for EDA
* Segmenting users, orders, or events
* Counting or ranking behaviors (signup, conversion)
* Filtering production tables for modeling
* Combining historical and current data from different tables
* Finding common records between two datasets (`INTERSECT`)
* Creating exclusion lists (`EXCEPT`)

---

## 💡 Tip

> “Most analysis starts with SELECT. Master joins, filters, and groups — everything else builds from there.”
