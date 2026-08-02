-- 10. Views & Query Plans
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 10-Views-And-Query-Plans.sql
--
-- Topics in this file:
--   01. CREATE VIEW
--   02. Querying a view like a table
--   03. DROP VIEW
--   04. EXPLAIN QUERY PLAN revisited on a join - index vs full scan

.headers on
.mode column

CREATE TABLE departments (
    dept_id   INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id     INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    dept_id    INTEGER NOT NULL,
    salary     REAL NOT NULL
);

INSERT INTO departments (dept_id, dept_name) VALUES
    (1, 'Engineering'), (2, 'Sales'), (3, 'Marketing');

INSERT INTO employees (emp_id, first_name, dept_id, salary) VALUES
    (1, 'Alice', 1, 95000),
    (2, 'Bob',   1, 72000),
    (3, 'Carla', 2, 68000),
    (4, 'Dev',   2, 61000),
    (5, 'Eve',   3, 58000);

-- Pad employees out to a few hundred rows so the query planner's SCAN vs
-- SEARCH decision in section 04 below reflects a realistic, sizeable table
-- rather than a coin-flip between two nearly-equal-size tables.
INSERT INTO employees (first_name, dept_id, salary)
    SELECT 'Employee' || value, 1 + (value % 3), 50000 + (value % 40) * 1000
    FROM generate_series(1, 300);

-- 01. CREATE VIEW
-- ------------------------------------
-- - A view stores a SELECT statement under a name - it holds no data of
--   its own; every query against it re-runs the underlying SELECT. Good
--   for hiding join/aggregation complexity behind a stable, simple name.

CREATE VIEW high_earners AS
SELECT e.first_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 65000;

SELECT '-- 01. View created (no output - CREATE VIEW does not produce rows)' AS section;

-- 02. Querying a view like a table
-- ------------------------------------
-- - From the caller's side, a view looks exactly like a read-only table -
--   SELECT, WHERE, ORDER BY, JOIN with it all work normally.

SELECT '-- 02a. SELECT * FROM the view directly' AS section;
SELECT * FROM high_earners ORDER BY salary DESC;

SELECT '-- 02b. Filtering and joining against the view like any table' AS section;
SELECT first_name, salary FROM high_earners WHERE dept_name = 'Engineering';

-- 03. DROP VIEW
-- ------------------------------------
-- - Removes the view definition. The underlying tables and their data are
--   completely unaffected - only the named SELECT shortcut is gone.

DROP VIEW high_earners;

SELECT '-- 03. View dropped; underlying tables still intact' AS section;
SELECT COUNT(*) AS employees_still_here FROM employees;

-- 04. EXPLAIN QUERY PLAN on a join - index vs full scan
-- ------------------------------------
-- - A JOIN's ON condition needs an index on the joined column to avoid a
--   full scan of one side for every row of the other (a nested-loop scan).
-- - Filtering to a single department forces SQLite to look up matching
--   employees by dept_id - without an index that means scanning all 305
--   employee rows; with one, it can jump straight to the matches.
-- - dept_id in employees has NO index yet below - watch the plan change
--   once one is added.

SELECT '-- 04a. Before an index on employees.dept_id: full SCAN of employees to find matches' AS section;
EXPLAIN QUERY PLAN
SELECT e.first_name, d.dept_name
FROM departments d
JOIN employees e ON e.dept_id = d.dept_id
WHERE d.dept_name = 'Engineering';

CREATE INDEX idx_employees_dept_id ON employees(dept_id);

SELECT '-- 04b. After CREATE INDEX: SEARCH employees USING the new index instead of a full scan' AS section;
EXPLAIN QUERY PLAN
SELECT e.first_name, d.dept_name
FROM departments d
JOIN employees e ON e.dept_id = d.dept_id
WHERE d.dept_name = 'Engineering';
