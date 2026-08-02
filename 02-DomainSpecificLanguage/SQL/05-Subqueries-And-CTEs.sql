-- 05. Subqueries & CTEs
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 05-Subqueries-And-CTEs.sql
--
-- Topics in this file:
--   01. Scalar subqueries
--   02. Subqueries in WHERE / IN
--   03. Correlated subqueries
--   04. WITH (CTE)
--   05. Recursive CTE - number sequence
--   06. Recursive CTE - walking an org chart

.headers on
.mode column

CREATE TABLE employees (
    emp_id      INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    dept        TEXT NOT NULL,
    manager_id  INTEGER,
    salary      REAL NOT NULL
);

INSERT INTO employees (emp_id, first_name, dept, manager_id, salary) VALUES
    (1, 'Alice', 'Engineering', NULL, 95000),  -- CEO-level, no manager
    (2, 'Bob',   'Engineering', 1,    72000),
    (3, 'Carla', 'Sales',       1,    68000),
    (4, 'Dev',   'Sales',       3,    61000),
    (5, 'Eve',   'Sales',       3,    58000),
    (6, 'Finn',  'Marketing',   1,    75000);

-- 01. Scalar subqueries
-- ------------------------------------
-- - A subquery that returns exactly one row, one column - can be used
--   anywhere a single value/expression is expected.

SELECT '-- 01. Scalar subquery: each salary vs the company-wide average' AS section;
SELECT
    first_name,
    salary,
    (SELECT AVG(salary) FROM employees) AS company_avg,
    salary - (SELECT AVG(salary) FROM employees) AS diff_from_avg
FROM employees
ORDER BY salary DESC;

-- 02. Subqueries in WHERE / IN
-- ------------------------------------
-- - IN (subquery): the outer row is kept if its value appears anywhere in
--   the subquery's result set. Equivalent in spirit to a join, but reads
--   more naturally for "matches any of these".

SELECT '-- 02. Employees who manage someone (their emp_id appears as a manager_id)' AS section;
SELECT first_name, dept
FROM employees
WHERE emp_id IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL)
ORDER BY first_name;

-- 03. Correlated subqueries
-- ------------------------------------
-- - The inner query references a column from the OUTER query, so it must
--   be re-evaluated once per outer row (unlike the scalar subquery in 01,
--   which runs once and is reused for every row).
-- - Performance note: correlated subqueries can be O(n*m) without a
--   supporting index on the correlated column - EXPLAIN QUERY PLAN (see
--   file 08) will show a "SCALAR SUBQUERY" re-executed per row if unindexed.

SELECT '-- 03. Employees earning more than their own department''s average' AS section;
SELECT e.first_name, e.dept, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary) FROM employees e2 WHERE e2.dept = e.dept
)
ORDER BY e.dept;

-- 04. WITH (CTE)
-- ------------------------------------
-- - A Common Table Expression names a subquery so it can be referenced
--   like a table in the main query - improves readability over deeply
--   nested subqueries, and a CTE can be referenced multiple times.

SELECT '-- 04. CTE: high earners (salary > 65000), then join back to employees' AS section;
WITH high_earners AS (
    SELECT emp_id, first_name, salary FROM employees WHERE salary > 65000
)
SELECT h.first_name, h.salary, e.dept
FROM high_earners h
JOIN employees e ON e.emp_id = h.emp_id
ORDER BY h.salary DESC;

-- 05. Recursive CTE - number sequence
-- ------------------------------------
-- - A recursive CTE has an "anchor" (base case, runs once) UNION ALL a
--   "recursive" term that refers back to the CTE's own name - it keeps
--   re-running the recursive term against the previously produced rows
--   until it produces no more rows.
-- - Classic use: generate a sequence without a real table (e.g. dates,
--   integers 1..N).

SELECT '-- 05. Recursive CTE: generate integers 1..10' AS section;
WITH RECURSIVE counter(n) AS (
    SELECT 1                       -- anchor: starting value
    UNION ALL
    SELECT n + 1 FROM counter WHERE n < 10   -- recursive step + termination
)
SELECT n FROM counter;

-- 06. Recursive CTE - walking an org chart
-- ------------------------------------
-- - Same mechanism applied to a self-referencing table: start from a root
--   employee, then repeatedly pull in rows whose manager_id matches an
--   emp_id already found - naturally computes reporting depth.

SELECT '-- 06. Recursive CTE: everyone under Alice, with reporting depth' AS section;
WITH RECURSIVE org_chart(emp_id, first_name, depth) AS (
    SELECT emp_id, first_name, 0
    FROM employees
    WHERE first_name = 'Alice'                 -- anchor: root of the chart
    UNION ALL
    SELECT e.emp_id, e.first_name, oc.depth + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.emp_id  -- recursive step: direct reports
)
SELECT first_name, depth FROM org_chart ORDER BY depth, first_name;
