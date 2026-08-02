## 0. Characteristics of {Dictioanry}
## 1. Creating {Dictioanry}
## 2. Acessing {Dictioanry}
## 3. Adding {Dictioanry}
## 4. Editing {Dictioanry}
## 5. Deleting {Dictioanry}
## 6. Operations on {Dictioanry}: membership/ loop
## 7. {Dictioanry} Specific Methods: len/sorted/min/max items/keys/values append/update
## 8. Advancaed Topics: Dictioanry Comprehension, Zip Function

# Python Dictionary Explanation

# 0. Characteristics of Dictionary
# ------------------------------------
# - Dictionaries are used to store data values in key:value pairs.
# - A dictionary is a collection which is ordered*, changeable and does not allow duplicates keys.
#   * As of Python 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# - Dictionaries are written with curly braces {}, and have keys and values.
# - Keys are unique and immutable (usually strings or numbers).
# - Values can be of any data type and can be mutable or immutable.

print("\n# 0. Characteristics of Dictionary")
print("# ------------------------------------")
print("# - Key-value pairs, ordered (>= Python 3.7), changeable, no duplicate keys.")
print("# - Keys are immutable (strings, numbers, tuples), Values can be any type.")

# 1. Creating Dictionary
# ------------------------------------
# - Dictionaries can be created using curly braces {} or the dict() constructor.

print("\n# 1. Creating Dictionary")
print("# ------------------------------------")

# a) Empty Dictionary
empty_dict = {}
print("a) Empty Dictionary:", empty_dict, type(empty_dict))

empty_dict_constructor = dict()
print("   Using dict() constructor:", empty_dict_constructor, type(empty_dict_constructor))

# b) Dictionary with initial key-value pairs
person_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("\nb) Dictionary with initial values:", person_dict)

person_dict_constructor = dict(name="Bob", age=25, city="London") # keyword arguments as keys
print("   Using dict() constructor with keyword arguments:", person_dict_constructor)

person_dict_constructor_pairs = dict([("name", "Charlie"), ("age", 35), ("city", "Paris")]) # list of tuples
print("   Using dict() constructor with list of tuples:", person_dict_constructor_pairs)

# 2. Accessing Dictionary
# ------------------------------------
# - You can access the items of a dictionary by referring to its key name, inside square brackets [].
# - Or using the get() method, which provides a default value if the key is not found.

print("\n# 2. Accessing Dictionary")
print("# ------------------------------------")

print("Original Dictionary:", person_dict)

# a) Using square brackets []
name = person_dict["name"]
print("a) Accessing 'name' using []:", name)

# b) Using get() method
age = person_dict.get("age")
print("b) Accessing 'age' using get():", age)

# c) Accessing a non-existent key with [] will raise KeyError
# city_not_found = person_dict["country"] # This will cause KeyError

# d) Accessing a non-existent key with get() returns None (or a default value)
city_not_found_get_none = person_dict.get("country")
print("d) Accessing non-existent 'country' using get():", city_not_found_get_none)

city_not_found_get_default = person_dict.get("country", "Unknown")
print("   Accessing non-existent 'country' using get() with default value:", city_not_found_get_default)

# 3. Adding Dictionary Items
# ------------------------------------
# - Adding items to a dictionary is done by assigning a value to a new key.
# - Or using the update() method to add multiple items or update existing ones.

print("\n# 3. Adding Dictionary Items")
print("# ------------------------------------")

print("Initial Dictionary:", person_dict)

# a) Adding a new key-value pair using square brackets []
person_dict["profession"] = "Engineer"
print("a) Adding 'profession' using []:", person_dict)

# b) Adding multiple items using update() method
person_dict.update({"email": "alice@example.com", "phone": "123-456-7890"})
print("b) Adding 'email' and 'phone' using update():", person_dict)

# c) update() method also works with keyword arguments
person_dict.update(gender="Female")
print("c) Adding 'gender' using update() with keyword argument:", person_dict)

# 4. Editing Dictionary Items
# ------------------------------------
# - Editing items is done by referring to the key and assigning a new value.
# - Or using the update() method to modify existing items.

print("\n# 4. Editing Dictionary Items")
print("# ------------------------------------")

print("Dictionary before editing:", person_dict)

# a) Editing an existing value using square brackets []
person_dict["age"] = 31
print("a) Editing 'age' using []:", person_dict)

# b) Editing multiple values using update() method
person_dict.update({"city": "San Francisco", "profession": "Software Engineer"})
print("b) Editing 'city' and 'profession' using update():", person_dict)

# 5. Deleting Dictionary Items
# ------------------------------------
# - There are several methods to remove items from a dictionary:
#   - pop(key): Removes the item with the specified key and returns the removed value.
#   - popitem(): Removes the last inserted key-value pair (in versions before 3.7, removes an arbitrary item).
#   - del keyword: Deletes an item with a specific key or the entire dictionary.
#   - clear(): Empties the dictionary.

print("\n# 5. Deleting Dictionary Items")
print("# ------------------------------------")

print("Dictionary before deletion:", person_dict)

# a) pop(key) - remove and return value
removed_age = person_dict.pop("age")
print("a) pop('age'):", person_dict, "Removed age:", removed_age)

# b) popitem() - remove the last inserted item (in Python 3.7+)
removed_item = person_dict.popitem()
print("b) popitem():", person_dict, "Removed item:", removed_item)

# c) del keyword - delete item by key
del person_dict["city"]
print("c) del person_dict['city']:", person_dict)

# d) del keyword - delete entire dictionary
# del person_dict
# print("d) del person_dict: (person_dict no longer exists)")
# try:
#     print(person_dict) # This will cause NameError if dictionary is deleted
# except NameError as e:
#     print("   Error:", e)

# e) clear() - empty the dictionary
person_dict.clear()
print("e) clear():", person_dict)

# Reset person_dict for further examples
person_dict = {"name": "Alice", "age": 30, "city": "New York"}

# 6. Operations on Dictionary: membership/ loop
# ------------------------------------

print("\n# 6. Operations on Dictionary: membership/ loop")
print("# ------------------------------------")

print("Dictionary for operations:", person_dict)

# a) Membership testing (checking if a key exists)
print("\na) Membership testing:")
print("'name' in person_dict:", "name" in person_dict)
print("'age' in person_dict:", "age" in person_dict)
print("'country' in person_dict:", "country" in person_dict) # Key does not exist
print("'country' not in person_dict:", "country" not in person_dict)

# b) Looping through a dictionary
print("\nb) Looping through a dictionary:")

print("   - Looping through keys:")
for key in person_dict: # or for key in person_dict.keys():
    print("     Key:", key)

print("   - Looping through values:")
for value in person_dict.values():
    print("     Value:", value)

print("   - Looping through key-value pairs (items):")
for key, value in person_dict.items():
    print("     Key:", key, ", Value:", value)

# 7. Dictionary Specific Methods: len/sorted/min/max/ items/keys/values /update

print("\n# 7. Dictionary Specific Methods: len/sorted/min/max/ items/keys/values /update")
print("# ------------------------------------")

print("Dictionary for methods:", person_dict)

# a) len() - number of items (key-value pairs)
print("\na) len(person_dict):", len(person_dict))

# b) sorted() - returns a sorted list of keys (by default)
sorted_keys = sorted(person_dict)
print("b) sorted(person_dict):", sorted_keys)

# person_dict has mixed value types (str, int), which aren't comparable to
# each other - sort/min/max by value need a dict with comparable values.
scores = {"math": 90, "science": 75, "art": 88}
sorted_keys_by_value = sorted(scores, key=scores.get) # Sort keys by value
print("   sorted(scores, key=scores.get):", sorted_keys_by_value)

# c) min() and max() - return the min/max key (by default) or based on values
min_key = min(person_dict)
max_key = max(person_dict)
print("\nc) min(person_dict):", min_key, ", max(person_dict):", max_key)

min_key_by_value = min(scores, key=scores.get)
max_key_by_value = max(scores, key=scores.get)
print("   min(scores, key=scores.get):", min_key_by_value, ", max(scores, key=scores.get):", max_key_by_value)

# d) items(), keys(), values() - view objects to access items, keys, values
items_view = person_dict.items()
keys_view = person_dict.keys()
values_view = person_dict.values()
print("\nd) items_view:", items_view, type(items_view))
print("   keys_view:", keys_view, type(keys_view))
print("   values_view:", values_view, type(values_view))

# Convert view objects to lists if you need to manipulate them as lists
items_list = list(items_view)
keys_list = list(keys_view)
values_list = list(values_view)
print("   items_list:", items_list, type(items_list))
print("   keys_list:", keys_list, type(keys_list))
print("   values_list:", values_list, type(values_list))

# e) update() - already used for adding and editing, can also merge dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"a": 10, "e": 5} # Overlapping key 'a' with dict1
print("\ne) update() - merging dictionaries")
print("   dict1:", dict1)
print("   dict2:", dict2)
print("   dict3:", dict3)

dict1.update(dict2) # Merge dict2 into dict1
print("   dict1.update(dict2):", dict1) # dict1 now contains items from dict2

dict1.update(dict3) # Merge dict3 into dict1, overwrites existing key 'a'
print("   dict1.update(dict3):", dict1) # dict1 now contains items from dict3, 'a' is updated

# 8. Advanced Topics: Dictionary Comprehension, Zip Function In Detail.
# ------------------------------------

print("\n# 8. Advanced Topics: Dictionary Comprehension, Zip Function In Detail.")
print("# ------------------------------------")

# a) Dictionary Comprehension - concise way to create dictionaries

print("\na) Dictionary Comprehension:")

# Example 1: Create a dictionary of numbers and their squares
squares_dict = {x: x**2 for x in range(5)}
print("   Example 1: Squares of numbers 0-4:", squares_dict)

# Example 2: Create a dictionary from a list, filtering even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_squares_dict = {x: x**2 for x in numbers if x % 2 == 0}
print("   Example 2: Squares of even numbers from list:", even_squares_dict)

# Example 3: Create a dictionary with key-value pairs swapped from another dictionary
swapped_dict = {value: key for key, value in person_dict.items()} # Be careful with value uniqueness when swapping
print("   Example 3: Swapping key-value pairs (original person_dict):", person_dict)
print("              Swapped dictionary:", swapped_dict)

# b) Zip Function in Detail - creating dictionaries from pairs of lists

print("\nb) Zip Function in Detail:")
# zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

keys_list = ["name", "age", "city"]
values_list = ["Eve", 28, "Chicago"]

# Example 1: Using zip() to combine keys and values lists into tuples
zipped_pairs = zip(keys_list, values_list)
print("   Example 1: zip(keys_list, values_list):", list(zipped_pairs)) # Convert iterator to list to print

# Example 2: Using zip() to create a dictionary
zipped_dict = dict(zip(keys_list, values_list))
print("   Example 2: dict(zip(keys_list, values_list)):", zipped_dict)

# Example 3: What happens if lists have different lengths? zip stops when the shortest list is exhausted.
short_keys_list = ["key1", "key2"]
long_values_list = ["val1", "val2", "val3"]
short_zipped_dict = dict(zip(short_keys_list, long_values_list))
print("   Example 3: zip with different length lists (shortest wins):", short_zipped_dict)

# Example 4: Unzipping using zip(*) - reversing the zip operation (separate pairs back to lists)
unzipped_keys, unzipped_values = zip(*zip(keys_list, values_list)) # * operator unpacks the zipped pairs
print("   Example 4: Unzipping using zip(*):")
print("              Unzipped keys:", list(unzipped_keys))
print("              Unzipped values:", list(unzipped_values))

# 9. Dict Insertion-Order Guarantee (Python 3.7+)
# ------------------------------------
# - Since Python 3.7, dicts are GUARANTEED (as a language spec, not just a
#   CPython implementation detail) to preserve insertion order: iterating
#   with keys()/values()/items() yields entries in the order they were added.
# - This makes dict.fromkeys() a handy order-preserving deduplication trick.

print("\n# 9. Dict Insertion-Order Guarantee (3.7+)")
print("# ------------------------------------")

order_demo = {}
order_demo["z"] = 1
order_demo["a"] = 2
order_demo["m"] = 3
print("Insertion order preserved:", list(order_demo.keys()), "(not sorted alphabetically)")

items_with_dupes = [1, 2, 2, 3, 1, 4]
deduped_ordered = list(dict.fromkeys(items_with_dupes))   # keeps first-seen order
print("dict.fromkeys() dedup, order-preserving:", deduped_ordered)

# 10. Dict Internals (Conceptual): Hash Table + Collisions
# ------------------------------------
# - Like sets, dicts are hash tables: a key's hash(key) determines which
#   slot it's stored in, giving O(1) average lookup/insert/delete.
# - Two different keys can hash to the same slot (a "collision") - CPython
#   resolves this via open addressing (probing to the next available slot).
# - Since 3.6, CPython dicts keep a separate compact array for insertion
#   order alongside the hash table, which is how ordering is preserved
#   without sacrificing O(1) lookups.

print("\n# 10. Dict Internals (Conceptual)")
print("# ------------------------------------")
print("# - lookup/insert/delete by key : O(1) average (hash -> slot)")
print("# - collisions                  : resolved via open addressing/probing")
print("# - iteration order              : insertion order (tracked separately)")

# 11. dict.setdefault vs collections.defaultdict
# ------------------------------------
# - setdefault(key, default): returns dict[key] if present, else inserts
#   default and returns it - one call, avoids a manual "if key not in dict" check.
# - defaultdict(factory): a dict subclass where MISSING keys auto-create a
#   default value (via factory()) on first access - handy for grouping/counting.

print("\n# 11. dict.setdefault vs collections.defaultdict")
print("# ------------------------------------")

grouped_setdefault = {}
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
for word in words:
    grouped_setdefault.setdefault(word[0], []).append(word)
print("Grouped with setdefault():", grouped_setdefault)

from collections import defaultdict
grouped_defaultdict = defaultdict(list)
for word in words:
    grouped_defaultdict[word[0]].append(word)   # missing key auto-creates []
print("Grouped with defaultdict(list):", dict(grouped_defaultdict))

# 12. Merging Dicts: | Operator (3.9+) vs update()
# ------------------------------------
# - dict1 | dict2 returns a NEW merged dict, leaving both originals unchanged.
# - dict1.update(dict2) merges dict2's items INTO dict1 in place.
# - In both, keys from the right-hand/argument dict win on conflicts.
# - |= is the in-place version of the | operator.

print("\n# 12. Merging Dicts: | Operator (3.9+) vs update()")
print("# ------------------------------------")

dict_a = {"x": 1, "y": 2}
dict_b = {"y": 20, "z": 30}

merged_new = dict_a | dict_b   # creates a new dict, dict_a/dict_b untouched
print("dict_a | dict_b (new dict):", merged_new)
print("dict_a unchanged:", dict_a)

dict_a_copy = dict_a.copy()
dict_a_copy.update(dict_b)     # mutates dict_a_copy in place
print("dict_a_copy.update(dict_b) (in place):", dict_a_copy)

dict_a_inplace = dict_a.copy()
dict_a_inplace |= dict_b       # |= is the in-place merge operator
print("dict_a_inplace |= dict_b (in place):", dict_a_inplace)

# 13. Dict Comprehension Performance
# ------------------------------------
# - Like list comprehensions, dict comprehensions compile to dedicated
#   bytecode and generally beat building a dict with a manual loop + []
#   assignment, especially for larger inputs.

print("\n# 13. Dict Comprehension Performance")
print("# ------------------------------------")

import timeit

comprehension_time = timeit.timeit("{x: x * x for x in range(1000)}", number=1000)

def build_with_loop():
    result = {}
    for x in range(1000):
        result[x] = x * x
    return result

loop_time = timeit.timeit(build_with_loop, number=1000)
print(f"Dict comprehension: {comprehension_time:.4f}s (1000 runs)")
print(f"Manual loop        : {loop_time:.4f}s (1000 runs)")

# 14. The __missing__ Hook
# ------------------------------------
# - Subclassing dict and defining __missing__(self, key) lets you customize
#   what happens when a key is looked up with [] and not found - this is
#   actually how defaultdict is implemented under the hood.

print("\n# 14. The __missing__ Hook")
print("# ------------------------------------")

class AutoZeroDict(dict):
    def __missing__(self, key):
        return 0   # instead of raising KeyError, return a default of 0

counter = AutoZeroDict()
counter["a"] += 1   # reads missing "a" as 0 via __missing__, then sets it to 1
counter["a"] += 1
print("AutoZeroDict counting without setdefault/defaultdict:", dict(counter))

print("\n# End of Dictionary Explanation")

