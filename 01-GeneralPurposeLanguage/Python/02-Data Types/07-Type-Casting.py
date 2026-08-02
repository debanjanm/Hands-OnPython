# Python Type Casting: Converting Between Data Types

# Introduction: Type Casting in Python
# ------------------------------------
# Type casting (also known as type conversion) is the process of changing the data type of a value from one type to another.
# Python supports two types of type casting:
# 1. Implicit Type Casting (Automatic): Python automatically converts data types in certain operations.
# 2. Explicit Type Casting (Manual): Users manually convert data types using built-in functions.

print("# Introduction: Type Casting in Python")
print("# ------------------------------------")
print("# Implicit vs. Explicit Type Casting:")
print("# - Implicit: Automatic type conversion by Python.")
print("# - Explicit: Manual type conversion using functions like int(), float(), str(), etc.")

# 1. Casting to Integer (int)
# ------------------------------------
# - int() function converts a value to an integer data type.
# - Can convert from: float, string (representing integer), boolean.

print("\n# 1. Casting to Integer (int)")
print("# ------------------------------------")

# a) From float to integer (truncates decimal part)
float_num = 3.99
int_num_from_float = int(float_num)
print("a) From float:")
print("   Original value:", float_num, "Type:", type(float_num))
print("   Casted to int:", int_num_from_float, "Type:", type(int_num_from_float))
print("   Note: Decimal part is truncated.")

# b) From string to integer (string must represent an integer)
str_num = "123"
int_num_from_str = int(str_num)
print("\nb) From string:")
print("   Original value:", str_num, "Type:", type(str_num))
print("   Casted to int:", int_num_from_str, "Type:", type(int_num_from_str))

# Example of invalid string to int conversion (will raise ValueError)
# invalid_str_num = "123.45"
# int_invalid_str = int(invalid_str_num) # This will cause ValueError: invalid literal for int() with base 10: '123.45'
# print("   Trying to cast invalid string to int:", int_invalid_str) # Uncommenting this will cause error

# c) From boolean to integer (True becomes 1, False becomes 0)
bool_val_true = True
int_from_bool_true = int(bool_val_true)
print("\nc) From boolean (True):")
print("   Original value:", bool_val_true, "Type:", type(bool_val_true))
print("   Casted to int:", int_from_bool_true, "Type:", type(int_from_bool_true))

bool_val_false = False
int_from_bool_false = int(bool_val_false)
print("\n   From boolean (False):")
print("   Original value:", bool_val_false, "Type:", type(bool_val_false))
print("   Casted to int:", int_from_bool_false, "Type:", type(int_from_bool_false))

# 2. Casting to Float (float)
# ------------------------------------
# - float() function converts a value to a floating-point number.
# - Can convert from: integer, string (representing float or integer), boolean.

print("\n# 2. Casting to Float (float)")
print("# ------------------------------------")

# a) From integer to float
int_num = 10
float_num_from_int = float(int_num)
print("a) From integer:")
print("   Original value:", int_num, "Type:", type(int_num))
print("   Casted to float:", float_num_from_int, "Type:", type(float_num_from_int))

# b) From string to float (string can represent float or integer)
str_float_num = "3.14"
float_num_from_str_float = float(str_float_num)
print("\nb) From string (float representation):")
print("   Original value:", str_float_num, "Type:", type(str_float_num))
print("   Casted to float:", float_num_from_str_float, "Type:", type(float_num_from_str_float))

str_int_num = "123"
float_num_from_str_int = float(str_int_num)
print("\n   From string (integer representation):")
print("   Original value:", str_int_num, "Type:", type(str_int_num))
print("   Casted to float:", float_num_from_str_int, "Type:", type(float_num_from_str_int))

# Example of invalid string to float conversion (will raise ValueError)
# invalid_str_float = "abc"
# float_invalid_str = float(invalid_str_float) # This will cause ValueError: could not convert string to float: 'abc'
# print("   Trying to cast invalid string to float:", float_invalid_str) # Uncommenting this will cause error

# c) From boolean to float (True becomes 1.0, False becomes 0.0)
bool_val_true_float = True
float_from_bool_true = float(bool_val_true_float)
print("\nc) From boolean (True):")
print("   Original value:", bool_val_true_float, "Type:", type(bool_val_true_float))
print("   Casted to float:", float_from_bool_true, "Type:", type(float_from_bool_true))

bool_val_false_float = False
float_from_bool_false = float(bool_val_false_float)
print("\n   From boolean (False):")
print("   Original value:", bool_val_false_float, "Type:", type(bool_val_false_float))
print("   Casted to float:", float_from_bool_false, "Type:", type(float_from_bool_false))

# 3. Casting to String (str)
# ------------------------------------
# - str() function converts a value to a string data type.
# - Can convert from: integer, float, boolean, list, tuple, dictionary, set, and many other types.

print("\n# 3. Casting to String (str)")
print("# ------------------------------------")

# a) From integer to string
int_num_str = 456
str_from_int = str(int_num_str)
print("a) From integer:")
print("   Original value:", int_num_str, "Type:", type(int_num_str))
print("   Casted to str:", str_from_int, "Type:", type(str_from_int))

# b) From float to string
float_num_str = 78.90
str_from_float = str(float_num_str)
print("\nb) From float:")
print("   Original value:", float_num_str, "Type:", type(float_num_str))
print("   Casted to str:", str_from_float, "Type:", type(str_from_float))

# c) From boolean to string
bool_val_str = True
str_from_bool = str(bool_val_str)
print("\nc) From boolean:")
print("   Original value:", bool_val_str, "Type:", type(bool_val_str))
print("   Casted to str:", str_from_bool, "Type:", type(str_from_bool))

# d) From list to string (string representation of the list)
list_data = [1, 2, 3]
str_from_list = str(list_data)
print("\nd) From list:")
print("   Original value:", list_data, "Type:", type(list_data))
print("   Casted to str:", str_from_list, "Type:", type(str_from_list))

# e) From tuple to string (string representation of the tuple)
tuple_data = (4, 5, 6)
str_from_tuple = str(tuple_data)
print("\ne) From tuple:")
print("   Original value:", tuple_data, "Type:", type(tuple_data))
print("   Casted to str:", str_from_tuple, "Type:", type(str_from_tuple))

# f) From dictionary to string (string representation of the dictionary)
dict_data = {"a": 1, "b": 2}
str_from_dict = str(dict_data)
print("\nf) From dictionary:")
print("   Original value:", dict_data, "Type:", type(dict_data))
print("   Casted to str:", str_from_dict, "Type:", type(str_from_dict))

# g) From set to string (string representation of the set)
set_data = {7, 8, 9}
str_from_set = str(set_data)
print("\ng) From set:")
print("   Original value:", set_data, "Type:", type(set_data))
print("   Casted to str:", str_from_set, "Type:", type(str_from_set))

# 4. Casting to Boolean (bool)
# ------------------------------------
# - bool() function converts a value to a boolean data type (True or False).
# - Most values are True, except for:
#   - False, None, 0, 0.0, empty strings (""), empty lists ([]), empty tuples (()), empty dictionaries ({}), empty sets (set()).

print("\n# 4. Casting to Boolean (bool)")
print("# ------------------------------------")

# a) From integer to boolean (0 is False, any other integer is True)
int_zero = 0
bool_from_int_zero = bool(int_zero)
print("a) From integer (0):")
print("   Original value:", int_zero, "Type:", type(int_zero))
print("   Casted to bool:", bool_from_int_zero, "Type:", type(bool_from_int_zero))

int_positive = 10
bool_from_int_positive = bool(int_positive)
print("\n   From integer (positive):")
print("   Original value:", int_positive, "Type:", type(int_positive))
print("   Casted to bool:", bool_from_int_positive, "Type:", type(bool_from_int_positive))

int_negative = -5
bool_from_int_negative = bool(int_negative)
print("\n   From integer (negative):")
print("   Original value:", int_negative, "Type:", type(int_negative))
print("   Casted to bool:", bool_from_int_negative, "Type:", type(bool_from_int_negative))

# b) From float to boolean (0.0 is False, any other float is True)
float_zero = 0.0
bool_from_float_zero = bool(float_zero)
print("\nb) From float (0.0):")
print("   Original value:", float_zero, "Type:", type(float_zero))
print("   Casted to bool:", bool_from_float_zero, "Type:", type(bool_from_float_zero))

float_nonzero = 3.14
bool_from_float_nonzero = bool(float_nonzero)
print("\n   From float (non-zero):")
print("   Original value:", float_nonzero, "Type:", type(float_nonzero))
print("   Casted to bool:", bool_from_float_nonzero, "Type:", type(bool_from_float_nonzero))

# c) From string to boolean (empty string "" is False, any non-empty string is True)
str_empty = ""
bool_from_str_empty = bool(str_empty)
print("\nc) From string (empty):")
print("   Original value:", str_empty, "Type:", type(str_empty))
print("   Casted to bool:", bool_from_str_empty, "Type:", type(bool_from_str_empty))

str_nonempty = "Hello"
bool_from_str_nonempty = bool(str_nonempty)
print("\n   From string (non-empty):")
print("   Original value:", str_nonempty, "Type:", type(str_nonempty))
print("   Casted to bool:", bool_from_str_nonempty, "Type:", type(bool_from_str_nonempty))

# d) From list to boolean (empty list [] is False, any non-empty list is True)
list_empty = []
bool_from_list_empty = bool(list_empty)
print("\nd) From list (empty):")
print("   Original value:", list_empty, "Type:", type(list_empty))
print("   Casted to bool:", bool_from_list_empty, "Type:", type(bool_from_list_empty))

list_nonempty = [1, 2]
bool_from_list_nonempty = bool(list_nonempty)
print("\n   From list (non-empty):")
print("   Original value:", list_nonempty, "Type:", type(list_nonempty))
print("   Casted to bool:", bool_from_list_nonempty, "Type:", type(bool_from_list_nonempty))

# e) From tuple to boolean (empty tuple () is False, any non-empty tuple is True)
tuple_empty = ()
bool_from_tuple_empty = bool(tuple_empty)
print("\ne) From tuple (empty):")
print("   Original value:", tuple_empty, "Type:", type(tuple_empty))
print("   Casted to bool:", bool_from_tuple_empty, "Type:", type(bool_from_tuple_empty))

tuple_nonempty = (1, 2)
bool_from_tuple_nonempty = bool(tuple_nonempty)
print("\n   From tuple (non-empty):")
print("   Original value:", tuple_nonempty, "Type:", type(tuple_nonempty))
print("   Casted to bool:", bool_from_tuple_nonempty, "Type:", type(bool_from_tuple_nonempty))

# f) From dictionary to boolean (empty dict {} is False, any non-empty dict is True)
dict_empty = {}
bool_from_dict_empty = bool(dict_empty)
print("\nf) From dictionary (empty):")
print("   Original value:", dict_empty, "Type:", type(dict_empty))
print("   Casted to bool:", bool_from_dict_empty, "Type:", type(bool_from_dict_empty))

dict_nonempty = {"a": 1}
bool_from_dict_nonempty = bool(dict_nonempty)
print("\n   From dictionary (non-empty):")
print("   Original value:", dict_nonempty, "Type:", type(dict_nonempty))
print("   Casted to bool:", bool_from_dict_nonempty, "Type:", type(bool_from_dict_nonempty))

# g) From set to boolean (empty set set() is False, any non-empty set is True)
set_empty = set()
bool_from_set_empty = bool(set_empty)
print("\ng) From set (empty):")
print("   Original value:", set_empty, "Type:", type(set_empty))
print("   Casted to bool:", bool_from_set_empty, "Type:", type(bool_from_set_empty))

set_nonempty = {1}
bool_from_set_nonempty = bool(set_nonempty)
print("\n   From set (non-empty):")
print("   Original value:", set_nonempty, "Type:", type(set_nonempty))
print("   Casted to bool:", bool_from_set_nonempty, "Type:", type(bool_from_set_nonempty))

# 5. Casting to List (list)
# ------------------------------------
# - list() function converts a value to a list data type.
# - Can convert from: tuple, string (creates list of characters), set, dictionary (keys, values, or items).

print("\n# 5. Casting to List (list)")
print("# ------------------------------------")

# a) From tuple to list
tuple_for_list = (10, 20, 30)
list_from_tuple_cast = list(tuple_for_list)
print("a) From tuple:")
print("   Original value:", tuple_for_list, "Type:", type(tuple_for_list))
print("   Casted to list:", list_from_tuple_cast, "Type:", type(list_from_tuple_cast))

# b) From string to list (list of characters)
str_for_list = "Python"
list_from_str_cast = list(str_for_list)
print("\nb) From string:")
print("   Original value:", str_for_list, "Type:", type(str_for_list))
print("   Casted to list:", list_from_str_cast, "Type:", type(list_from_str_cast))

# c) From set to list (order is not guaranteed as sets are unordered)
set_for_list = {1, 2, 3}
list_from_set_cast = list(set_for_list)
print("\nc) From set:")
print("   Original value:", set_for_list, "Type:", type(set_for_list))
print("   Casted to list:", list_from_set_cast, "Type:", type(list_from_set_cast))
print("   Note: Order might not be preserved from set.")

# d) From dictionary to list (keys, values, or items)
dict_for_list = {"a": 1, "b": 2, "c": 3}

list_from_dict_keys = list(dict_for_list) # By default, it iterates through keys
print("\nd) From dictionary (keys):")
print("   Original value:", dict_for_list, "Type:", type(dict_for_list))
print("   Casted to list (keys):", list_from_dict_keys, "Type:", type(list_from_dict_keys))

list_from_dict_values = list(dict_for_list.values()) # Iterate through values
print("\n   From dictionary (values):")
print("   Original value:", dict_for_list, "Type:", type(dict_for_list))
print("   Casted to list (values):", list_from_dict_values, "Type:", type(list_from_dict_values))

list_from_dict_items = list(dict_for_list.items()) # Iterate through key-value pairs (items)
print("\n   From dictionary (items):")
print("   Original value:", dict_for_list, "Type:", type(dict_for_list))
print("   Casted to list (items):", list_from_dict_items, "Type:", type(list_from_dict_items))

# 6. Casting to Tuple (tuple)
# ------------------------------------
# - tuple() function converts a value to a tuple data type.
# - Can convert from: list, string (creates tuple of characters), set, dictionary (keys, values, or items).

print("\n# 6. Casting to Tuple (tuple)")
print("# ------------------------------------")

# a) From list to tuple
list_for_tuple = [1, 2, 3]
tuple_from_list_cast = tuple(list_for_tuple)
print("a) From list:")
print("   Original value:", list_for_tuple, "Type:", type(list_for_tuple))
print("   Casted to tuple:", tuple_from_list_cast, "Type:", type(tuple_from_list_cast))

# b) From string to tuple (tuple of characters)
str_for_tuple = "TupleStr"
tuple_from_str_cast = tuple(str_for_tuple)
print("\nb) From string:")
print("   Original value:", str_for_tuple, "Type:", type(str_for_tuple))
print("   Casted to tuple:", tuple_from_str_cast, "Type:", type(tuple_from_str_cast))

# c) From set to tuple (order is not guaranteed as sets are unordered)
set_for_tuple = {4, 5, 6}
tuple_from_set_cast = tuple(set_for_tuple)
print("\nc) From set:")
print("   Original value:", set_for_tuple, "Type:", type(set_for_tuple))
print("   Casted to tuple:", tuple_from_set_cast, "Type:", type(tuple_from_set_cast))
print("   Note: Order might not be preserved from set.")

# d) From dictionary to tuple (keys, values, or items)
dict_for_tuple = {"d": 4, "e": 5, "f": 6}

tuple_from_dict_keys = tuple(dict_for_tuple) # By default, it iterates through keys
print("\nd) From dictionary (keys):")
print("   Original value:", dict_for_tuple, "Type:", type(dict_for_tuple))
print("   Casted to tuple (keys):", tuple_from_dict_keys, "Type:", type(tuple_from_dict_keys))

tuple_from_dict_values = tuple(dict_for_tuple.values()) # Iterate through values
print("\n   From dictionary (values):")
print("   Original value:", dict_for_tuple, "Type:", type(dict_for_tuple))
print("   Casted to tuple (values):", tuple_from_dict_values, "Type:", type(tuple_from_dict_values))

tuple_from_dict_items = tuple(dict_for_tuple.items()) # Iterate through key-value pairs (items)
print("\n   From dictionary (items):")
print("   Original value:", dict_for_tuple, "Type:", type(dict_for_tuple))
print("   Casted to tuple (items):", tuple_from_dict_items, "Type:", type(tuple_from_dict_items))

# 7. Casting to Set (set)
# ------------------------------------
# - set() function converts a value to a set data type.
# - Can convert from: list, tuple, string (creates set of unique characters), dictionary (keys or values).
# - Duplicates are automatically removed in sets.

print("\n# 7. Casting to Set (set)")
print("# ------------------------------------")

# a) From list to set (removes duplicates and unordered)
list_for_set = [1, 2, 2, 3, 4, 4, 4] # List with duplicates
set_from_list_cast = set(list_for_set)
print("a) From list:")
print("   Original value:", list_for_set, "Type:", type(list_for_set))
print("   Casted to set:", set_from_list_cast, "Type:", type(set_from_list_cast))
print("   Note: Duplicates removed, order is not preserved.")

# b) From tuple to set (removes duplicates and unordered)
tuple_for_set = (5, 6, 6, 7, 8, 8, 8) # Tuple with duplicates
set_from_tuple_cast = set(tuple_for_set)
print("\nb) From tuple:")
print("   Original value:", tuple_for_set, "Type:", type(tuple_for_set))
print("   Casted to set:", set_from_tuple_cast, "Type:", type(set_from_tuple_cast))
print("   Note: Duplicates removed, order is not preserved.")

# c) From string to set (set of unique characters, unordered)
str_for_set = "Mississippi" # String with duplicate characters
set_from_str_cast = set(str_for_set)
print("\nc) From string:")
print("   Original value:", str_for_set, "Type:", type(str_for_set))
print("   Casted to set:", set_from_str_cast, "Type:", type(set_from_str_cast))
print("   Note: Unique characters, order is not preserved.")

# d) From dictionary to set (keys or values)
dict_for_set = {"g": 7, "h": 8, "i": 9, "j": 7} # Dictionary with duplicate values (for demonstration)

set_from_dict_keys = set(dict_for_set) # By default, it iterates through keys
print("\nd) From dictionary (keys):")
print("   Original value:", dict_for_set, "Type:", type(dict_for_set))
print("   Casted to set (keys):", set_from_dict_keys, "Type:", type(set_from_dict_keys))
print("   Note: Keys are used, order is not preserved.")

set_from_dict_values = set(dict_for_set.values()) # Iterate through values
print("\n   From dictionary (values):")
print("   Original value:", dict_for_set, "Type:", type(dict_for_set))
print("   Casted to set (values):", set_from_dict_values, "Type:", type(set_from_dict_values))
print("   Note: Values are used, duplicates removed, order is not preserved.")

# 8. Casting to Dictionary (dict)
# ------------------------------------
# - dict() function converts a value to a dictionary data type.
# - Can convert from: list of tuples (where each tuple is key-value pair), zip objects.

print("\n# 8. Casting to Dictionary (dict)")
print("# ------------------------------------")

# a) From list of tuples to dictionary (each tuple is a key-value pair)
list_of_tuples_for_dict = [("key1", 10), ("key2", 20), ("key3", 30)]
dict_from_list_of_tuples = dict(list_of_tuples_for_dict)
print("a) From list of tuples:")
print("   Original value:", list_of_tuples_for_dict, "Type:", type(list_of_tuples_for_dict))
print("   Casted to dict:", dict_from_list_of_tuples, "Type:", type(dict_from_list_of_tuples))

# b) From zip object to dictionary (zip of keys and values)
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
zipped_pairs = zip(keys, values) # Create a zip object of key-value pairs
dict_from_zip = dict(zipped_pairs)
print("\nb) From zip object:")
print("   Original zip object:", zipped_pairs, "Type:", type(zipped_pairs)) # zip object itself
print("   List of zipped pairs (for visualization):", list(zipped_pairs)) # List of tuples from zip
print("   Casted to dict:", dict_from_zip, "Type:", type(dict_from_zip))

# Example of invalid structure for dictionary casting (will raise ValueError)
# invalid_list_for_dict = [(1, 2, 3), (4, 5)] # Tuples not consistently key-value pairs
# dict_invalid_cast = dict(invalid_list_for_dict) # This will cause ValueError: dictionary update sequence element #0 has length 3; 2 is required
# print("   Trying to cast invalid list of tuples to dict:", dict_invalid_cast) # Uncommenting this will cause error

# 9. Implicit vs Explicit Conversion Gotchas
# ------------------------------------
# - Implicit casting only happens in numeric contexts Python considers safe
#   (e.g. int + float -> float). It never happens between unrelated types
#   like str and int - those always need explicit casting.
# - bool("False") is True! Any non-empty string is truthy, including the
#   string "False" - bool() on a string only checks emptiness, it does not
#   parse the text.
# - int("3.5") raises ValueError - int() cannot parse a decimal point
#   directly from a string. Go through float() first: int(float("3.5")).
# - int() strips surrounding WHITESPACE from a string automatically, but it
#   does not tolerate other stray characters.

print("\n# 9. Implicit vs Explicit Conversion Gotchas")
print("# ------------------------------------")

implicit_result = 5 + 2.5   # int implicitly promoted to float for the operation
print("5 + 2.5 =", implicit_result, ", Type:", type(implicit_result), "(implicit int -> float)")

print("\nbool('False') =", bool("False"), "(gotcha: non-empty string is always truthy!)")
print("bool('') =", bool(""), "(only an EMPTY string is falsy)")

try:
    int("3.5")   # int() can't parse a decimal point in a string directly
except ValueError as e:
    print("\nint('3.5') fails:", e)
print("int(float('3.5')) works instead:", int(float("3.5")))

print("\nint('  42  ') strips whitespace:", int("  42  "))
try:
    int("42abc")   # whitespace is fine, but other stray characters are not
except ValueError as e:
    print("int('42abc') fails:", e)

# 10. Custom Casting via Dunder Methods
# ------------------------------------
# - A class controls how built-in casting functions treat its instances by
#   defining the matching dunder method:
#   __int__    -> called by int(obj)
#   __float__  -> called by float(obj)
#   __str__    -> called by str(obj) / print(obj)
#   __bool__   -> called by bool(obj) and in truthiness checks (if obj:)
# - If __bool__ isn't defined, Python falls back to __len__ (0 -> False),
#   and if neither exists, every instance is truthy by default.

print("\n# 10. Custom Casting via Dunder Methods")
print("# ------------------------------------")

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __int__(self):
        return self.cents // 100          # int(Money(...)) -> whole dollars

    def __float__(self):
        return self.cents / 100           # float(Money(...)) -> dollars.cents

    def __str__(self):
        return f"${self.cents / 100:.2f}"  # str(Money(...)) / print(Money(...))

    def __bool__(self):
        return self.cents != 0            # bool(Money(...)) -> False only if zero

wallet = Money(1050)
empty_wallet = Money(0)

print("int(wallet)   :", int(wallet))
print("float(wallet) :", float(wallet))
print("str(wallet)   :", str(wallet))
print("print(wallet) :", wallet)          # print() calls __str__ implicitly
print("bool(wallet)  :", bool(wallet))
print("bool(empty_wallet):", bool(empty_wallet))
print("'wallet is truthy' check:", "yes" if wallet else "no")

print("\n# Conclusion: Type Casting in Python")
print("# ------------------------------------")
print("# Type casting is essential for converting data between different types in Python.")
print("# It allows for flexible data manipulation and is crucial for various operations.")
print("# Be mindful of potential errors during explicit casting, especially when converting strings to numbers.")

