# 01. Primitive Data Types
# 02. Numeric - Integer, Float, Complex
# 03. Boolean
# 04. None 

# 01. Primitive Data Types
# ------------------------------------
# - Primitive data types are the most basic data types available in a programming language.
# - They represent single values directly in memory and are the building blocks for more complex data structures.
# - Python's primitive data types include numerics (integers, floats, complex numbers), booleans, and the special type None.
# - Understanding primitive types is fundamental as they are used extensively in all Python programs.

print("# 01. Primitive Data Types")
print("# ------------------------------------")
print("# - Basic data types representing single values.")
print("# - Building blocks for complex data structures.")
print("# - Python's primitive types: Numeric (int, float, complex), Boolean, None.")
print("# - Fundamental for all Python programs.")

# 02. Numeric - Integer, Float, Complex
# ------------------------------------
# - Numeric types in Python represent numerical values.
# - Python supports three main numeric types:
#   - Integer (`int`): Represents whole numbers, can be positive, negative, or zero, and of unlimited length.
#   - Float (`float`): Represents floating-point numbers (numbers with a decimal point).  Use for real numbers, precision depends on system architecture.
#   - Complex (`complex`): Represents complex numbers in the form a + bj, where 'a' is the real part and 'b' is the imaginary part, and 'j' is the imaginary unit.

print("\n# 02. Numeric - Integer, Float, Complex")
print("# ------------------------------------")
print("# - Represent numerical values.")
print("# - Three main numeric types:")
print("#   - Integer (int): Whole numbers, unlimited length.")
print("#   - Float (float): Floating-point numbers, decimal numbers.")
print("#   - Complex (complex): Complex numbers, a + bj.")

# a) Integer (int)
print("\n# a) Integer (int)")
print("# ---------------")
print("# - Whole numbers, positive, negative, or zero, unlimited length.")

integer_example_1 = 100
integer_example_2 = -5
integer_example_3 = 0
integer_example_4 = 12345678901234567890  # Very large integer

print("\n# Examples:")
print("integer_example_1 =", integer_example_1, ", Type:", type(integer_example_1))
print("integer_example_2 =", integer_example_2, ", Type:", type(integer_example_2))
print("integer_example_3 =", integer_example_3, ", Type:", type(integer_example_3))
print("integer_example_4 =", integer_example_4, ", Type:", type(integer_example_4))
print("# Operations: Arithmetic operations (+, -, *, /, //, %, **), bitwise operations, etc.")
print("# Common Uses: Counters, indices, quantities, any whole number value.")

# b) Float (float)
print("\n# b) Float (float)")
print("# -------------")
print("# - Floating-point numbers, numbers with a decimal point.")
print("# - Represents real numbers, precision depends on system architecture.")

float_example_1 = 3.14
float_example_2 = -0.001
float_example_3 = 2.0
float_example_4 = 1.79e308  # Maximum representable float value (approximately, system dependent)

print("\n# Examples:")
print("float_example_1 =", float_example_1, ", Type:", type(float_example_1))
print("float_example_2 =", float_example_2, ", Type:", type(float_example_2))
print("float_example_3 =", float_example_3, ", Type:", type(float_example_3))
print("float_example_4 =", float_example_4, ", Type:", type(float_example_4))
print("# Operations: Arithmetic operations, mathematical functions (from math module).")
print("# Common Uses: Representing measurements, ratios, real numbers, decimal values.")

# c) Complex (complex)
print("\n# c) Complex (complex)")
print("# ---------------")
print("# - Complex numbers in the form a + bj, where 'j' is the imaginary unit.")
print("# - 'a' is the real part, 'b' is the imaginary part.")

complex_example_1 = 2 + 3j
complex_example_2 = -1.5 - 0.5j
complex_example_3 = complex(5, -2) # Using complex constructor
complex_example_4 = 4j # Real part is 0

print("\n# Examples:")
print("complex_example_1 =", complex_example_1, ", Type:", type(complex_example_1))
print("complex_example_2 =", complex_example_2, ", Type:", type(complex_example_2))
print("complex_example_3 =", complex_example_3, ", Type:", type(complex_example_3))
print("complex_example_4 =", complex_example_4, ", Type:", type(complex_example_4))
print("# Attributes: .real (real part), .imag (imaginary part).")
print("   Real part of complex_example_1:", complex_example_1.real)
print("   Imaginary part of complex_example_1:", complex_example_1.imag)
print("# Operations: Arithmetic operations, complex number specific functions (from cmath module).")
print("# Common Uses: Scientific computing, engineering, mathematics, especially in fields dealing with frequency domain, quantum mechanics etc.")

# 03. Boolean
# ------------------------------------
# - Boolean type (`bool`) represents truth values.
# - It can have one of two values: `True` or `False` (case-sensitive).
# - Booleans are often the result of comparison operations or logical expressions.
# - In numerical contexts, `True` is often treated as 1 and `False` as 0.

print("\n# 03. Boolean")
print("# ------------------------------------")
print("# - Represents truth values: True or False (case-sensitive).")
print("# - Result of comparison operations or logical expressions.")
print("# - True often treated as 1, False as 0 in numeric context.")

boolean_example_1 = True
boolean_example_2 = False
boolean_example_3 = (5 > 3) # Result of a comparison
boolean_example_4 = bool(0) # Boolean conversion of 0 (False)
boolean_example_5 = bool(1) # Boolean conversion of 1 (True)
boolean_example_6 = bool("Hello") # Boolean conversion of non-empty string (True)
boolean_example_7 = bool("") # Boolean conversion of empty string (False)

print("\n# Examples:")
print("boolean_example_1 =", boolean_example_1, ", Type:", type(boolean_example_1))
print("boolean_example_2 =", boolean_example_2, ", Type:", type(boolean_example_2))
print("boolean_example_3 =", boolean_example_3, ", Type:", type(boolean_example_3))
print("boolean_example_4 =", boolean_example_4, ", Type:", type(boolean_example_4))
print("boolean_example_5 =", boolean_example_5, ", Type:", type(boolean_example_5))
print("boolean_example_6 =", boolean_example_6, ", Type:", type(boolean_example_6))
print("boolean_example_7 =", boolean_example_7, ", Type:", type(boolean_example_7))
print("# Operations: Logical operations (and, or, not).")
print("# Common Uses: Conditional statements, flags, logical evaluations, controlling program flow.")

# 04. None
# ------------------------------------
# - `None` is a special literal in Python. It is not the same as zero, False, or an empty string.
# - `None` represents the absence of a value or a null value.
# - It is often used to indicate that a variable has not been assigned a value, or to represent the result of a function that does not explicitly return a value.
# - `None` is its own data type, `NoneType`.

print("\n# 04. None")
print("# ------------------------------------")
print("# - Special literal representing absence of a value or null value.")
print("# - Not zero, False, or empty string.")
print("# - Indicates a variable not assigned a value or function with no explicit return.")
print("# - Data type is NoneType.")

none_example_1 = None
none_example_2 = None  # Re-assigning None still results in None
none_example_3 = print("Hello") # print function returns None
none_example_4 = [1, 2, 3].pop() if [1, 2, 3] else None # pop() returns last element, but if list was empty, it could return None (using conditional expression for example)

print("\n# Examples:")
print("none_example_1 =", none_example_1, ", Type:", type(none_example_1))
print("none_example_2 =", none_example_2, ", Type:", type(none_example_2))
print("none_example_3 (result of print()) =", none_example_3, ", Type:", type(none_example_3))
# The output of print is None, but print itself outputs "Hello" to console. To avoid console output in this context, we could have assigned to none_example_3 something that evaluates to None without side-effects for demonstration.
none_example_3_demonstration = print("Demonstration of print() returning None - No variable assignment, just calling print:", end=" ")
print(none_example_3_demonstration) # This print will show None as print() returns None.
print("none_example_4 (pop() from list if list not empty, else None) = (Note: pop() was done if list not empty for example to show conditional None assignment): ", none_example_4, ", Type:", type(none_example_4))

print("# Operations: Check for identity (is None, is not None).")
print("# Common Uses: Initialize variables without initial value, function return values indicating no result, optional arguments.")
print("# Note: None is often used to handle cases where a value might be absent or not applicable.")

# 05. Integer Caching Internals
# ------------------------------------
# - CPython pre-creates and caches small integers from -5 to 256 as
#   singleton objects. Any name bound to one of these values points to the
#   SAME object in memory - `is` comparisons "work" for equality by accident.
# - Outside that range, each literal typically creates a new int object
#   (though the interpreter may still merge some constants in the same
#   compiled code block - never rely on it either way).

print("\n# 05. Integer Caching Internals")
print("# ------------------------------------")

cached_a = 256
cached_b = 256
print("256 is 256 (cached range -5..256):", cached_a is cached_b)

uncached_a = 257
uncached_b = 257
print("257 is 257 (outside cached range):", uncached_a is uncached_b, "(implementation detail!)")
print("# Always use '==' to compare integer VALUES, never 'is'.")

# 06. Float Precision & Exact Arithmetic (Decimal, Fraction)
# ------------------------------------
# - float is IEEE-754 double precision: fast, but cannot represent every
#   decimal fraction exactly (binary vs decimal bases don't line up).
# - decimal.Decimal: exact base-10 arithmetic, ideal for money/finance.
# - fractions.Fraction: exact rational arithmetic (numerator/denominator).

print("\n# 06. Float Precision & Exact Arithmetic")
print("# ------------------------------------")

print("float: 0.1 + 0.2 =", 0.1 + 0.2, "(not exactly 0.3)")

from decimal import Decimal
decimal_sum = Decimal("0.1") + Decimal("0.2")
print("Decimal: Decimal('0.1') + Decimal('0.2') =", decimal_sum, "(exact)")

from fractions import Fraction
fraction_sum = Fraction(1, 3) + Fraction(1, 6)
print("Fraction: Fraction(1,3) + Fraction(1,6) =", fraction_sum, "(exact rational)")
print("# Common Uses: Decimal for currency/finance, Fraction for exact ratios.")

# 07. Complex Number Operations
# ------------------------------------
# - Beyond .real/.imag, complex numbers support conjugate() (flips the sign
#   of the imaginary part) and abs() (returns the magnitude/modulus).

print("\n# 07. Complex Number Operations")
print("# ------------------------------------")

z = 3 + 4j
print("z =", z)
print("z.conjugate() =", z.conjugate())
print("abs(z) (magnitude, sqrt(3**2 + 4**2)) =", abs(z))
print("z * z.conjugate() =", z * z.conjugate(), "(always a real-valued result)")

# 08. Integer Bit Length & Bitwise Operations
# ------------------------------------
# - int.bit_length() returns the number of bits needed to represent the
#   integer in binary (excluding sign and leading zeros).
# - Bitwise operators: & (AND), | (OR), ^ (XOR), ~ (NOT), <<, >> (shifts).

print("\n# 08. Integer Bit Length & Bitwise Operations")
print("# ------------------------------------")

n = 37
print(f"n = {n}, bin(n) = {bin(n)}, n.bit_length() = {n.bit_length()}")

x, y = 12, 10
print(f"\nx={x} ({bin(x)}), y={y} ({bin(y)})")
print("x & y  (AND):", x & y)
print("x | y  (OR) :", x | y)
print("x ^ y  (XOR):", x ^ y)
print("~x     (NOT):", ~x, "(equivalent to -x - 1)")
print("x << 2 (left shift, x*4):", x << 2)
print("x >> 2 (right shift, x//4):", x >> 2)

# 09. Memory Footprint with sys.getsizeof
# ------------------------------------
# - sys.getsizeof() reports the memory (in bytes) an object occupies.
# - Useful to see how types differ in overhead - e.g. bool/int/float are
#   fixed-size, but Python ints grow larger in memory for bigger values.

print("\n# 09. Memory Footprint with sys.getsizeof")
print("# ------------------------------------")

import sys
print("sys.getsizeof(True)         :", sys.getsizeof(True), "bytes")
print("sys.getsizeof(0)            :", sys.getsizeof(0), "bytes")
print("sys.getsizeof(100)          :", sys.getsizeof(100), "bytes")
print("sys.getsizeof(2**64)        :", sys.getsizeof(2**64), "bytes (bigger value, more bytes)")
print("sys.getsizeof(3.14)         :", sys.getsizeof(3.14), "bytes (fixed size for any float)")
print("sys.getsizeof(3+4j)         :", sys.getsizeof(3 + 4j), "bytes")

print("\n# End of Primitive Data Types Explanation")

