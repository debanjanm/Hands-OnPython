-- 08. Constraints & Keys
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 08-Constraints-And-Keys.sql
--
-- Topics in this file:
--   01. PRIMARY KEY - INTEGER PRIMARY KEY is a rowid alias
--   02. FOREIGN KEY - PRAGMA foreign_keys = ON is required to enforce them
--   03. UNIQUE
--   04. CHECK
--   05. NOT NULL
--   06. CREATE INDEX + EXPLAIN QUERY PLAN

.headers on
.mode column

-- 01. PRIMARY KEY - INTEGER PRIMARY KEY is a rowid alias
-- ------------------------------------
-- - Every SQLite table (unless declared WITHOUT ROWID) has a hidden 64-bit
--   signed integer rowid column.
-- - A column declared exactly `INTEGER PRIMARY KEY` becomes an ALIAS for
--   that rowid - it's not a separate value. This is why it auto-increments
--   on its own (picks max(existing)+1) and why lookups by it are the
--   fastest possible (direct rowid access, not a b-tree index lookup).
-- - Gotcha: `INTEGER PRIMARY KEY` is special-cased; `BIGINT PRIMARY KEY` or
--   a composite PRIMARY KEY does NOT get this rowid-alias behavior - it
--   becomes a normal (indexed) column/constraint instead.

CREATE TABLE departments (
    dept_id    INTEGER PRIMARY KEY,   -- rowid alias: auto-increments, fastest lookup
    dept_name  TEXT NOT NULL
);

INSERT INTO departments (dept_name) VALUES ('Engineering');  -- dept_id omitted
INSERT INTO departments (dept_name) VALUES ('Sales');

SELECT '-- 01. dept_id auto-assigned via rowid aliasing (no explicit value given)' AS section;
-- Note dept_id and rowid come back under the SAME column name below - proof
-- they are literally the same underlying value, not just kept in sync.
SELECT dept_id, dept_name, rowid AS "same_as_dept_id (rowid)" FROM departments;

-- 02. FOREIGN KEY - needs PRAGMA foreign_keys = ON
-- ------------------------------------
-- - SQLite parses FOREIGN KEY constraints but does NOT enforce them by
--   default, for backward compatibility. Enforcement must be turned on
--   PER CONNECTION with `PRAGMA foreign_keys = ON;` (it is off by default
--   even in recent SQLite versions).

CREATE TABLE employees (
    emp_id     INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    dept_id    INTEGER REFERENCES departments(dept_id)
);

SELECT '-- 02a. foreign_keys pragma is OFF by default' AS section;
PRAGMA foreign_keys;

SELECT '-- 02b. WITHOUT enforcement: inserting a bogus dept_id 999 silently succeeds' AS section;
INSERT INTO employees (emp_id, first_name, dept_id) VALUES (1, 'Ghost', 999);
SELECT * FROM employees;
DELETE FROM employees WHERE emp_id = 1;  -- clean up the bad row before turning enforcement on

PRAGMA foreign_keys = ON;

SELECT '-- 02c. WITH enforcement: the same bad insert now raises FOREIGN KEY constraint failed' AS section;
-- Wrapped so the deliberate failure doesn't abort this whole script; SQLite
-- itself would raise here - this demonstrates it without exiting non-zero.
.mode list
SELECT 'Expected error on the next statement, caught by app-level error handling in real code:' AS note;
.mode column

-- (This would raise: "FOREIGN KEY constraint failed")
-- INSERT INTO employees (emp_id, first_name, dept_id) VALUES (2, 'Ghost2', 999);

SELECT '-- 02d. A VALID foreign key insert still works fine with enforcement on' AS section;
INSERT INTO employees (emp_id, first_name, dept_id) VALUES (3, 'Alice', 1);
SELECT * FROM employees;

-- 03. UNIQUE
-- ------------------------------------
-- - Enforces that no two rows share the same value in the constrained
--   column(s). Unlike PRIMARY KEY, a UNIQUE column CAN hold NULL - and
--   SQLite treats multiple NULLs as all distinct from each other (they
--   don't violate uniqueness against one another).

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    email      TEXT UNIQUE
);

INSERT INTO accounts (email) VALUES ('a@example.com');
INSERT INTO accounts (email) VALUES (NULL);
INSERT INTO accounts (email) VALUES (NULL);  -- allowed: NULLs are not "equal" to each other

SELECT '-- 03. UNIQUE allows multiple NULLs, blocks duplicate non-NULL values' AS section;
SELECT * FROM accounts;

-- 04. CHECK
-- ------------------------------------
-- - A row-level boolean expression that must be TRUE (or NULL) for every
--   row - lets the database itself enforce domain rules instead of relying
--   on application code (recall file 01's TEXT-in-a-REAL-column gotcha -
--   CHECK is one real defense against that class of bug).

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    price      REAL NOT NULL CHECK (price >= 0)
);

INSERT INTO products (price) VALUES (19.99);

SELECT '-- 04. CHECK-constrained table accepts valid data' AS section;
SELECT * FROM products;
-- (This would raise: "CHECK constraint failed: products")
-- INSERT INTO products (price) VALUES (-5);

-- 05. NOT NULL
-- ------------------------------------
-- - Rejects any INSERT/UPDATE that would leave the column NULL. Combine
--   with DEFAULT to supply an automatic fallback instead of erroring.

CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY,
    title   TEXT NOT NULL,
    status  TEXT NOT NULL DEFAULT 'open'
);

INSERT INTO tasks (title) VALUES ('Write SQL curriculum');

SELECT '-- 05. NOT NULL column filled via DEFAULT when omitted' AS section;
SELECT * FROM tasks;
-- (This would raise: "NOT NULL constraint failed: tasks.title")
-- INSERT INTO tasks (title) VALUES (NULL);

-- 06. CREATE INDEX + EXPLAIN QUERY PLAN
-- ------------------------------------
-- - An index is a separate on-disk structure that lets SQLite find rows by
--   a column's value without scanning every row (a "full table scan").
-- - EXPLAIN QUERY PLAN shows, without running it, how SQLite intends to
--   execute a query - "SCAN" means row-by-row full scan, "SEARCH ... USING
--   INDEX" means it used an index to jump straight to matching rows.

CREATE TABLE big_lookup (
    id    INTEGER PRIMARY KEY,
    email TEXT
);
INSERT INTO big_lookup (email)
    SELECT 'user' || value || '@example.com' FROM generate_series(1, 500);

SELECT '-- 06a. Before an index: full table SCAN on email' AS section;
EXPLAIN QUERY PLAN SELECT * FROM big_lookup WHERE email = 'user250@example.com';

CREATE INDEX idx_big_lookup_email ON big_lookup(email);

SELECT '-- 06b. After CREATE INDEX: SEARCH using the new index' AS section;
EXPLAIN QUERY PLAN SELECT * FROM big_lookup WHERE email = 'user250@example.com';
