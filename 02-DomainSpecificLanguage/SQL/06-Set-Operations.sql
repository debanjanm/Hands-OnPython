-- 06. Set Operations
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 06-Set-Operations.sql
--
-- Topics in this file:
--   01. UNION vs UNION ALL (dedup cost)
--   02. INTERSECT
--   03. EXCEPT
--   04. Column/type alignment requirement between combined queries

.headers on
.mode column

CREATE TABLE engineering_team (
    emp_id      INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    skill       TEXT NOT NULL
);

CREATE TABLE contractors (
    contractor_id  INTEGER PRIMARY KEY,
    full_name      TEXT NOT NULL,
    specialty      TEXT NOT NULL
);

INSERT INTO engineering_team (emp_id, first_name, skill) VALUES
    (1, 'Alice', 'Python'),
    (2, 'Bob',   'SQL'),
    (3, 'Carla', 'Python');

INSERT INTO contractors (contractor_id, full_name, specialty) VALUES
    (101, 'Dev',   'SQL'),
    (102, 'Alice', 'Python'),   -- same name+skill also appears as an employee
    (103, 'Eve',   'Go');

-- 01. UNION vs UNION ALL
-- ------------------------------------
-- - UNION combines two result sets AND removes duplicate rows - it must
--   sort/hash the combined output to find duplicates, which costs extra
--   CPU and memory proportional to the row count.
-- - UNION ALL combines them WITHOUT removing duplicates - strictly
--   cheaper, because no dedup pass is needed. Prefer UNION ALL whenever
--   you already know the two sets are disjoint, or duplicates are fine.

SELECT '-- 01a. UNION: dedups the Alice/Python row appearing on both sides' AS section;
SELECT first_name AS name, skill AS tag FROM engineering_team
UNION
SELECT full_name, specialty FROM contractors
ORDER BY name;

SELECT '-- 01b. UNION ALL: keeps every row, including the Alice/Python duplicate' AS section;
SELECT first_name AS name, skill AS tag FROM engineering_team
UNION ALL
SELECT full_name, specialty FROM contractors
ORDER BY name;

-- 02. INTERSECT
-- ------------------------------------
-- - Returns only rows present in BOTH result sets (compares full rows,
--   deduplicated).

SELECT '-- 02. INTERSECT: (name, skill) pairs present in both tables' AS section;
SELECT first_name AS name, skill AS tag FROM engineering_team
INTERSECT
SELECT full_name, specialty FROM contractors;

-- 03. EXCEPT
-- ------------------------------------
-- - Returns rows from the FIRST result set that do NOT appear in the
--   second. Order of the two queries matters - EXCEPT is not symmetric.

SELECT '-- 03a. EXCEPT: employees not also listed as contractors' AS section;
SELECT first_name AS name, skill AS tag FROM engineering_team
EXCEPT
SELECT full_name, specialty FROM contractors;

SELECT '-- 03b. EXCEPT reversed: contractors not also listed as employees' AS section;
SELECT full_name AS name, specialty AS tag FROM contractors
EXCEPT
SELECT first_name, skill FROM engineering_team;

-- 04. Column/type alignment requirement
-- ------------------------------------
-- - Every query combined with UNION/UNION ALL/INTERSECT/EXCEPT must return
--   the SAME NUMBER of columns. Column NAMES in the output come from the
--   first query only; SQLite does not require matching declared types
--   (thanks to dynamic typing), but mixing incompatible data per column
--   position is still a design smell - keep the meaning of each column
--   position consistent across all combined queries.

SELECT '-- 04. Column count must match: 2 and 2 here, aliased from the first query' AS section;
SELECT emp_id AS id, first_name AS label FROM engineering_team
UNION ALL
SELECT contractor_id, full_name FROM contractors
ORDER BY id;
-- Mismatched column counts (e.g. selecting 3 columns on one side) raises:
--   "SELECTs to the left and right of UNION do not have the same number of result columns"
