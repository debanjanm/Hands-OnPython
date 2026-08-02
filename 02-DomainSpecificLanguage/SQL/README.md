# SQL

Dialect: **SQLite** - chosen because it needs no server, so every file here
is self-contained and verified by actually running it:

```
sqlite3 ":memory:" < file.sql
```

Each `.sql` file creates its own tables and seeds its own data at the top,
so it runs standalone against a fresh in-memory database - no shared or
external database, no fixture files.

| File | Covers |
|---|---|
| [01-Fundamentals.sql](01-Fundamentals.sql) | `CREATE TABLE`, SQLite storage classes/type affinity, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`/`OFFSET`, `DISTINCT` |
| [02-Filtering-And-Operators.sql](02-Filtering-And-Operators.sql) | Comparison operators, `AND`/`OR`/`NOT` precedence, `LIKE`/`GLOB`, `IN`, `BETWEEN`, `IS NULL` vs `= NULL`, `CASE WHEN` |
| [03-Joins.sql](03-Joins.sql) | `INNER`/`LEFT`/`RIGHT`/`FULL OUTER`/`CROSS JOIN`, the pre-3.39 LEFT JOIN workaround, self-join, multi-table joins |
| [04-Aggregation-And-Grouping.sql](04-Aggregation-And-Grouping.sql) | `COUNT`/`SUM`/`AVG`/`MIN`/`MAX`, `GROUP BY`, `HAVING` vs `WHERE`, `GROUP_CONCAT` |
| [05-Subqueries-And-CTEs.sql](05-Subqueries-And-CTEs.sql) | Scalar/`IN`/correlated subqueries, `WITH` (CTE), recursive CTEs (sequence + org chart) |
| [06-Set-Operations.sql](06-Set-Operations.sql) | `UNION` vs `UNION ALL`, `INTERSECT`, `EXCEPT`, column/type alignment |
| [07-Window-Functions.sql](07-Window-Functions.sql) | `OVER()`, `ROW_NUMBER()`, `RANK()`/`DENSE_RANK()`, `LAG()`/`LEAD()`, running totals, `PARTITION BY` |
| [08-Constraints-And-Keys.sql](08-Constraints-And-Keys.sql) | `PRIMARY KEY` (rowid alias), `FOREIGN KEY` + `PRAGMA foreign_keys`, `UNIQUE`, `CHECK`, `NOT NULL`, `CREATE INDEX` + `EXPLAIN QUERY PLAN` |
| [09-Transactions.sql](09-Transactions.sql) | ACID briefly, `BEGIN`/`COMMIT`/`ROLLBACK`, rollback after an error, `SAVEPOINT` |
| [10-Views-And-Query-Plans.sql](10-Views-And-Query-Plans.sql) | `CREATE VIEW`, querying/dropping a view, `EXPLAIN QUERY PLAN` on a join (index vs full scan) |
| [11-Data-Modification.sql](11-Data-Modification.sql) | `UPDATE`, `DELETE`, `INSERT ... ON CONFLICT DO UPDATE` (upsert), `ALTER TABLE ADD COLUMN`/`DROP COLUMN` |
| [12-Normalization-And-Design.sql](12-Normalization-And-Design.sql) | 1NF/2NF/3NF explained, a denormalized BEFORE schema vs a normalized AFTER schema, both runnable |
