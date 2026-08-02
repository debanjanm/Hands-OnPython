## 0. Characteristics of {Tuple}
## 1. Creating {Tuple}
## 2. Acessing {Tuple}
## 3. Adding {Tuple}
## 4. Editing {Tuple}
## 5. Deleting {Tuple}
## 6. Operations on {Tuple}: arithmatic/membership/ loop
## 7. {Tuple} Specific Methods: len/sum/min/max count index count sorted 
## 8. Advancaed Topics:  Zip, Special Syntax

# Python Tuple Explanation

# 0. Characteristics of Tuple
# ------------------------------------
# - Tuples are used to store multiple items in a single variable.
# - Tuples are ordered, immutable (unchangeable), and allow duplicate values.
# - Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# - Tuples are written with parentheses ().

print("\n# 0. Characteristics of Tuple")
print("# ------------------------------------")
print("# - Ordered, immutable, allows duplicates, indexed.")

# 1. Creating Tuple
# ------------------------------------
# - Tuples can be created using parentheses () or the tuple() constructor.

print("\n# 1. Creating Tuple")
print("# ------------------------------------")

# a) Empty Tuple
empty_tuple = ()
print("a) Empty Tuple:", empty_tuple, type(empty_tuple))

empty_tuple_constructor = tuple()
print("   Using tuple() constructor:", empty_tuple_constructor, type(empty_tuple_constructor))

# b) Tuple with initial values
number_tuple = (1, 2, 3, 4, 5)
print("\nb) Tuple with initial values:", number_tuple)

mixed_tuple = (1, "hello", 3.14, True)
print("   Tuple with mixed data types:", mixed_tuple)

string_tuple = ("apple", "banana", "cherry")
print("   Tuple of strings:", string_tuple)

# c) Tuple with single item - important to include a trailing comma
single_item_tuple = ("item",)  # Trailing comma is crucial
print("\nc) Tuple with single item:", single_item_tuple, type(single_item_tuple))

not_a_tuple = ("item") # Without trailing comma, it's just a string in parentheses
print("   Not a tuple (no comma):", not_a_tuple, type(not_a_tuple))

# d) Creating tuple from other iterables (e.g., list, string)
list_data = [10, 20, 30]
tuple_from_list = tuple(list_data)
print("\nd) Tuple from list:", tuple_from_list)

string_data = "world"
tuple_from_string = tuple(string_data)
print("   Tuple from string:", tuple_from_string)

# 2. Accessing Tuple Items
# ------------------------------------
# - Tuple items are accessed by referring to the index number, just like lists.
# - Indexing starts from 0.
# - Negative indexing works the same way as lists.
# - Slicing is also supported for tuples.

print("\n# 2. Accessing Tuple Items")
print("# ------------------------------------")

print("Original Tuple:", string_tuple)

# a) Accessing by index
first_item = string_tuple[0]
print("a) Accessing first item [0]:", first_item)

second_item = string_tuple[1]
print("   Accessing second item [1]:", second_item)

last_item = string_tuple[-1]
print("   Accessing last item [-1]:", last_item)

# b) Slicing - get a range of items
slice_tuple_1_3 = string_tuple[1:3] # Items from index 1 to 2
print("\nb) Slicing [1:3]:", slice_tuple_1_3)

slice_tuple_start_2 = string_tuple[2:] # Items from index 2 to the end
print("   Slicing [2:]:", slice_tuple_start_2)

slice_tuple_all = string_tuple[:] # Copy of the entire tuple
print("   Slicing [:] (copy):", slice_tuple_all)

# 3. Adding Tuple Items (Immutability)
# ------------------------------------
# - Tuples are immutable, meaning you cannot directly add items.
# - However, you can concatenate tuples to simulate adding items or create a new tuple.

print("\n# 3. Adding Tuple Items (Immutability)")
print("# ------------------------------------")

print("Initial Tuple:", string_tuple)

# a) Concatenation to 'add' items (creates a new tuple)
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined_tuple = tuple1 + tuple2
print("a) Concatenation:", combined_tuple)
print("   Original tuple1 remains unchanged:", tuple1)

# b) Adding a single item using concatenation (needs to be in a tuple)
original_tuple = ("apple", "banana")
new_tuple_with_item = original_tuple + ("cherry",) # Note the comma to make it a tuple
print("\nb) Concatenating with single item:", new_tuple_with_item)

# 4. Editing Tuple Items (Immutability)
# ------------------------------------
# - Tuples are immutable, so you cannot change items directly.
# - To 'edit', you would typically convert to a list, modify, and convert back to a tuple, or create a new tuple with modified values.

print("\n# 4. Editing Tuple Items (Immutability)")
print("# ------------------------------------")

print("Original Tuple:", string_tuple)

# a) Attempting to change item directly will raise TypeError
# string_tuple[0] = "new_apple" # This will cause TypeError: 'tuple' object does not support item assignment

# b) 'Editing' by converting to list, modifying, and converting back
tuple_to_list = list(string_tuple)
tuple_to_list[0] = "apple_edited" # Now we can modify the list
edited_tuple = tuple(tuple_to_list) # Convert back to tuple
print("b) 'Editing' by list conversion:", edited_tuple)
print("   Original tuple remains unchanged:", string_tuple)

# 5. Deleting Tuple Items (Immutability)
# ------------------------------------
# - Tuples are immutable, you cannot delete individual items.
# - You can delete the entire tuple using the 'del' keyword.

print("\n# 5. Deleting Tuple Items (Immutability)")
print("# ------------------------------------")

print("Tuple before 'deletion':", string_tuple)

# a) Attempting to delete item by index will raise TypeError
# del string_tuple[0] # This will cause TypeError: 'tuple' object doesn't support item deletion

# b) Deleting the entire tuple
# del string_tuple
# print("b) del string_tuple: (string_tuple no longer exists)")
# try:
#     print(string_tuple) # This will cause NameError if tuple is deleted
# except NameError as e:
#     print("   Error:", e)

# For demonstration purposes, let's keep string_tuple for further examples
string_tuple = ("apple", "banana", "cherry")

# 6. Operations on Tuple: arithmetic/membership/ loop
# ------------------------------------

print("\n# 6. Operations on Tuple: arithmetic/membership/ loop")
print("# ------------------------------------")

print("Tuple for operations:", string_tuple)

# a) Arithmetic operations - concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

concatenated_tuple = tuple1 + tuple2 # Tuple concatenation
print("\na) Arithmetic - concatenation:")
print("   tuple1 + tuple2:", concatenated_tuple)

repeated_tuple = tuple1 * 3 # Tuple repetition
print("\n   Arithmetic - repetition:")
print("   tuple1 * 3:", repeated_tuple)

# b) Membership testing (checking if an item exists)
print("\nb) Membership testing:")
print("'apple' in string_tuple:", "apple" in string_tuple)
print("'banana' in string_tuple:", "banana" in string_tuple)
print("'orange' in string_tuple:", "orange" in string_tuple) # Item does not exist
print("'orange' not in string_tuple:", "orange" not in string_tuple)

# c) Looping through a tuple
print("\nc) Looping through a tuple:")

print("   - Looping through elements:")
for item in string_tuple:
    print("     Item:", item)

print("   - Looping through index and elements using enumerate():")
for index, item in enumerate(string_tuple):
    print("     Index:", index, ", Item:", item)

print("   - Looping using index range:")
for i in range(len(string_tuple)):
    print("     Index:", i, ", Item:", string_tuple[i])

# 7. Tuple Specific Methods: len/sum/min/max/count/index/sorted

print("\n# 7. Tuple Specific Methods: len/sum/min/max/count/index/sorted")
print("# ------------------------------------")

number_tuple_methods = (5, 2, 8, 1, 8, 3)
print("Tuple for methods:", number_tuple_methods)

# a) len() - number of items in the tuple
print("\na) len(number_tuple_methods):", len(number_tuple_methods))

# b) sum() - sum of all items in the tuple (numeric tuple)
print("b) sum(number_tuple_methods):", sum(number_tuple_methods))

# c) min() and max() - min/max item in the tuple
print("c) min(number_tuple_methods):", min(number_tuple_methods), ", max(number_tuple_methods):", max(number_tuple_methods))

# d) count(item) - count occurrences of an item
print("d) count(8):", number_tuple_methods.count(8))
print("   count(4):", number_tuple_methods.count(4))

# e) index(item) - returns index of the first occurrence of an item
print("e) index(8):", number_tuple_methods.index(8))
# print("   index(4):", number_tuple_methods.index(4)) # ValueError: 4 is not in tuple

# f) sorted(tuple) - returns a new sorted list from tuple (tuple itself is unchanged)
sorted_list_from_tuple = sorted(number_tuple_methods)
print("\nf) sorted(number_tuple_methods):", sorted_list_from_tuple, type(sorted_list_from_tuple))
print("   Original tuple remains unchanged:", number_tuple_methods)

# 8. Advanced Topics: Zip, Special Syntax

print("\n# 8. Advanced Topics: Zip, Special Syntax")
print("# ------------------------------------")

# a) Zip function - combining multiple iterables (including tuples)

print("\na) Zip Function:")

tuple_names = ("Alice", "Bob", "Charlie")
tuple_ages = (25, 30, 28)
tuple_cities = ("New York", "London", "Paris")

# Example 1: Zip two tuples - creates an iterator of tuples
zipped_tuple_pairs = zip(tuple_names, tuple_ages)
print("   Example 1: zip(tuple_names, tuple_ages):", list(zipped_tuple_pairs)) # Convert to list to print iterator

# Example 2: Zip three tuples
zipped_tuple_triples = zip(tuple_names, tuple_ages, tuple_cities)
print("   Example 2: zip(tuple_names, tuple_ages, tuple_cities):", list(zipped_tuple_triples))

# Example 3: Creating tuple of tuples using zip and tuple constructor
tuple_of_tuples = tuple(zip(tuple_names, tuple_ages))
print("   Example 3: tuple(zip(tuple_names, tuple_ages)):", tuple_of_tuples, type(tuple_of_tuples))

# b) Special Syntax - Tuple Packing and Unpacking

print("\nb) Special Syntax - Tuple Packing and Unpacking:")

# i) Tuple Packing - assigning multiple values to a single tuple variable
packed_tuple = 1, "hello", 3.14  # Values are 'packed' into a tuple
print("   i) Tuple Packing: packed_tuple =", packed_tuple, type(packed_tuple))

# ii) Tuple Unpacking - extracting values from a tuple into separate variables
x, y, z = packed_tuple # Values are 'unpacked' into x, y, z
print("   ii) Tuple Unpacking: x, y, z = packed_tuple")
print("       x:", x, ", y:", y, ", z:", z)

# Example: Unpacking with zip
coordinate_pairs = [(10, 20), (30, 40), (50, 60)]
x_coords, y_coords = zip(*coordinate_pairs) # Unzip list of tuples using * operator
print("   Example: Unpacking with zip and *:")
print("       coordinate_pairs:", coordinate_pairs)
print("       Unpacked x_coords:", x_coords, type(x_coords)) # zip returns iterators of tuples
print("       Unpacked y_coords:", y_coords, type(y_coords))

# 9. Immutability Is Shallow - Mutable Contents Gotcha
# ------------------------------------
# - A tuple itself cannot be reassigned (you can't replace what's at a slot),
#   but if a tuple CONTAINS a mutable object (like a list), that inner
#   object can still be mutated in place - the tuple's immutability only
#   protects its own slots, not what they point to.

print("\n# 9. Immutability Is Shallow - Mutable Contents Gotcha")
print("# ------------------------------------")

tuple_with_list = (1, 2, [3, 4])
print("Original:", tuple_with_list)

# tuple_with_list[2] = [9, 9]   # TypeError - can't reassign the slot itself
tuple_with_list[2].append(5)    # but the LIST inside can be mutated in place
print("After tuple_with_list[2].append(5):", tuple_with_list, "(tuple 'changed' even though it's immutable!)")

# 10. Tuple Hashability
# ------------------------------------
# - A tuple is hashable (usable as a dict key / set member) ONLY if every
#   element inside it is also hashable. A tuple containing a list is NOT
#   hashable, because lists are mutable and unhashable.
# - This is the main practical reason to reach for a tuple over a list:
#   you need it as a dict key or set element.

print("\n# 10. Tuple Hashability")
print("# ------------------------------------")

hashable_tuple = (1, 2, 3)
print("hash((1, 2, 3)):", hash(hashable_tuple))

coordinate_cache = {(0, 0): "origin", (1, 1): "diagonal"}   # tuples as dict keys
print("Using tuples as dict keys:", coordinate_cache)

try:
    hash(([1, 2], 3))   # tuple containing a list
except TypeError as e:
    print("\nhash(([1, 2], 3)) fails:", e)

try:
    bad_dict = {[1, 2]: "value"}   # a list can never be a dict key
except TypeError as e:
    print("{[1, 2]: 'value'} fails:", e)

# 11. Tuple vs List - Creation Performance
# ------------------------------------
# - Tuples are immutable and fixed-size, so Python can allocate them more
#   cheaply than lists (no extra over-allocated capacity needed - see List's
#   section 9). Tuple literals of constants are even precomputed at compile
#   time in some cases.

print("\n# 11. Tuple vs List - Creation Performance")
print("# ------------------------------------")

import timeit

tuple_creation = timeit.timeit("(1, 2, 3, 4, 5)", number=1_000_000)
list_creation = timeit.timeit("[1, 2, 3, 4, 5]", number=1_000_000)
print(f"Creating a tuple literal x1,000,000: {tuple_creation:.4f}s")
print(f"Creating a list literal  x1,000,000: {list_creation:.4f}s")
print("# Tuples are typically faster to create and lighter in memory - use")
print("# them for fixed collections of values that won't change.")

import sys
print("\nsys.getsizeof((1, 2, 3)) :", sys.getsizeof((1, 2, 3)), "bytes")
print("sys.getsizeof([1, 2, 3]) :", sys.getsizeof([1, 2, 3]), "bytes")

# 12. Tuple as Lightweight Record vs namedtuple vs dataclass
# ------------------------------------
# - Plain tuple: fastest/lightest, but fields are accessed by POSITION -
#   `person[0]`, `person[1]` are not self-documenting.
# - collections.namedtuple: still an immutable tuple under the hood, but
#   fields are also accessible by NAME - readable, still very lightweight.
# - dataclass: a regular (mutable by default) class with less boilerplate -
#   best when you need mutability, methods, or default values.

print("\n# 12. Tuple as Lightweight Record vs namedtuple vs dataclass")
print("# ------------------------------------")

plain_tuple_person = ("Alice", 30)
print("Plain tuple:", plain_tuple_person, "-> name is plain_tuple_person[0]:", plain_tuple_person[0])

from collections import namedtuple
Person = namedtuple("Person", ["name", "age"])
namedtuple_person = Person("Alice", 30)
print("\nnamedtuple:", namedtuple_person, "-> name is namedtuple_person.name:", namedtuple_person.name)
print("Still a tuple under the hood:", isinstance(namedtuple_person, tuple))

from dataclasses import dataclass
@dataclass
class PersonDC:
    name: str
    age: int

dataclass_person = PersonDC("Alice", 30)
print("\ndataclass:", dataclass_person, "-> name is dataclass_person.name:", dataclass_person.name)
dataclass_person.age = 31   # dataclasses are mutable by default (unlike tuple/namedtuple)
print("dataclass is mutable, age updated to:", dataclass_person.age)
print("# Choose: tuple for anonymous fixed data, namedtuple for readable")
print("# immutable records, dataclass when you need mutability or methods.")

print("\n# End of Tuple Explanation")

