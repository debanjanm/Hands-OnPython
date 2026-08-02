# 01. Errors and Exceptions - Introduction
# ------------------------------------
# - Syntax errors: code is malformed, caught before the program even runs.
# - Exceptions: errors that occur during execution (e.g. dividing by zero).
# - Exception handling lets a program respond to errors instead of crashing.

print("# 01. Errors and Exceptions - Introduction")
print("# ------------------------------------")

# 02. Basic try/except
# ------------------------------------
print("\n# 02. Basic try/except")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught: division by zero")

# 03. Catching Multiple Exception Types
# ------------------------------------
print("\n# 03. Catching Multiple Exception Types")
for value in ["10", "abc", 0]:
    try:
        print(100 / int(value))
    except ZeroDivisionError:
        print("Caught: cannot divide by zero")
    except ValueError:
        print(f"Caught: '{value}' is not a valid number")

# 04. Catching Multiple Exceptions in One Line
# ------------------------------------
print("\n# 04. Catching Multiple Exceptions in One Line")
try:
    int("not a number")
except (ValueError, TypeError) as e:
    print(f"Caught one of ValueError/TypeError: {e}")

# 05. else Clause - Runs Only if No Exception Occurred
# ------------------------------------
print("\n# 05. else Clause")
try:
    value = int("42")
except ValueError:
    print("conversion failed")
else:
    print("conversion succeeded, value:", value)

# 06. finally Clause - Always Runs (cleanup)
# ------------------------------------
print("\n# 06. finally Clause")
try:
    print("doing risky work")
    raise ValueError("something went wrong")
except ValueError as e:
    print("handled:", e)
finally:
    print("finally always runs (cleanup code goes here)")

# 07. Raising Exceptions Manually
# ------------------------------------
print("\n# 07. Raising Exceptions Manually")
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print("Caught raised exception:", e)

# 08. Custom Exception Classes
# ------------------------------------
# - Inherit from Exception (or a more specific built-in) to create your
#   own meaningful exception types.
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

def withdraw_v2(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

print("\n# 08. Custom Exception Classes")
try:
    withdraw_v2(100, 500)
except InsufficientFundsError as e:
    print("Caught custom exception:", e)
    print("extra data on exception:", e.balance, e.amount)

# 09. Exception Chaining (raise ... from ...)
# ------------------------------------
print("\n# 09. Exception Chaining")
def load_config():
    try:
        int("not-a-number")
    except ValueError as original_error:
        raise RuntimeError("Failed to load config") from original_error

try:
    load_config()
except RuntimeError as e:
    print("Caught:", e)
    print("original cause:", e.__cause__)

# 10. Built-in Exception Hierarchy (common ones)
# ------------------------------------
print("\n# 10. Built-in Exception Hierarchy (reference)")
print("# BaseException")
print("#  -> Exception")
print("#      -> ValueError, TypeError, KeyError, IndexError")
print("#      -> ZeroDivisionError, ArithmeticError")
print("#      -> FileNotFoundError, OSError")
print("#      -> AttributeError, NameError, ImportError")
print("# Catching a base class (e.g. Exception) also catches its subclasses.")

try:
    [1, 2, 3][10]
except IndexError:
    print("caught IndexError")

try:
    {"a": 1}["missing"]
except KeyError:
    print("caught KeyError")

# 11. Context Managers as Exception-Safe Cleanup (recap)
# ------------------------------------
print("\n# 11. Context Managers as Exception-Safe Cleanup")
print("# - `with` statements (see 06-Context-Managers.py) guarantee cleanup")
print("#   even when an exception occurs, similar to try/finally.")

# 12. Exception Groups and except* (Python 3.11+)
# ------------------------------------
# - ExceptionGroup bundles multiple unrelated exceptions raised together
#   (common in concurrent code where several tasks can fail independently).
# - except* matches exceptions INSIDE the group by type, and can run more
#   than one except* clause if the group has a mix of types.
# - Skip gracefully on older Python since the syntax doesn't even parse there.
import sys

print("\n# 12. Exception Groups and except* (3.11+)")
if sys.version_info >= (3, 11):
    # Written as a string + exec so the file still IMPORTS/PARSES on < 3.11
    # (except* is new syntax, not just a new runtime feature).
    code = '''
try:
    raise ExceptionGroup(
        "multiple failures",
        [ValueError("bad value"), TypeError("bad type"), ValueError("another bad value")],
    )
except* ValueError as eg:
    print("handled ValueError(s):", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("handled TypeError(s):", [str(e) for e in eg.exceptions])
'''
    exec(code)
else:
    print("skipped: except* requires Python 3.11+, this interpreter is", sys.version_info[:3])

# 13. Bare `raise` vs `raise e` Inside except
# ------------------------------------
# - Bare `raise` re-raises the CURRENT exception with its ORIGINAL traceback
#   intact, showing exactly where it first occurred.
# - `raise e` raises the SAME exception object, but Python adds a NEW frame
#   for that raise statement, making the traceback look like it started here.
# - Prefer bare `raise` when re-raising - it keeps debugging info accurate.
print("\n# 13. Bare `raise` vs `raise e`")
def reraise_bare():
    try:
        int("not-a-number")
    except ValueError:
        print("re-raising with bare `raise` (preserves original traceback)")
        raise

def reraise_with_e():
    try:
        int("not-a-number")
    except ValueError as e:
        print("re-raising with `raise e` (adds this frame to the traceback)")
        raise e

for fn in (reraise_bare, reraise_with_e):
    try:
        fn()
    except ValueError as e:
        print("caught at top level:", e)

# 14. contextlib.suppress() - Cleaner try/except/pass
# ------------------------------------
# - When you genuinely want to ignore a specific exception, suppress() reads
#   better than a try/except block whose body is just `pass`.
import contextlib

print("\n# 14. contextlib.suppress()")
data = {"a": 1}
with contextlib.suppress(KeyError):
    print(data["missing"])  # raises KeyError, silently ignored
print("execution continues normally after the suppressed block")

# 15. Custom Exception Hierarchy Design
# ------------------------------------
# - Define one base exception for your app/module, then specific subclasses
#   for each failure mode. Callers can catch the base to handle the whole
#   family, or a specific subclass to handle just one case.
class AppError(Exception):
    """Base exception for this application."""

class ValidationError(AppError):
    """Raised when input data fails validation."""

class NotFoundError(AppError):
    """Raised when a requested resource doesn't exist."""

def fetch_user(user_id):
    if user_id < 0:
        raise ValidationError(f"user_id cannot be negative: {user_id}")
    if user_id > 100:
        raise NotFoundError(f"no user with id {user_id}")
    return {"id": user_id, "name": "demo-user"}

print("\n# 15. Custom Exception Hierarchy Design")
for uid in (-1, 999, 5):
    try:
        print("fetched:", fetch_user(uid))
    except AppError as e:
        # catching the BASE class handles both ValidationError and NotFoundError
        print(f"caught {type(e).__name__} via base AppError:", e)

# 16. The traceback Module - Formatting/Logging Exceptions Manually
# ------------------------------------
# - traceback.format_exc() gives the full traceback as a string, useful for
#   logging to a file instead of just letting it print to stderr.
import traceback

print("\n# 16. traceback Module")
try:
    1 / 0
except ZeroDivisionError:
    formatted = traceback.format_exc()
    print("formatted traceback (first line only shown here):")
    print(formatted.strip().splitlines()[-1])
