-- 04. Aggregation & Grouping
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 04-Aggregation-And-Grouping.sql
--
-- Topics in this file:
--   01. COUNT / SUM / AVG / MIN / MAX
--   02. GROUP BY (single column)
--   03. GROUP BY (multiple columns)
--   04. HAVING vs WHERE
--   05. GROUP_CONCAT

.headers on
.mode column

CREATE TABLE employees (
    emp_id      INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    dept        TEXT NOT NULL,
    region      TEXT NOT NULL,
    salary      REAL NOT NULL
);

INSERT INTO employees (emp_id, first_name, dept, region, salary) VALUES
    (1, 'Alice', 'Engineering', 'West', 95000),
    (2, 'Bob',   'Engineering', 'East', 72000),
    (3, 'Carla', 'Sales',       'West', 68000),
    (4, 'Dev',   'Sales',       'West', 61000),
    (5, 'Eve',   'Sales',       'East', 58000),
    (6, 'Finn',  'Marketing',   'East', 75000);

-- 01. COUNT / SUM / AVG / MIN / MAX
-- ------------------------------------
-- - These are aggregate functions: they collapse many rows into one value.
-- - COUNT(*) counts rows; COUNT(col) counts non-NULL values in that column
--   only - the two can differ when a column has NULLs.

SELECT '-- 01. Aggregates over the whole table' AS section;
SELECT
    COUNT(*)        AS total_employees,
    SUM(salary)      AS total_salary,
    AVG(salary)      AS avg_salary,
    MIN(salary)      AS min_salary,
    MAX(salary)      AS max_salary
FROM employees;

-- 02. GROUP BY (single column)
-- ------------------------------------
-- - Splits rows into buckets by the grouped column(s), then applies
--   aggregate functions PER bucket instead of over the whole table.
-- - Every non-aggregated column in the SELECT list must appear in GROUP BY
--   (SQLite is lenient here and won't always error, but relying on that is
--   a portability trap - other databases will reject it).

SELECT '-- 02. Headcount and avg salary per department' AS section;
SELECT dept, COUNT(*) AS headcount, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept
ORDER BY dept;

-- 03. GROUP BY (multiple columns)
-- ------------------------------------
-- - Buckets are formed from the COMBINATION of all listed columns - one
--   group per distinct (dept, region) pair.

SELECT '-- 03. Headcount per (dept, region) combination' AS section;
SELECT dept, region, COUNT(*) AS headcount, SUM(salary) AS total_salary
FROM employees
GROUP BY dept, region
ORDER BY dept, region;

-- 04. HAVING vs WHERE
-- ------------------------------------
-- - WHERE filters individual ROWS, BEFORE grouping/aggregation happens.
-- - HAVING filters GROUPS, AFTER aggregation - it can reference aggregate
--   functions (SUM, COUNT, ...), WHERE cannot.
-- - Concrete need for HAVING: "departments with more than 1 employee" is a
--   property of the GROUP (its row count), not of any single row, so WHERE
--   headcount > 1 is not expressible - WHERE never sees the aggregated
--   value, HAVING does.

SELECT '-- 04a. WHERE: filter rows first (only West region), then group' AS section;
SELECT dept, COUNT(*) AS headcount
FROM employees
WHERE region = 'West'
GROUP BY dept
ORDER BY dept;

SELECT '-- 04b. HAVING: filter groups after aggregation (depts with 2+ people)' AS section;
SELECT dept, COUNT(*) AS headcount
FROM employees
GROUP BY dept
HAVING COUNT(*) >= 2
ORDER BY dept;

SELECT '-- 04c. WHERE and HAVING combined: filter rows, then filter the resulting groups' AS section;
SELECT dept, AVG(salary) AS avg_salary
FROM employees
WHERE region = 'East'
GROUP BY dept
HAVING AVG(salary) > 60000
ORDER BY dept;

-- 05. GROUP_CONCAT
-- ------------------------------------
-- - SQLite-specific aggregate: concatenates values from a group into a
--   single string, comma-separated by default, or with a custom separator
--   as a second argument.

SELECT '-- 05. GROUP_CONCAT: names per department' AS section;
SELECT dept, GROUP_CONCAT(first_name, ', ') AS team_members
FROM employees
GROUP BY dept
ORDER BY dept;
