-- 07. Window Functions
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 07-Window-Functions.sql
--
-- Topics in this file:
--   01. OVER() basics - window functions vs GROUP BY
--   02. ROW_NUMBER()
--   03. RANK() / DENSE_RANK()
--   04. LAG() / LEAD()
--   05. Running totals with SUM() OVER (ORDER BY ... ROWS BETWEEN ...)
--   06. PARTITION BY

.headers on
.mode column

CREATE TABLE orders (
    order_id     INTEGER PRIMARY KEY,
    salesperson  TEXT NOT NULL,
    region       TEXT NOT NULL,
    order_date   TEXT NOT NULL,
    amount       REAL NOT NULL
);

INSERT INTO orders (order_id, salesperson, region, order_date, amount) VALUES
    (1, 'Carla', 'West', '2026-01-05', 500),
    (2, 'Carla', 'West', '2026-01-12', 800),
    (3, 'Carla', 'West', '2026-01-20', 800),   -- tie with order 2, for RANK demo
    (4, 'Dev',   'West', '2026-01-08', 300),
    (5, 'Dev',   'West', '2026-01-15', 650),
    (6, 'Eve',   'East', '2026-01-03', 400),
    (7, 'Eve',   'East', '2026-01-18', 900);

-- 01. OVER() basics - window functions vs GROUP BY
-- ------------------------------------
-- - GROUP BY collapses many rows into one row per group.
-- - A window function (any function followed by OVER (...)) keeps EVERY
--   row, but computes its result using a "window" of related rows -
--   here, every row still gets its own amount AND the overall total.

SELECT '-- 01. OVER() with no partition: total is repeated on every row' AS section;
SELECT order_id, salesperson, amount, SUM(amount) OVER () AS grand_total
FROM orders
ORDER BY order_id;

-- 02. ROW_NUMBER()
-- ------------------------------------
-- - Assigns a strictly increasing, unique integer per row within its
--   window, in the order given by ORDER BY - ties still get distinct
--   numbers (arbitrarily broken).

SELECT '-- 02. ROW_NUMBER() over all orders by amount descending' AS section;
SELECT order_id, salesperson, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num
FROM orders
ORDER BY row_num;

-- 03. RANK() / DENSE_RANK()
-- ------------------------------------
-- - RANK(): ties share the same rank, but the NEXT rank skips ahead by the
--   number of tied rows (1, 2, 2, 4, ...).
-- - DENSE_RANK(): ties share the same rank, and the next rank is always
--   +1 with no gap (1, 2, 2, 3, ...).

SELECT '-- 03. RANK vs DENSE_RANK: Carla''s orders 2 and 3 tie at 800' AS section;
SELECT order_id, salesperson, amount,
       RANK()       OVER (ORDER BY amount DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rnk
FROM orders
ORDER BY amount DESC;

-- 04. LAG() / LEAD()
-- ------------------------------------
-- - LAG(col, n): value from n rows BEFORE the current row (default n=1).
-- - LEAD(col, n): value from n rows AFTER the current row.
-- - Both return NULL when there's no such row (start/end of the window) -
--   handy for period-over-period comparisons without a self-join.

SELECT '-- 04. LAG/LEAD per salesperson, ordered by date: compare to prev/next order' AS section;
SELECT salesperson, order_date, amount,
       LAG(amount)  OVER (PARTITION BY salesperson ORDER BY order_date) AS prev_amount,
       LEAD(amount) OVER (PARTITION BY salesperson ORDER BY order_date) AS next_amount
FROM orders
ORDER BY salesperson, order_date;

-- 05. Running totals (ROWS BETWEEN)
-- ------------------------------------
-- - The frame clause (ROWS BETWEEN ... AND ...) controls exactly which
--   rows contribute to each row's aggregate.
-- - UNBOUNDED PRECEDING AND CURRENT ROW = "every row so far" -> classic
--   running total.

SELECT '-- 05. Running total of amount per salesperson, ordered by date' AS section;
SELECT salesperson, order_date, amount,
       SUM(amount) OVER (
           PARTITION BY salesperson
           ORDER BY order_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM orders
ORDER BY salesperson, order_date;

-- 06. PARTITION BY
-- ------------------------------------
-- - Divides rows into independent groups (partitions) BEFORE applying the
--   window function - each partition is computed separately, like a
--   GROUP BY that doesn't collapse rows. Already used above (04, 05); here
--   it's isolated with RANK() to show per-region ranking.

SELECT '-- 06. PARTITION BY region: rank each order within its own region' AS section;
SELECT region, salesperson, amount,
       RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rank_in_region
FROM orders
ORDER BY region, rank_in_region;
