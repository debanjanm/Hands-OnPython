# 01. Unpacking - Introduction
# ------------------------------------
# - Unpacking lets you assign elements of an iterable to multiple
#   variables in a single statement.
# - Packing is the reverse: gathering multiple values into one variable
#   (list/tuple), typically using the * operator.

print("# 01. Unpacking - Introduction")
print("# ------------------------------------")

# 02. Basic Sequence Unpacking
# ------------------------------------
a, b, c = (1, 2, 3)
print("\n# 02. Basic Sequence Unpacking")
print(a, b, c)

x, y = [10, 20]
print(x, y)

# 03. Swapping Values (no temp variable needed)
# ------------------------------------
x, y = y, x
print("\n# 03. Swapping Values")
print("x:", x, "y:", y)

# 04. Extended Unpacking with * (starred expressions)
# ------------------------------------
first, *rest = [1, 2, 3, 4, 5]
print("\n# 04. Extended Unpacking with *")
print("first:", first, "rest:", rest)

*init, last = [1, 2, 3, 4, 5]
print("init:", init, "last:", last)

first, *middle, last = [1, 2, 3, 4, 5]
print("first:", first, "middle:", middle, "last:", last)

# 05. Ignoring Values with _
# ------------------------------------
first, _, third = (1, 2, 3)
print("\n# 05. Ignoring Values with _")
print("first:", first, "third:", third)

# 06. Nested Unpacking
# ------------------------------------
(a, b), c = (1, 2), 3
print("\n# 06. Nested Unpacking")
print(a, b, c)

points = [(1, 2), (3, 4), (5, 6)]
for px, py in points:
    print(f"point -> x={px}, y={py}")

# 07. Unpacking in Function Calls (*args)
# ------------------------------------
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print("\n# 07. Unpacking in Function Calls (*args)")
print(add(*numbers))

# 08. Unpacking Dictionaries (**kwargs)
# ------------------------------------
def greet(name, greeting):
    return f"{greeting}, {name}!"

person = {"name": "Debanjan", "greeting": "Hello"}
print("\n# 08. Unpacking Dictionaries (**kwargs)")
print(greet(**person))

# 09. Merging Collections with Unpacking
# ------------------------------------
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print("\n# 09. Merging Collections with Unpacking")
print("merged list:", merged_list)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}  # note: 'b' in dict2 overrides dict1
merged_dict = {**dict1, **dict2}
print("merged dict:", merged_dict)

# 10. Packing Arguments in Function Definitions
# ------------------------------------
def summarize(*args, **kwargs):
    print("args (packed into tuple):", args)
    print("kwargs (packed into dict):", kwargs)

print("\n# 10. Packing Arguments in Function Definitions")
summarize(1, 2, 3, name="Debanjan", role="Learner")

# 11. Unpacking in Function Returns (Multiple Values)
# ------------------------------------
# - Python functions can only return ONE object, but that object is often a
#   tuple - `return a, b` packs a and b into a tuple, and the caller
#   unpacks it right back into separate names in one line.

print("\n# 11. Unpacking in Function Returns")
print("# ------------------------------------")

def min_max(numbers):
    return min(numbers), max(numbers)   # packed into a tuple on return

low, high = min_max([4, 1, 9, 2, 7])    # unpacked immediately by the caller
print("min_max([4, 1, 9, 2, 7]) unpacked -> low:", low, "high:", high)

# 12. Unpacking with zip(*matrix) for Transpose
# ------------------------------------
# - zip(*matrix) is the classic "unzip"/transpose trick: * unpacks each row
#   as a separate argument to zip(), which then groups by COLUMN instead of
#   by row - flipping rows and columns.

print("\n# 12. Unpacking with zip(*matrix) for Transpose")
print("# ------------------------------------")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
transposed = list(zip(*matrix))   # * unpacks the 3 rows as 3 separate args to zip()
print("Original matrix:", matrix)
print("Transposed (zip(*matrix)):", transposed)

# 13. Unpacking Gotcha with Generators (Single Consumption)
# ------------------------------------
# - A generator/iterator can only be consumed ONCE. Unpacking it (like any
#   iteration) exhausts it - trying to unpack or iterate it again yields
#   nothing, silently, with no error.

print("\n# 13. Unpacking Gotcha with Generators")
print("# ------------------------------------")

gen = (x for x in range(3))
a, b, c = gen                 # unpacking consumes the generator fully
print("First unpack -> a:", a, "b:", b, "c:", c)

print("list(gen) after it's exhausted:", list(gen), "(empty - already consumed!)")

try:
    x, y, z = gen              # trying to unpack an exhausted generator
except ValueError as e:
    print("Unpacking an exhausted generator raises:", e)

# 14. Extended Unpacking in For-Loops
# ------------------------------------
# - The `first, *rest` starred pattern from section 04 also works directly
#   as a for-loop target, unpacking each item of a sequence-of-sequences
#   on every iteration.

print("\n# 14. Extended Unpacking in For-Loops")
print("# ------------------------------------")

records = [
    ("Alice", 90, 85, 95),
    ("Bob", 70, 75),
    ("Charlie", 88, 92, 79, 100),
]

for name, *scores in records:   # name gets the first item, scores gets the rest as a list
    print(f"{name}: scores={scores}, average={sum(scores) / len(scores):.1f}")
