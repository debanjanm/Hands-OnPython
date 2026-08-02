-- 02. Filtering & Operators
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 02-Filtering-And-Operators.sql
--
-- Topics in this file:
--   01. Comparison operators
--   02. AND / OR / NOT precedence
--   03. LIKE / GLOB wildcards
--   04. IN
--   05. BETWEEN
--   06. IS NULL / IS NOT NULL (vs the "= NULL" gotcha)
--   07. CASE WHEN expressions

.headers on
.mode column

CREATE TABLE employees (
    emp_id      INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    last_name   TEXT NOT NULL,
    dept        TEXT,
    salary      REAL,
    manager_id  INTEGER
);

INSERT INTO employees (emp_id, first_name, last_name, dept, salary, manager_id) VALUES
    (1, 'Alice', 'Nguyen', 'Engineering', 95000, NULL),
    (2, 'Bob',   'Smith',  'Engineering', 72000, 1),
    (3, 'Carla', 'Diaz',   'Sales',       68000, NULL),
    (4, 'Dev',   'Roy',    'Sales',       61000, 3),
    (5, 'Eve',   'Owusu',  'Marketing',   58000, NULL),
    (6, 'Finn',  'Walsh',  NULL,          75000, 1);   -- dept not yet assigned

-- 01. Comparison operators
-- ------------------------------------
-- - =, !=  (or <>), <, >, <=, >=  -- all standard.
-- - SQLite has no dedicated boolean type; comparisons yield 0/1 integers.

SELECT '-- 01. salary >= 70000' AS section;
SELECT first_name, salary FROM employees WHERE salary >= 70000;

-- 02. AND / OR / NOT precedence
-- ------------------------------------
-- - Precedence (highest to lowest): NOT, then AND, then OR.
-- - Mixing AND/OR without parentheses is a classic bug source - always
--   parenthesize explicitly when combining them.

SELECT '-- 02a. Engineering AND salary > 80000 OR Sales (no parens - AND binds tighter)' AS section;
SELECT first_name, dept, salary FROM employees
WHERE dept = 'Engineering' AND salary > 80000 OR dept = 'Sales';
-- Reads as: (dept = 'Engineering' AND salary > 80000) OR dept = 'Sales'
-- Alice qualifies via the first clause; Carla and Dev via the second -
-- Bob (Engineering, 72000) is excluded even though a careless reading of
-- "Engineering or Sales, and salary > 80000" might expect otherwise.

SELECT '-- 02b. Same intent written unambiguously with parentheses' AS section;
SELECT first_name, dept, salary FROM employees
WHERE dept IN ('Engineering', 'Sales') AND salary > 80000;

SELECT '-- 02c. NOT' AS section;
SELECT first_name, dept FROM employees WHERE NOT dept = 'Engineering';

-- 03. LIKE / GLOB wildcards
-- ------------------------------------
-- - LIKE: case-insensitive (for ASCII) pattern match. % = any run of chars,
--   _ = exactly one char.
-- - GLOB: case-sensitive, uses Unix shell-style wildcards: * = any run of
--   chars, ? = exactly one char, [abc] = character class.

SELECT '-- 03a. LIKE ''%a%'' (name contains a/A anywhere)' AS section;
SELECT first_name FROM employees WHERE first_name LIKE '%a%';

SELECT '-- 03b. LIKE ''_ob'' (exactly 3 chars, ends in ob)' AS section;
SELECT first_name FROM employees WHERE first_name LIKE '_ob';

SELECT '-- 03c. GLOB ''[A-C]*'' (case-sensitive, starts with A, B, or C)' AS section;
SELECT first_name FROM employees WHERE first_name GLOB '[A-C]*';

-- 04. IN
-- ------------------------------------
-- - Shorthand for a chain of OR'd equality checks. Also accepts a subquery
--   (see file 05-Subqueries-And-CTEs.sql).

SELECT '-- 04. dept IN (''Sales'', ''Marketing'')' AS section;
SELECT first_name, dept FROM employees WHERE dept IN ('Sales', 'Marketing');

-- 05. BETWEEN
-- ------------------------------------
-- - Inclusive on both ends: BETWEEN x AND y means >= x AND <= y.

SELECT '-- 05. salary BETWEEN 60000 AND 75000 (inclusive)' AS section;
SELECT first_name, salary FROM employees WHERE salary BETWEEN 60000 AND 75000;

-- 06. IS NULL / IS NOT NULL vs the "= NULL" gotcha
-- ------------------------------------
-- - NULL means "unknown". Any comparison with NULL using =, !=, <, etc.
--   evaluates to NULL (neither true nor false), so the row is dropped
--   from WHERE results - NULL is never equal to anything, including itself.
-- - Use IS NULL / IS NOT NULL to actually test for NULL.

SELECT '-- 06a. WRONG: dept = NULL matches nothing, ever' AS section;
SELECT first_name FROM employees WHERE dept = NULL;

SELECT '-- 06b. RIGHT: dept IS NULL' AS section;
SELECT first_name FROM employees WHERE dept IS NULL;

SELECT '-- 06c. manager_id IS NOT NULL' AS section;
SELECT first_name, manager_id FROM employees WHERE manager_id IS NOT NULL;

-- 07. CASE WHEN expressions
-- ------------------------------------
-- - An inline expression, not a control-flow statement - evaluates to a
--   single value per row and can be used anywhere an expression is valid
--   (SELECT list, WHERE, ORDER BY, ...).
-- - Branches are evaluated top to bottom; first match wins. ELSE is the
--   fallback (defaults to NULL if omitted).

SELECT '-- 07. CASE WHEN salary tier' AS section;
SELECT
    first_name,
    salary,
    CASE
        WHEN salary >= 90000 THEN 'Senior'
        WHEN salary >= 65000 THEN 'Mid'
        ELSE 'Junior'
    END AS salary_tier
FROM employees
ORDER BY salary DESC;
