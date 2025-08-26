# 📘 SQL Getting Started Guide

This guide is for absolute beginners. It covers the most common SQL clauses that form the foundation of nearly every query you'll write, including how to combine data from multiple tables.

---

## 🎯 Purpose

To provide a clear, simple introduction to the core building blocks of SQL. Use this as your very first step before diving into more complex topics.

---

## 🧱 The Core Building Blocks

A standard SQL query follows a logical order. Think of it as building a sentence to ask your database a question.

```sql
SELECT   -- What columns do you want to see?
FROM     -- Which table is the data in?
JOIN     -- What other table should be linked?
WHERE    -- How do you want to filter the rows?
GROUP BY -- How should you aggregate the data?
ORDER BY -- In what order should the results be?
LIMIT    -- How many rows should be returned?
```

---

### 1. `SELECT` and `FROM`

These are the only two mandatory clauses. `SELECT` specifies the columns you want, and `FROM` specifies the table they live in.

| Task                               | Example Query                               |
| ---------------------------------- | ------------------------------------------- |
| Get all columns from a table       | `SELECT * FROM customers;`                  |
| Get specific columns from a table  | `SELECT first_name, email FROM customers;`  |
| Rename a column in the output      | `SELECT order_id, amount AS order_value FROM orders;` |

✔️ **Tip:** Using `*` is great for exploration, but in production, always list the specific columns you need. It's more efficient and predictable.

---

### 2. `LIMIT`

The `LIMIT` clause restricts the number of rows returned by your query. It's perfect for peeking at a table without fetching all the data.

| Task                               | Example Query                               |
| ---------------------------------- | ------------------------------------------- |
| Get the first 10 rows from a table | `SELECT * FROM customers LIMIT 10;`         |

✔️ **Tip:** Always use `LIMIT` when exploring large tables to save time and resources. It's usually one of the last clauses in a query.

---

### 3. `WHERE`

The `WHERE` clause filters your data to only include rows that meet a certain condition.

| Task                               | Example Query                                     |
| ---------------------------------- | ------------------------------------------------- |
| Filter for a specific value        | `SELECT * FROM products WHERE category = 'Books';` |
| Filter based on a number           | `SELECT * FROM orders WHERE amount > 100;`        |
| Combine multiple conditions        | `SELECT * FROM users WHERE country = 'USA' AND last_seen > '2024-01-01';` |

✔️ **Tip:** You can use operators like `=`, `!=`, `>`, `<`, `>=`, `<=`, `IN`, `LIKE`, and `BETWEEN`.

---

### 4. `JOIN`s

Most of the time, the data you need is split across multiple tables. `JOIN`s are used to combine rows from two or more tables based on a related column between them.

| Join Type     | Purpose                                                 | Example Query                                           |
| ------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `INNER JOIN`  | Returns only the rows where the join key exists in *both* tables. | `SELECT * FROM customers c JOIN orders o ON c.id = o.customer_id;` |
| `LEFT JOIN`   | Returns *all* rows from the left table, and matched rows from the right. | `SELECT * FROM customers c LEFT JOIN orders o ON c.id = o.customer_id;` |

✔️ **Tip:** `LEFT JOIN` is great for finding things that *don't* have a match. For example, finding all customers who have never placed an order.

---

### 5. `GROUP BY`

The `GROUP BY` clause is used with aggregate functions (like `COUNT`, `SUM`, `AVG`) to group rows that have the same values in specified columns into summary rows.

| Task                               | Example Query                                     |
| ---------------------------------- | ------------------------------------------------- |
| Count orders per customer          | `SELECT customer_id, COUNT(order_id) FROM orders GROUP BY customer_id;` |
| Calculate total sales per category | `SELECT category, SUM(sales) FROM products GROUP BY category;` |

✔️ **Tip:** Any column in your `SELECT` statement that isn't an aggregate function *must* be in your `GROUP BY` clause.

---

### 6. `ORDER BY`

The `ORDER BY` clause sorts the final result set in ascending (`ASC`) or descending (`DESC`) order.

| Task                               | Example Query                                     |
| ---------------------------------- | ------------------------------------------------- |
| Sort products by price (low to high) | `SELECT * FROM products ORDER BY price ASC;`      |
| Sort users by signup date (newest first) | `SELECT * FROM users ORDER BY signup_date DESC;` |

✔️ **Tip:** `ASC` is the default, so you can omit it. For descending order, you must specify `DESC`.

---

## 🧩 Putting It All Together

Here’s a complete query that uses all of these clauses to find the total sales for each product category, but only for orders placed in the USA. It then shows the top 10 highest-selling categories first.

```sql
-- Find the total sales for each product category in the USA
SELECT
    p.category,
    SUM(o.order_amount) AS total_sales
FROM
    orders AS o
INNER JOIN
    products AS p ON o.product_id = p.id
WHERE
    o.country = 'USA'
GROUP BY
    p.category
ORDER BY
    total_sales DESC
LIMIT 10;
```

This query answers a specific business question by combining filtering, aggregation, and sorting. Master these five clauses, and you're well on your way to writing powerful SQL!