-- 03. Joins
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 03-Joins.sql
--
-- Topics in this file:
--   01. INNER JOIN
--   02. LEFT JOIN
--   03. RIGHT/FULL OUTER JOIN - and the LEFT JOIN workaround for older SQLite
--   04. CROSS JOIN
--   05. Self-join (employee -> manager)
--   06. Multi-table joins

.headers on
.mode column

CREATE TABLE departments (
    dept_id     INTEGER PRIMARY KEY,
    dept_name   TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id      INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    dept_id     INTEGER,             -- may be NULL: not yet assigned
    manager_id  INTEGER,             -- self-referencing FK -> employees.emp_id
    salary      REAL
);

INSERT INTO departments (dept_id, dept_name) VALUES
    (1, 'Engineering'),
    (2, 'Sales'),
    (3, 'Marketing'),
    (4, 'Legal');       -- no employees assigned - used to demo LEFT/RIGHT JOIN

INSERT INTO employees (emp_id, first_name, dept_id, manager_id, salary) VALUES
    (1, 'Alice', 1, NULL, 95000),   -- Alice has no manager (top of chain)
    (2, 'Bob',   1, 1,    72000),   -- Bob reports to Alice
    (3, 'Carla', 2, NULL, 68000),   -- Carla has no manager
    (4, 'Dev',   2, 3,    61000),   -- Dev reports to Carla
    (5, 'Eve',   NULL, 1, 58000);   -- Eve has a manager but no dept yet

-- 01. INNER JOIN
-- ------------------------------------
-- - Returns only rows where the join condition matches on BOTH sides.
-- - Eve (dept_id NULL) and Legal (no employees) are both dropped.

SELECT '-- 01. INNER JOIN employees x departments' AS section;
SELECT e.first_name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
ORDER BY e.first_name;

-- 02. LEFT JOIN
-- ------------------------------------
-- - Keeps every row from the left table; unmatched right-side columns come
--   back as NULL. Eve now appears with dept_name = NULL.

SELECT '-- 02. LEFT JOIN keeps unmatched employees' AS section;
SELECT e.first_name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
ORDER BY e.first_name;

-- 03. RIGHT JOIN / FULL OUTER JOIN
-- ------------------------------------
-- - SQLite added RIGHT JOIN and FULL OUTER JOIN support in version 3.39.0
--   (2022). Before that, SQLite had NEITHER - only INNER and LEFT JOIN
--   existed, because with table order swapped, a RIGHT JOIN is just a
--   LEFT JOIN in reverse. That workaround is still useful for targeting
--   older SQLite builds or maximum portability.
-- - Legal (dept_id 4) has no employees, so it only appears via RIGHT/FULL.

SELECT '-- 03a. RIGHT JOIN (native, 3.39+): every department, even empty ones' AS section;
SELECT e.first_name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

SELECT '-- 03b. Equivalent portable workaround: swap table order, use LEFT JOIN' AS section;
SELECT e.first_name, d.dept_name
FROM departments d
LEFT JOIN employees e ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

SELECT '-- 03c. FULL OUTER JOIN (native, 3.39+): unmatched rows from both sides' AS section;
SELECT e.first_name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

-- 04. CROSS JOIN
-- ------------------------------------
-- - Cartesian product: every row of the left table paired with every row
--   of the right table (no join condition). Row count = left_count *
--   right_count. Rarely what you want on real data - useful for generating
--   combinations (e.g. size x color grids) or with small lookup tables.

SELECT '-- 04. CROSS JOIN: sizes x colors combination grid' AS section;
CREATE TABLE sizes (size TEXT);
CREATE TABLE colors (color TEXT);
INSERT INTO sizes VALUES ('S'), ('M');
INSERT INTO colors VALUES ('Red'), ('Blue');
SELECT sizes.size, colors.color FROM sizes CROSS JOIN colors;

-- 05. Self-join (employee -> manager)
-- ------------------------------------
-- - Join a table to itself using two aliases. Classic use case: resolving
--   a manager_id that points back into the same employees table.
-- - LEFT JOIN here so employees with no manager (Alice, Carla) still show
--   up, with manager_name = NULL.

SELECT '-- 05. Self-join: employee alongside their manager''s name' AS section;
SELECT emp.first_name AS employee, mgr.first_name AS manager
FROM employees emp
LEFT JOIN employees mgr ON emp.manager_id = mgr.emp_id
ORDER BY emp.first_name;

-- 06. Multi-table joins
-- ------------------------------------
-- - Chain multiple JOIN clauses to pull in more than two tables. Each JOIN
--   is evaluated left to right; order can matter for readability and
--   sometimes for the query planner (see EXPLAIN QUERY PLAN in file 08/10).

SELECT '-- 06. Multi-table: employee + department + manager, one row each' AS section;
SELECT
    emp.first_name  AS employee,
    d.dept_name      AS department,
    mgr.first_name   AS manager
FROM employees emp
LEFT JOIN departments d   ON emp.dept_id = d.dept_id
LEFT JOIN employees mgr   ON emp.manager_id = mgr.emp_id
ORDER BY emp.first_name;
