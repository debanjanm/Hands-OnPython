# 01. Comprehensions - Introduction
# ------------------------------------
# - Comprehensions provide a short, readable way to build a new collection
#   (list, dict, set) or a generator by looping over an iterable, optionally
#   filtering items, and applying an expression to each item.
# - General shape: [expression for item in iterable if condition]

print("# 01. Comprehensions - Introduction")
print("# ------------------------------------")

# 02. List Comprehension
# ------------------------------------
squares = [x ** 2 for x in range(1, 6)]
print("\n# 02. List Comprehension")
print(squares)  # [1, 4, 9, 16, 25]

# Equivalent using a plain loop, for comparison:
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x ** 2)
print(squares_loop)

# 03. List Comprehension with Condition (filter)
# ------------------------------------
evens = [x for x in range(1, 21) if x % 2 == 0]
print("\n# 03. List Comprehension with Condition")
print(evens)

# 04. List Comprehension with if-else (conditional expression)
# ------------------------------------
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print("\n# 04. List Comprehension with if-else")
print(labels)

# 05. Nested List Comprehension
# ------------------------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("\n# 05. Nested List Comprehension (flatten a matrix)")
print(flattened)

transposed = [[row[i] for row in matrix] for i in range(3)]
print("Transposed matrix:", transposed)

# 06. Set Comprehension
# ------------------------------------
unique_lengths = {len(word) for word in ["apple", "kiwi", "fig", "plum", "date"]}
print("\n# 06. Set Comprehension")
print(unique_lengths)

# 07. Dictionary Comprehension
# ------------------------------------
square_map = {x: x ** 2 for x in range(1, 6)}
print("\n# 07. Dictionary Comprehension")
print(square_map)

# Invert a dictionary using dict comprehension
square_map_inverted = {value: key for key, value in square_map.items()}
print(square_map_inverted)

# 08. Generator Expression
# ------------------------------------
# - Same syntax as list comprehension but with () instead of [].
# - Lazily evaluated - values are produced one at a time, saving memory.
gen = (x ** 2 for x in range(1, 6))
print("\n# 08. Generator Expression")
print(gen)  # <generator object ...>
print(list(gen))  # values consumed here

# 09. Comprehensions vs Loops - When to Use
# ------------------------------------
# - Use comprehensions for simple, readable transformations/filters.
# - Prefer a regular loop when logic has multiple steps, side effects,
#   or becomes hard to read as a one-liner.
print("\n# 09. Comprehensions vs Loops - When to Use")
print("# - Comprehensions: short, simple, single expression.")
print("# - Loops: multi-step logic, side effects, readability.")

# 10. Walrus Operator Inside Comprehensions
# ------------------------------------
# - `:=` lets you assign AND use a value in the same expression - useful
#   inside a comprehension to avoid computing the same expensive thing
#   twice (once to filter, once to use).

print("\n# 10. Walrus Operator Inside Comprehensions")
print("# ------------------------------------")

def expensive_transform(n):
    return n * n - 3   # stand-in for something costly you don't want to run twice

data = [1, 2, 3, 4, 5, 6]

# Without walrus: expensive_transform() would need to run twice per item
# (once in the condition, once in the expression) unless written awkwardly.
with_walrus = [result for x in data if (result := expensive_transform(x)) > 10]
print(with_walrus)

# 11. Comprehension Scope (No Leak, Unlike Python 2)
# ------------------------------------
# - In Python 3, comprehensions have their OWN local scope - loop variables
#   used inside them do not leak into the surrounding scope (Python 2's
#   list comprehensions did leak their loop variable).

print("\n# 11. Comprehension Scope (No Leak)")
print("# ------------------------------------")

loop_var = "outer_value"
squares_scoped = [loop_var for loop_var in range(3)]   # inner loop_var is local to the comprehension
print("Comprehension result:", squares_scoped)
print("Outer 'loop_var' still:", loop_var, "(untouched - Python 3 comprehensions don't leak)")

# 12. Performance: Comprehension vs Loop + append() (timeit)
# ------------------------------------
# - Comprehensions avoid the repeated attribute lookup (`.append`) and
#   Python-level function call overhead a manual loop pays each iteration,
#   so they're usually measurably faster.

print("\n# 12. Performance: Comprehension vs Loop + append()")
print("# ------------------------------------")

import timeit

comprehension_time = timeit.timeit("[x * 2 for x in range(1000)]", number=1000)

def loop_with_append():
    result = []
    for x in range(1000):
        result.append(x * 2)
    return result

loop_time = timeit.timeit(loop_with_append, number=1000)
print(f"List comprehension : {comprehension_time:.4f}s (1000 runs)")
print(f"Loop with .append(): {loop_time:.4f}s (1000 runs)")

# 13. Memory: Generator Expression vs List Comprehension
# ------------------------------------
# - A list comprehension builds and stores every value in memory at once.
# - A generator expression produces values lazily, one at a time - for a
#   large or unbounded sequence, this keeps memory usage flat instead of
#   growing with the input size.

print("\n# 13. Memory: Generator Expression vs List Comprehension")
print("# ------------------------------------")

import sys

list_comp = [x for x in range(100_000)]
gen_expr = (x for x in range(100_000))
print("sys.getsizeof(list comprehension):", sys.getsizeof(list_comp), "bytes")
print("sys.getsizeof(generator expression):", sys.getsizeof(gen_expr), "bytes (constant, regardless of range size)")
print("# Use a generator expression when you only need to iterate once and")
print("# don't need list operations like indexing or len().")

# 14. Nested Comprehension Readability Tradeoff
# ------------------------------------
# - A nested comprehension (comprehension inside a comprehension) can pack
#   a lot of logic into one line, but readability drops fast past 2 levels.
# - Once a comprehension needs more than one 'for' plus a condition, or the
#   line no longer reads left-to-right naturally, switch to a real loop.

print("\n# 14. Nested Comprehension Readability Tradeoff")
print("# ------------------------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Still reasonably readable: flatten + filter in one line.
flat_evens = [n for row in matrix for n in row if n % 2 == 0]
print("Flattened evens (nested comprehension):", flat_evens)

# Once there's extra branching logic, a real loop is clearer than
# cramming it into a comprehension:
flat_evens_loop = []
for row in matrix:
    for n in row:
        if n % 2 == 0:
            flat_evens_loop.append(n * 10)   # extra step - easier to read as a loop
print("Same idea with an extra step, as a loop:", flat_evens_loop)
