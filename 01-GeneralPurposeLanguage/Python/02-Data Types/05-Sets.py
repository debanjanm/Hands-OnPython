## 0. Characteristics of {Sets}
## 1. Creating {Sets}
## 2. Acessing {Sets}
## 3. Adding {Sets}
## 4. Editing {Sets}
## 5. Deleting {Sets}
## 6. Operations on {Sets}: arithmatic/membership/ loop
## 7. {Sets} Specific Methods: len/sum/min/max/sorted union/Update intersection/Difference copy 
## 8. Advancaed Topics: Set Comprehension, Frozenset

# Python Set Explanation

# 0. Characteristics of Set
# ------------------------------------
# - Sets are used to store multiple items in a single variable.
# - Sets are unordered, unchangeable*, and do not allow duplicate values.
#   *Set items are unchangeable, but you can remove items and add new items.
# - Sets are unordered, so you cannot access items by index.
# - Sets are written with curly braces {}.

print("\n# 0. Characteristics of Set")
print("# ------------------------------------")
print("# - Unordered, unchangeable (items, but set itself is mutable - add/remove), no duplicates, unindexed.")

# 1. Creating Set
# ------------------------------------
# - Sets can be created using curly braces {} or the set() constructor.

print("\n# 1. Creating Set")
print("# ------------------------------------")

# a) Empty Set
empty_set = set() # Important: use set() constructor to create an empty set
print("a) Empty Set:", empty_set, type(empty_set))

not_an_empty_set = {} # This creates an empty dictionary, not an empty set
print("   Not an empty set (creates dictionary):", not_an_empty_set, type(not_an_empty_set))

# b) Set with initial values
fruit_set = {"apple", "banana", "cherry"}
print("\nb) Set with initial values:", fruit_set)

number_set = {1, 2, 3, 4, 5}
print("   Set of numbers:", number_set)

mixed_set = {1, "apple", True, 3.14}
print("   Set with mixed data types:", mixed_set)

# c) Sets automatically remove duplicate values
duplicate_set = {"apple", "banana", "cherry", "apple"} # "apple" is duplicated
print("\nc) Set with duplicates (duplicates are removed):", duplicate_set)

# d) Creating set from other iterables (e.g., list, tuple, string)
list_data = [10, 20, 30, 20] # List with duplicates
set_from_list = set(list_data) # Duplicates will be removed in set
print("\nd) Set from list:", set_from_list)

tuple_data = (1, 2, 3, 2) # Tuple with duplicates
set_from_tuple = set(tuple_data) # Duplicates will be removed
print("   Set from tuple:", set_from_tuple)

string_data = "hello"
set_from_string = set(string_data) # Characters will be unique and unordered
print("   Set from string:", set_from_string)

# 2. Accessing Set Items (Unordered)
# ------------------------------------
# - You cannot access items in a set by referring to an index, as sets are unordered.
# - But you can loop through the set items, or check if a specified value is present in a set, by using the 'in' keyword.

print("\n# 2. Accessing Set Items (Unordered)")
print("# ------------------------------------")

print("Original Set:", fruit_set)

# a) Accessing by index is not supported - will cause TypeError
# first_fruit = fruit_set[0] # This will cause TypeError: 'set' object is not subscriptable

# b) Checking if an item is in the set (membership testing)
print("\nb) Membership testing:")
print("'apple' in fruit_set:", "apple" in fruit_set)
print("'banana' in fruit_set:", "banana" in fruit_set)
print("'orange' in fruit_set:", "orange" in fruit_set) # Item not in set
print("'orange' not in fruit_set:", "orange" not in fruit_set)

# c) Looping through the set
print("\nc) Looping through the set:")
for fruit in fruit_set:
    print("   Fruit:", fruit) # Order may vary as sets are unordered

# 3. Adding Set Items
# ------------------------------------
# - Once a set is created, you cannot change its items, but you can add new items.
# - To add one item to a set use the add() method.
# - To add more than one item to the set, use the update() method.

print("\n# 3. Adding Set Items")
print("# ------------------------------------")

print("Initial Set:", fruit_set)

# a) add() - add a single item
fruit_set.add("orange")
print("a) add('orange'):", fruit_set)

# b) add() - adding an existing item has no effect (sets only store unique values)
fruit_set.add("apple") # 'apple' is already in the set
print("b) add('apple') - no effect:", fruit_set)

# c) update() - add multiple items from another iterable (list, tuple, set)
more_fruits = ["grape", "kiwi", "apple"] # Note: 'apple' is duplicate and already in fruit_set
fruit_set.update(more_fruits) # Adds 'grape', 'kiwi' and ignores the duplicate 'apple'
print("c) update(['grape', 'kiwi', 'apple']):", fruit_set)

# 4. Editing Set Items (Unchangeable Items)
# ------------------------------------
# - Set items are unchangeable, meaning that sets do not support item editing.
# - You can't change existing items in the set directly.
# - If you want to "edit" an item, you would typically remove the item and add a new one.

print("\n# 4. Editing Set Items (Unchangeable Items)")
print("# ------------------------------------")

print("Set before 'edit' (actually remove and add):", fruit_set)

# a) No direct way to edit an item
# fruit_set[0] = "new_apple" # This will cause TypeError: 'set' object is not subscriptable

# b) Simulate 'edit' by removing and adding
fruit_set.remove("banana") # Remove 'banana'
fruit_set.add("mango")    # Add 'mango'
print("b) Simulate 'edit' (remove 'banana', add 'mango'):", fruit_set)

# 5. Deleting Set Items
# ------------------------------------
# - To remove an item in a set, use the remove(), or discard() method.
# - You can also use the pop() method to remove an item, but this method will remove a random item because sets are unordered.
# - The clear() method empties the set.
# - The del keyword will delete the set completely.

print("\n# 5. Deleting Set Items")
print("# ------------------------------------")

print("Set before deletion:", fruit_set)

# a) remove(item) - remove a specified item, raises KeyError if item not found
fruit_set.remove("cherry")
print("a) remove('cherry'):", fruit_set)

# b) remove(item) - trying to remove an item not in set raises KeyError
# fruit_set.remove("blueberry") # This will cause KeyError: 'blueberry'

# c) discard(item) - remove a specified item, does NOT raise error if item not found
fruit_set.discard("kiwi")
print("c) discard('kiwi'):", fruit_set)

fruit_set.discard("blueberry") # 'blueberry' not in set, no error is raised
print("   discard('blueberry') - no error:", fruit_set)

# d) pop() - removes an arbitrary item (since sets are unordered) and returns it
popped_item = fruit_set.pop()
print("d) pop():", fruit_set, "Removed item:", popped_item)

# e) clear() - empty the set
fruit_set.clear()
print("e) clear():", fruit_set)

# Reset fruit_set for further examples
fruit_set = {"apple", "banana", "cherry", "date"}

# 6. Operations on Set: arithmetic (set operations)/membership/ loop
# ------------------------------------

print("\n# 6. Operations on Set: arithmetic (set operations)/membership/ loop")
print("# ------------------------------------")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)

# a) Union - combines elements from both sets (no duplicates)
union_set = set1.union(set2) # Method way
print("\na) Union:")
print("   set1.union(set2):", union_set)
union_set_operator = set1 | set2 # Operator way
print("   set1 | set2:", union_set_operator)

# b) Intersection - elements common to both sets
intersection_set = set1.intersection(set2) # Method way
print("\nb) Intersection:")
print("   set1.intersection(set2):", intersection_set)
intersection_set_operator = set1 & set2 # Operator way
print("   set1 & set2:", intersection_set_operator)

# c) Difference - elements in set1 but not in set2
difference_set = set1.difference(set2) # Method way (set1 - set2)
print("\nc) Difference (set1 - set2):")
print("   set1.difference(set2):", difference_set)
difference_set_operator = set1 - set2 # Operator way (set1 - set2)
print("   set1 - set2:", difference_set_operator)

# d) Symmetric Difference - elements in either set1 or set2, but not in both
symmetric_difference_set = set1.symmetric_difference(set2) # Method way
print("\nd) Symmetric Difference:")
print("   set1.symmetric_difference(set2):", symmetric_difference_set)
symmetric_difference_set_operator = set1 ^ set2 # Operator way
print("   set1 ^ set2:", symmetric_difference_set_operator)

# e) Membership testing
print("\ne) Membership testing:")
print("   3 in set1:", 3 in set1)
print("   6 in set1:", 6 in set1)
print("   6 not in set1:", 6 not in set1)

# f) Looping through a set
print("\nf) Looping through a set:")
for item in set1:
    print("   Item:", item) # Order is not guaranteed

# 7. Set Specific Methods: len/sum/min/max/sorted/union/update/intersection/difference/copy

print("\n# 7. Set Specific Methods: len/sum/min/max/sorted/union/update/intersection/difference/copy")
print("# ------------------------------------")

number_set_methods = {5, 2, 8, 1, 8, 3} # Note: 8 is duplicated in initialization, but will be unique in set
print("Set for methods:", number_set_methods) # Duplicates are already removed

# a) len() - number of elements in the set
print("\na) len(number_set_methods):", len(number_set_methods))

# b) sum() - sum of all elements (numeric set)
print("b) sum(number_set_methods):", sum(number_set_methods))

# c) min() and max() - min/max element in the set
print("c) min(number_set_methods):", min(number_set_methods), ", max(number_set_methods):", max(number_set_methods))

# d) sorted(set) - returns a new sorted list from set (set itself is unchanged)
sorted_list_from_set = sorted(number_set_methods)
print("\nd) sorted(number_set_methods):", sorted_list_from_set, type(sorted_list_from_set))
print("   Original set remains unchanged:", number_set_methods)

# e) union() and update() - union methods
set_union_example = {10, 20, 30}
print("\ne) union() and update():")
print("   Original set:", number_set_methods, "Union set:", set_union_example)
new_union_set = number_set_methods.union(set_union_example) # Returns a new set
print("   number_set_methods.union(set_union_example):", new_union_set)
number_set_methods.update(set_union_example) # Modifies number_set_methods in place
print("   number_set_methods.update(set_union_example) - modifies original:", number_set_methods)
# Reset for next examples
number_set_methods = {5, 2, 8, 1, 3, 8} # Re-initialize, duplicates will be auto-removed
set_union_example = {10, 20, 30}

# f) intersection() and intersection_update() - intersection methods
set_intersection_example = {3, 8, 9}
print("\nf) intersection() and intersection_update():")
print("   Original set:", number_set_methods, "Intersection set:", set_intersection_example)
new_intersection_set = number_set_methods.intersection(set_intersection_example) # Returns a new set
print("   number_set_methods.intersection(set_intersection_example):", new_intersection_set)
number_set_methods.intersection_update(set_intersection_example) # Modifies number_set_methods in place
print("   number_set_methods.intersection_update(set_intersection_example) - modifies original:", number_set_methods)
# Reset
number_set_methods = {5, 2, 8, 1, 3, 8}
set_intersection_example = {3, 8, 9}

# g) difference() and difference_update() - difference methods
set_difference_example = {1, 2, 9}
print("\ng) difference() and difference_update():")
print("   Original set:", number_set_methods, "Difference set:", set_difference_example)
new_difference_set = number_set_methods.difference(set_difference_example) # Returns a new set
print("   number_set_methods.difference(set_difference_example):", new_difference_set)
number_set_methods.difference_update(set_difference_example) # Modifies number_set_methods in place
print("   number_set_methods.difference_update(set_difference_example) - modifies original:", number_set_methods)
# Reset
number_set_methods = {5, 2, 8, 1, 3, 8}
set_difference_example = {1, 2, 9}

# h) copy() - returns a shallow copy of the set
copied_set = number_set_methods.copy()
print("\nh) copy(): Original:", number_set_methods, ", Copied set:", copied_set)
print("   copied_set is number_set_methods:", copied_set is number_set_methods) # Check if it is the same object (should be False)
print("   copied_set == number_set_methods:", copied_set == number_set_methods) # Check if values are the same (should be True)

# 8. Advanced Topics: Set Comprehension, Frozenset

print("\n# 8. Advanced Topics: Set Comprehension, Frozenset")
print("# ------------------------------------")

# a) Set Comprehension - concise way to create sets

print("\na) Set Comprehension:")

# Example 1: Create a set of squares of numbers 0-9
squares_set = {x**2 for x in range(10)}
print("   Example 1: Squares of numbers 0-9:", squares_set)

# Example 2: Create a set of even numbers from 0-9
even_numbers_set = {x for x in range(10) if x % 2 == 0}
print("   Example 2: Even numbers from 0-9:", even_numbers_set)

# Example 3: Create a set of lengths of fruits in fruit_set (initialized earlier)
fruit_lengths_set = {len(fruit) for fruit in fruit_set}
print("   Example 3: Lengths of fruits in fruit_set:", fruit_lengths_set)

# b) Frozenset - immutable version of set

print("\nb) Frozenset:")

# i) Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4]) # Created from a list, can be from any iterable
print("   i) Creating frozenset from list:", frozen_set, type(frozen_set))

# ii) Frozensets are immutable - cannot add or remove items
# frozen_set.add(5) # AttributeError: 'frozenset' object has no attribute 'add'
# frozen_set.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'

# iii) Operations on frozensets - still supports operations like union, intersection, etc., but they return new frozensets or sets
frozen_set1 = frozenset([1, 2, 3])
frozen_set2 = frozenset([3, 4, 5])
frozen_union = frozen_set1.union(frozen_set2) # Returns a new frozenset
print("   iii) Operations - frozen_set1.union(frozen_set2):", frozen_union, type(frozen_union))

# iv) Why use frozensets? - Can be used as keys in dictionaries or elements in other sets (because they are hashable due to immutability)
dict_with_frozenset_key = {frozen_set1: "value"} # Frozenset as dictionary key
print("   iv) Frozenset as dictionary key:", dict_with_frozenset_key)

set_of_frozensets = {frozen_set1, frozen_set2} # Frozenset as element in another set
print("   v) Set of frozensets:", set_of_frozensets)

# 9. Hash Table Internals & O(1) Average Membership
# ------------------------------------
# - A set is backed by a hash table: each element's hash(x) determines
#   which "bucket" (slot) it's stored in.
# - Membership testing (`x in my_set`) computes hash(x) and jumps straight
#   to that bucket - O(1) on average, versus O(n) for `x in my_list`
#   (which must scan every item).
# - This is why only HASHABLE (and thus generally immutable) objects can be
#   set elements - unhashable types like list have no stable hash to bucket by.

print("\n# 9. Hash Table Internals & O(1) Average Membership")
print("# ------------------------------------")

import timeit

big_list = list(range(100_000))
big_set = set(big_list)

list_lookup = timeit.timeit("99_999 in big_list", globals={"big_list": big_list}, number=1000)
set_lookup = timeit.timeit("99_999 in big_set", globals={"big_set": big_set}, number=1000)
print(f"'x in list' (O(n), scans every item): {list_lookup:.5f}s (1000 lookups)")
print(f"'x in set'  (O(1) average, hash jump): {set_lookup:.5f}s (1000 lookups)")

try:
    {[1, 2]}   # a list has no stable hash - can't be a set element
except TypeError as e:
    print("\nSet of a list fails:", e)

# 10. frozenset - Immutable, Hashable Sets
# ------------------------------------
# - frozenset is the immutable counterpart to set: same hash-table lookups,
#   but no add()/remove(), which makes it hashable - so a frozenset can be
#   used as a dict key or nested inside another set (a plain set cannot).

print("\n# 10. frozenset - Immutable, Hashable Sets")
print("# ------------------------------------")

frozen = frozenset([1, 2, 3])
print("frozenset([1, 2, 3]):", frozen, "hashable:", hash(frozen) is not None)

set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print("Set of frozensets:", set_of_sets)

try:
    {set([1, 2])}   # a mutable set cannot itself be a set element
except TypeError as e:
    print("Set of a (mutable) set fails:", e)

# 11. Set Operation Complexity (Conceptual)
# ------------------------------------
# - union/intersection/difference/symmetric_difference generally run in
#   O(len(set1) + len(set2)) - each hash table is scanned once.
# - Hash collisions (two different elements landing in the same bucket)
#   are resolved internally via open addressing/probing - amortized O(1)
#   per operation still holds on average, but a pathological case with many
#   collisions can degrade towards O(n). Python's hash randomization
#   (PYTHONHASHSEED) helps guard against adversarial collision attacks.

print("\n# 11. Set Operation Complexity (Conceptual)")
print("# ------------------------------------")
print("# - membership (in)         : O(1) average")
print("# - add() / remove()        : O(1) average")
print("# - union / intersection    : O(len(a) + len(b))")
print("# - Collisions are handled internally via probing; worst case degrades")
print("#   to O(n), but that's rare in practice thanks to hash randomization.")

# 12. Fast Deduplication: set vs list
# ------------------------------------
# - Deduplicating with `list(set(items))` is O(n) - one pass through items,
#   each with an O(1) average set insertion.
# - The naive "check if already in a list, then append" approach is O(n^2) -
#   each membership check scans the growing list linearly.

print("\n# 12. Fast Deduplication: set vs list")
print("# ------------------------------------")

items_with_dupes = [1, 2, 2, 3, 4, 4, 4, 5]

def dedupe_with_list(items):
    seen = []
    for item in items:
        if item not in seen:   # O(n) scan every time -> O(n^2) overall
            seen.append(item)
    return seen

def dedupe_with_set(items):
    return list(set(items))    # O(n) overall, but does not preserve order

print("dedupe_with_list():", dedupe_with_list(items_with_dupes), "(preserves order, O(n^2))")
print("dedupe_with_set() :", sorted(dedupe_with_set(items_with_dupes)), "(O(n), order not preserved)")
print("# For order-preserving O(n) dedup, use dict.fromkeys(items) instead (see Dictionary file).")

print("\n# End of Set Explanation")

