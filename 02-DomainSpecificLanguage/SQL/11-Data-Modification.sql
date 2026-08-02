-- 11. Data Modification
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 11-Data-Modification.sql
--
-- Topics in this file:
--   01. UPDATE (with WHERE, multi-column)
--   02. DELETE (with WHERE)
--   03. INSERT ... ON CONFLICT DO UPDATE (upsert)
--   04. ALTER TABLE ADD COLUMN - and SQLite's limited ALTER TABLE

.headers on
.mode column

CREATE TABLE products (
    sku      TEXT PRIMARY KEY,
    name     TEXT NOT NULL,
    price    REAL NOT NULL,
    stock    INTEGER NOT NULL DEFAULT 0
);

INSERT INTO products (sku, name, price, stock) VALUES
    ('SKU-1', 'Widget',  9.99, 100),
    ('SKU-2', 'Gadget', 19.99, 50),
    ('SKU-3', 'Gizmo',  29.99, 0);

-- 01. UPDATE
-- ------------------------------------
-- - WHERE scopes which rows change - an UPDATE with no WHERE touches EVERY
--   row, a common and costly mistake. Always run the equivalent SELECT
--   first to sanity-check which rows will be affected.
-- - Multiple columns can be set in one UPDATE, comma-separated.

SELECT '-- 01a. Before UPDATE' AS section;
SELECT * FROM products;

UPDATE products
SET price = 24.99, stock = 40   -- multi-column update
WHERE sku = 'SKU-2';

SELECT '-- 01b. After UPDATE: only SKU-2 changed (price and stock together)' AS section;
SELECT * FROM products;

-- 02. DELETE
-- ------------------------------------
-- - Same WHERE-scoping caution as UPDATE - DELETE FROM table with no WHERE
--   removes every row (but keeps the table/schema itself, unlike DROP TABLE).

DELETE FROM products WHERE stock = 0;

SELECT '-- 02. DELETE: out-of-stock SKU-3 removed' AS section;
SELECT * FROM products;

-- 03. INSERT ... ON CONFLICT DO UPDATE (upsert)
-- ------------------------------------
-- - "Insert this row, but if it already conflicts with a UNIQUE/PRIMARY
--   KEY constraint, update the existing row instead" - one statement,
--   avoids a separate SELECT-then-branch round trip.
-- - `excluded.column` refers to the value that WOULD have been inserted,
--   letting you reference it inside the DO UPDATE clause.

SELECT '-- 03a. Upsert an existing SKU: price/stock updated, name untouched' AS section;
INSERT INTO products (sku, name, price, stock) VALUES ('SKU-1', 'Widget', 8.49, 120)
ON CONFLICT (sku) DO UPDATE SET price = excluded.price, stock = excluded.stock;
SELECT * FROM products WHERE sku = 'SKU-1';

SELECT '-- 03b. Upsert a new SKU: no conflict, behaves like a plain INSERT' AS section;
INSERT INTO products (sku, name, price, stock) VALUES ('SKU-4', 'Doohickey', 4.99, 200)
ON CONFLICT (sku) DO UPDATE SET price = excluded.price, stock = excluded.stock;
SELECT * FROM products ORDER BY sku;

-- 04. ALTER TABLE ADD COLUMN - and SQLite's limited ALTER TABLE
-- ------------------------------------
-- - SQLite's ALTER TABLE supports only a handful of operations: RENAME TO,
--   RENAME COLUMN, ADD COLUMN, and (since 3.35.0, 2021) DROP COLUMN.
-- - Before 3.35.0, dropping a column required the classic workaround:
--   create a new table without the column, copy the data across, drop the
--   old table, rename the new one - still the only option for changes
--   ALTER TABLE doesn't support directly (e.g. changing a column's type,
--   adding/removing constraints on an existing column).
-- - ADD COLUMN requirements: the new column can't be PRIMARY KEY or UNIQUE,
--   and if NOT NULL, it must have a non-NULL DEFAULT (existing rows need a
--   value to backfill).

ALTER TABLE products ADD COLUMN category TEXT NOT NULL DEFAULT 'Uncategorized';

SELECT '-- 04a. ADD COLUMN: existing rows backfilled with the DEFAULT' AS section;
SELECT * FROM products ORDER BY sku;

-- DROP COLUMN, available since SQLite 3.35.0 (2021-03) - older SQLite
-- versions need the "create new table, copy, drop, rename" workaround
-- described above instead.
ALTER TABLE products DROP COLUMN category;

SELECT '-- 04b. DROP COLUMN (3.35+): category column gone' AS section;
SELECT * FROM products ORDER BY sku;
