-- 01. Fundamentals
-- ------------------------------------
-- Dialect: SQLite (chosen because it needs no server - every file here is
-- self-contained and runnable with just the sqlite3 CLI against an
-- in-memory database):
--   sqlite3 ":memory:" < 01-Fundamentals.sql
--
-- Topics in this file:
--   01. CREATE TABLE with SQLite types + dynamic typing / type affinity
--   02. INSERT
--   03. Basic SELECT
--   04. WHERE
--   05. ORDER BY (ASC/DESC, multiple columns)
--   06. LIMIT / OFFSET
--   07. DISTINCT

.headers on
.mode column

-- 01. CREATE TABLE with SQLite types
-- ------------------------------------
-- - SQLite has 5 storage classes: NULL, INTEGER, REAL, TEXT, BLOB.
-- - Unlike most databases, SQLite uses "type affinity", not rigid typing:
--   a column's declared type is only a HINT about the preferred storage
--   class. Any column (except an INTEGER PRIMARY KEY) can still store a
--   value of any type, regardless of the declared column type.
-- - The declared type is mapped to one of 5 affinities: TEXT, NUMERIC,
--   INTEGER, REAL, BLOB, based on rules (e.g. a type containing "INT" gets
--   INTEGER affinity, "CHAR"/"CLOB"/"TEXT" gets TEXT affinity).

CREATE TABLE employees (
    emp_id      INTEGER PRIMARY KEY,   -- INTEGER PRIMARY KEY -> alias for rowid (see file 08)
    first_name  TEXT NOT NULL,
    last_name   TEXT NOT NULL,
    salary      REAL,                  -- floating point
    photo       BLOB,                  -- raw bytes, stored as-is
    notes       TEXT                   -- may be left NULL
);

INSERT INTO employees (emp_id, first_name, last_name, salary, photo, notes) VALUES
    (1, 'Alice', 'Nguyen', 95000.50, NULL, 'Team lead'),
    (2, 'Bob',   'Smith',  72000.00, NULL, NULL),
    (3, 'Carla', 'Diaz',   81000.75, NULL, 'Remote');

-- Gotcha: dynamic typing lets you insert a TEXT value into a REAL-affinity
-- column - SQLite will try to convert it losslessly, but if it can't, it
-- stores the original type untouched. This is legal SQL in SQLite but would
-- be an error in strict databases like PostgreSQL.
INSERT INTO employees (emp_id, first_name, last_name, salary) VALUES
    (4, 'Dev', 'Roy', 'not-a-number');

SELECT '-- 01. Table contents (note salary stored as TEXT for emp_id 4)' AS section;
SELECT emp_id, first_name, salary, typeof(salary) AS salary_storage_class FROM employees;

-- 02. INSERT
-- ------------------------------------
-- - Multi-row INSERT with a single VALUES clause (shown above) is the
--   efficient form - one statement, one transaction, far less overhead than
--   many single-row INSERTs.
-- - Columns not listed use their DEFAULT (or NULL if no default is set).

INSERT INTO employees (emp_id, first_name, last_name) VALUES (5, 'Eve', 'Owusu');

SELECT '-- 02. Row inserted with only required columns' AS section;
SELECT * FROM employees WHERE emp_id = 5;

-- 03. Basic SELECT
-- ------------------------------------
-- - SELECT column_list FROM table; use * to select every column (fine for
--   exploration, avoid in application code - explicit columns are cheaper
--   to reason about and survive schema changes better).

SELECT '-- 03. Basic SELECT of specific columns' AS section;
SELECT first_name, last_name, salary FROM employees;

-- 04. WHERE
-- ------------------------------------
-- - Filters rows before they are returned. Runs against raw column values,
--   so comparisons follow SQLite's normal type-affinity/comparison rules.

SELECT '-- 04. WHERE salary > 80000' AS section;
SELECT first_name, salary FROM employees WHERE salary > 80000;
-- Gotcha: Dev's salary ('not-a-number', stored as TEXT) also satisfies this
-- filter! SQLite's type-sorting rule ranks TEXT values as always greater
-- than any NUMERIC/INTEGER/REAL value, regardless of content. Another
-- reason to enforce types with CHECK constraints (see file 08).

-- 05. ORDER BY
-- ------------------------------------
-- - Default direction is ASC. DESC reverses it.
-- - Multiple columns: sorts by the first, then breaks ties with the next.

SELECT '-- 05a. ORDER BY salary DESC' AS section;
SELECT first_name, salary FROM employees ORDER BY salary DESC;

SELECT '-- 05b. ORDER BY last_name ASC, first_name ASC (multi-column)' AS section;
SELECT last_name, first_name FROM employees ORDER BY last_name ASC, first_name ASC;

-- 06. LIMIT / OFFSET
-- ------------------------------------
-- - LIMIT caps the number of rows returned.
-- - OFFSET skips a number of rows before returning results - classic
--   "page 2" pagination is `LIMIT page_size OFFSET page_size * (page - 1)`.
-- - Without ORDER BY, row order (and hence which rows LIMIT/OFFSET pick)
--   is NOT guaranteed - always pair LIMIT/OFFSET with ORDER BY for stable
--   pagination.

SELECT '-- 06. LIMIT 2 OFFSET 1 (2nd and 3rd highest earners)' AS section;
SELECT first_name, salary FROM employees ORDER BY salary DESC LIMIT 2 OFFSET 1;

-- 07. DISTINCT
-- ------------------------------------
-- - Removes duplicate rows from the result set (compares the full selected
--   column list, not just one column).

INSERT INTO employees (emp_id, first_name, last_name, salary) VALUES
    (6, 'Fay', 'Diaz', 81000.75);

SELECT '-- 07a. Without DISTINCT: last_name may repeat' AS section;
SELECT last_name FROM employees ORDER BY last_name;

SELECT '-- 07b. With DISTINCT: duplicates collapsed' AS section;
SELECT DISTINCT last_name FROM employees ORDER BY last_name;
