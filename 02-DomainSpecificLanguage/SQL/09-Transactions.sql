-- 09. Transactions
-- ------------------------------------
-- Run with: sqlite3 ":memory:" < 09-Transactions.sql
--
-- Topics in this file:
--   01. ACID, briefly
--   02. BEGIN / COMMIT
--   03. ROLLBACK after an error
--   04. SAVEPOINT (nested rollback)

.headers on
.mode column

-- 01. ACID, briefly
-- ------------------------------------
-- - Atomicity:   a transaction's statements all succeed, or none do - no
--                partial writes left behind.
-- - Consistency: a transaction moves the database from one valid state to
--                another, never violating declared constraints.
-- - Isolation:   concurrent transactions don't see each other's uncommitted
--                changes (SQLite serializes writers - one writer at a time).
-- - Durability:  once COMMIT returns, the change survives a crash/power
--                loss (it's been fsync'd to disk, per SQLite's journal mode).

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner      TEXT NOT NULL,
    balance    REAL NOT NULL CHECK (balance >= 0)
);

INSERT INTO accounts (owner, balance) VALUES ('Alice', 1000), ('Bob', 500);

-- 02. BEGIN / COMMIT
-- ------------------------------------
-- - Every statement outside an explicit transaction runs in its own
--   implicit auto-commit transaction. BEGIN starts a transaction you
--   control; COMMIT makes its changes permanent.
-- - A transfer between two rows is the textbook case for wrapping multiple
--   statements atomically - if the second UPDATE failed after the first
--   succeeded outside a transaction, money would vanish.

SELECT '-- 02a. Balances before the transfer' AS section;
SELECT * FROM accounts;

BEGIN;
UPDATE accounts SET balance = balance - 200 WHERE owner = 'Alice';
UPDATE accounts SET balance = balance + 200 WHERE owner = 'Bob';
COMMIT;

SELECT '-- 02b. Balances after COMMIT: transfer applied atomically' AS section;
SELECT * FROM accounts;

-- 03. ROLLBACK after an error
-- ------------------------------------
-- - ROLLBACK discards every change made since BEGIN, restoring the state
--   as of the last COMMIT. Here, a transfer that would push Bob's balance
--   negative gets caught (via CHECK) and rolled back with no partial effect.

SELECT '-- 03a. Balances before the failed transfer attempt' AS section;
SELECT * FROM accounts;

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE owner = 'Alice';
-- This second update would violate the CHECK (balance >= 0) constraint,
-- since Bob only has 700 - simulate catching that failure at the app layer
-- and rolling back both statements instead of leaving Alice's debit applied.
-- UPDATE accounts SET balance = balance - 900 WHERE owner = 'Bob'; -- would fail CHECK
ROLLBACK;

SELECT '-- 03b. Balances after ROLLBACK: unchanged, as if the transaction never ran' AS section;
SELECT * FROM accounts;

-- 04. SAVEPOINT
-- ------------------------------------
-- - A SAVEPOINT marks a point inside a transaction that you can roll back
--   to WITHOUT discarding the whole transaction - useful for "undo just
--   this part" logic nested inside a larger unit of work.
-- - ROLLBACK TO releases nothing itself; a matching RELEASE (or the outer
--   COMMIT/ROLLBACK) finishes things off.

SELECT '-- 04a. Balances before the savepoint demo' AS section;
SELECT * FROM accounts;

BEGIN;
UPDATE accounts SET balance = balance + 50 WHERE owner = 'Alice';  -- kept

SAVEPOINT before_bob_bonus;
UPDATE accounts SET balance = balance + 1000000 WHERE owner = 'Bob';  -- mistake
ROLLBACK TO before_bob_bonus;  -- undo just the mistaken update

UPDATE accounts SET balance = balance + 50 WHERE owner = 'Bob';  -- the real, intended change
COMMIT;

SELECT '-- 04b. Alice +50 and Bob +50 kept; Bob''s erroneous +1000000 was undone' AS section;
SELECT * FROM accounts;
