-- 12. Normalization & Design
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 12-Normalization-And-Design.sql
--
-- This file is mostly comment-driven - it explains 1NF/2NF/3NF, then
-- builds a concrete BEFORE (denormalized) schema and an AFTER (normalized)
-- schema for the same data, so the difference is runnable, not just prose.
--
-- Topics in this file:
--   01. 1NF - First Normal Form
--   02. 2NF - Second Normal Form
--   03. 3NF - Third Normal Form
--   04. BEFORE - one wide denormalized table
--   05. AFTER - split into normalized tables with foreign keys
--   06. Comparing query results between BEFORE and AFTER

.headers on
.mode column

-- 01. 1NF - First Normal Form
-- ------------------------------------
-- - Every column holds a single, atomic value - no comma-separated lists,
--   no repeating groups of columns (like product_1, product_2, product_3).
-- - Every row is uniquely identifiable (has a primary key).
-- - A column storing "Widget,Gadget,Gizmo" as one string violates 1NF -
--   it's hiding a one-to-many relationship inside a single cell.

-- 02. 2NF - Second Normal Form
-- ------------------------------------
-- - Must already be in 1NF.
-- - Every non-key column depends on the WHOLE primary key, not just part
--   of it. Only matters with a composite (multi-column) primary key - if
--   a column depends on only one part of the key, it's a 2NF violation.
-- - Example: a table keyed on (order_id, product_id) storing customer_name
--   violates 2NF, because customer_name depends only on order_id, not on
--   product_id too.

-- 03. 3NF - Third Normal Form
-- ------------------------------------
-- - Must already be in 2NF.
-- - No TRANSITIVE dependencies: a non-key column must depend on the
--   primary key directly, not on another non-key column.
-- - Example: storing both dept_id and dept_name on an employees row -
--   dept_name depends on dept_id, not on emp_id directly (change the
--   department's name, and it would need updating on every employee row
--   that copied it) - a transitive dependency, and a 3NF violation.

-- 04. BEFORE - one wide denormalized table
-- ------------------------------------
-- - order_id + product_sku would be the natural composite key, but
--   customer_name/customer_email depend only on order_id (2NF violation),
--   and product_name/unit_price depend only on product_sku, not on the
--   full (order_id, product_sku) pair (also a 2NF violation).
-- - Data duplication: customer_email and product_name repeat on every
--   line that shares an order or a product - update anomaly risk (fixing
--   a customer's typo'd email means updating N rows, and might miss one,
--   leaving inconsistent copies of "the same" fact).

CREATE TABLE orders_wide (
    order_id       INTEGER NOT NULL,
    product_sku    TEXT    NOT NULL,
    customer_name  TEXT    NOT NULL,   -- depends only on order_id
    customer_email TEXT    NOT NULL,   -- depends only on order_id
    product_name   TEXT    NOT NULL,   -- depends only on product_sku
    unit_price     REAL    NOT NULL,   -- depends only on product_sku
    quantity       INTEGER NOT NULL,   -- depends on the full (order_id, product_sku) pair
    PRIMARY KEY (order_id, product_sku)
);

INSERT INTO orders_wide (order_id, product_sku, customer_name, customer_email, product_name, unit_price, quantity) VALUES
    (1, 'SKU-1', 'Alice', 'alice@example.com', 'Widget', 9.99,  2),
    (1, 'SKU-2', 'Alice', 'alice@example.com', 'Gadget', 19.99, 1),
    (2, 'SKU-1', 'Bob',   'bob@example.com',   'Widget', 9.99,  5);
    -- Notice: 'Alice'/'alice@example.com' duplicated across order 1's two
    -- lines, and 'Widget'/9.99 duplicated across orders 1 and 2.

SELECT '-- 04. BEFORE: denormalized - customer and product facts repeated per line' AS section;
SELECT * FROM orders_wide ORDER BY order_id, product_sku;

-- 05. AFTER - split into normalized tables with foreign keys
-- ------------------------------------
-- - customers: one row per customer - customer_email lives in exactly ONE
--   place now.
-- - products: one row per product - product_name/unit_price live in
--   exactly ONE place.
-- - orders: one row per order, referencing its customer.
-- - order_items: one row per (order, product) line, referencing both -
--   this is the table that actually needs the composite relationship;
--   quantity correctly depends on the full (order_id, product_sku) pair.
-- - Now updating a customer's email or a product's price is a single-row
--   UPDATE, with no risk of missed/inconsistent duplicates.

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
    sku        TEXT PRIMARY KEY,
    name       TEXT NOT NULL,
    unit_price REAL NOT NULL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_id    INTEGER NOT NULL REFERENCES orders(order_id),
    product_sku TEXT    NOT NULL REFERENCES products(sku),
    quantity    INTEGER NOT NULL,
    PRIMARY KEY (order_id, product_sku)
);

INSERT INTO customers (customer_id, name, email) VALUES
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob',   'bob@example.com');

INSERT INTO products (sku, name, unit_price) VALUES
    ('SKU-1', 'Widget', 9.99),
    ('SKU-2', 'Gadget', 19.99);

INSERT INTO orders (order_id, customer_id) VALUES
    (1, 1),   -- Alice's order
    (2, 2);   -- Bob's order

INSERT INTO order_items (order_id, product_sku, quantity) VALUES
    (1, 'SKU-1', 2),
    (1, 'SKU-2', 1),
    (2, 'SKU-1', 5);

SELECT '-- 05. AFTER: normalized tables - each fact stored exactly once' AS section;
SELECT '-- customers' AS table_name;
SELECT * FROM customers;
SELECT '-- products' AS table_name;
SELECT * FROM products;
SELECT '-- orders' AS table_name;
SELECT * FROM orders;
SELECT '-- order_items' AS table_name;
SELECT * FROM order_items ORDER BY order_id, product_sku;

-- 06. Comparing query results between BEFORE and AFTER
-- ------------------------------------
-- - The same question - "line items with customer and product details" -
--   is a single SELECT against orders_wide, but requires joining 4 tables
--   in the normalized version. That extra JOIN is normalization's real
--   cost, paid at query time in exchange for update-time safety - a
--   trade-off, not a free win, which is why heavily-read/rarely-written
--   reporting tables are sometimes deliberately denormalized.

SELECT '-- 06a. BEFORE: one flat table, no joins needed' AS section;
SELECT customer_name, product_name, quantity, unit_price
FROM orders_wide
ORDER BY order_id, product_sku;

SELECT '-- 06b. AFTER: same result, reconstructed via joins across 4 tables' AS section;
SELECT c.name AS customer_name, p.name AS product_name, oi.quantity, p.unit_price
FROM order_items oi
JOIN orders o     ON oi.order_id = o.order_id
JOIN customers c  ON o.customer_id = c.customer_id
JOIN products p   ON oi.product_sku = p.sku
ORDER BY oi.order_id, oi.product_sku;
