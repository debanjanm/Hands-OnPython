from dataclasses import dataclass, field

# 01. Dataclasses - Introduction
# ------------------------------------
# - @dataclass auto-generates boilerplate like __init__, __repr__, __eq__
#   for classes that mainly hold data.
# - Reduces repetitive code compared to writing these methods by hand.

print("# 01. Dataclasses - Introduction")
print("# ------------------------------------")

# 02. Basic Dataclass
# ------------------------------------
@dataclass
class Point:
    x: int
    y: int

p1 = Point(2, 3)
p2 = Point(2, 3)
print("\n# 02. Basic Dataclass")
print(p1)                 # auto __repr__ -> Point(x=2, y=3)
print(p1 == p2)            # auto __eq__ -> True (compares field values)

# 03. Default Values and default_factory
# ------------------------------------
@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)  # mutable defaults need default_factory
    passed: bool = False

s = Student("Debanjan")
s.grades.append(90)
print("\n# 03. Default Values and default_factory")
print(s)

# 04. Immutable Dataclass (frozen=True)
# ------------------------------------
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

ip = ImmutablePoint(1, 1)
print("\n# 04. Immutable Dataclass (frozen=True)")
print(ip)
try:
    ip.x = 5
except Exception as e:
    print(f"Error modifying frozen instance: {e}")

# 05. Operator Overloading - Introduction
# ------------------------------------
# - Python lets custom classes define behavior for built-in operators
#   (+, -, ==, <, etc.) by implementing special/dunder methods.
print("\n# 05. Operator Overloading - Introduction")
print("# - Implement __add__, __eq__, __lt__, etc. to support operators.")

# 06. Overloading Arithmetic Operators
# ------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
print("\n# 06. Overloading Arithmetic Operators")
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 3 =", v1 * 3)

# 07. Overloading Comparison Operators
# ------------------------------------
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __repr__(self):
        return f"Money({self.amount})"

m1 = Money(100)
m2 = Money(200)
print("\n# 07. Overloading Comparison Operators")
print("m1 == m2:", m1 == m2)
print("m1 < m2:", m1 < m2)
print("sorted:", sorted([m2, m1]))  # uses __lt__

# 08. Other Common Dunder Methods
# ------------------------------------
class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

cart = Cart()
cart.add("apple")
cart.add("bread")
print("\n# 08. Other Common Dunder Methods")
print("len(cart):", len(cart))            # __len__
print("'apple' in cart:", "apple" in cart)  # __contains__
print("cart[0]:", cart[0])                  # __getitem__
for item in cart:                           # __iter__
    print("item:", item)

# 09. __post_init__ for Derived/Validated Fields
# ------------------------------------
# - __post_init__ runs automatically right after the generated __init__
#   finishes - the place to validate input or compute fields derived from
#   other fields, without hand-writing a custom __init__.
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False) # not passed in, computed in __post_init__
    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")
        self.area = self.width * self.height # derived field

print("\n# 09. __post_init__ for Derived/Validated Fields")
rect = Rectangle(4, 5)
print("rect:", rect)
try:
    Rectangle(-1, 5)
except ValueError as e:
    print("Caught validation error:", e)

# 10. field(compare=False) and field(repr=False)
# ------------------------------------
# - compare=False: excludes a field from the generated __eq__ (and order
#   comparisons) - two instances can be "equal" even if this field differs.
# - repr=False: excludes a field from the generated __repr__ output entirely.
@dataclass
class User:
    name: str
    id: int = field(compare=False)          # ignored by __eq__
    password_hash: str = field(repr=False, default="") # hidden from __repr__

u1 = User("Alice", 1)
u2 = User("Alice", 2) # different id, but id is excluded from comparison
print("\n# 10. field(compare=False) and field(repr=False)")
print("u1 == u2 (id excluded from comparison):", u1 == u2)
print("repr(u1) (password_hash hidden):", repr(u1))

# 11. order=True for Auto Comparison Methods
# ------------------------------------
# - order=True generates __lt__, __le__, __gt__, __ge__ automatically, using
#   fields in declaration order (like comparing tuples of the field values).
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

v1 = Version(1, 2, 0)
v2 = Version(1, 3, 0)
print("\n# 11. order=True for Auto Comparison Methods")
print("v1 < v2:", v1 < v2)   # compares (major, minor, patch) tuple-wise
print("sorted:", sorted([v2, v1]))

# 12. Dataclass Inheritance - Field Ordering Rules
# ------------------------------------
# - Fields from the base class come first, then the subclass's own fields.
# - A field WITHOUT a default cannot follow a field WITH a default in the
#   combined list - so if the base class has a defaulted field, every field
#   the subclass adds must also have a default (or use kw_only, 3.10+).
@dataclass
class Animal:
    name: str
    legs: int = 4 # has a default

@dataclass
class Dog(Animal):
    breed: str = "unknown" # must also have a default - follows a defaulted base field

print("\n# 12. Dataclass Inheritance - Field Ordering Rules")
print("Dog('Rex', 4, 'Labrador'):", Dog("Rex", 4, "Labrador"))
print("# - Animal.legs has a default, so Dog.breed is also forced to have one -")
print("#   'non-default argument follows default argument' would be a TypeError otherwise.")

# 13. slots=True Dataclass (Python 3.10+) - Memory Savings
# ------------------------------------
# - slots=True auto-generates __slots__ for the dataclass, combining
#   dataclass convenience with the memory savings covered in 02-Class-Object.py.
@dataclass(slots=True)
class LightPoint:
    x: int
    y: int

print("\n# 13. slots=True Dataclass")
lp = LightPoint(1, 2)
print("lp:", lp)
print("hasattr(lp, '__dict__'):", hasattr(lp, "__dict__")) # False - no __dict__, uses slots
try:
    lp.z = 3
except AttributeError as e:
    print("lp.z = 3 -> AttributeError:", e)

# 14. __radd__ and __iadd__ (Reflected and In-Place Operators)
# ------------------------------------
# - __add__(self, other) handles `self + other`.
# - __radd__(self, other) is the fallback for `other + self`, used when
#   `other`'s own __add__ doesn't know how to handle a Vector (e.g. int + Vector).
# - __iadd__(self, other) backs the in-place `self += other`; if omitted,
#   Python falls back to __add__ (a += b becomes a = a.__add__(b)).
class VectorOps:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return VectorOps(self.x + other.x, self.y + other.y)
    def __radd__(self, other):
        if other == 0: # supports sum([...]) which starts with 0 + first_element
            return self
        return self.__add__(other)
    def __iadd__(self, other):
        self.x += other.x # mutates in place instead of creating a new object
        self.y += other.y
        return self
    def __repr__(self):
        return f"VectorOps({self.x}, {self.y})"

v = VectorOps(1, 1)
print("\n# 14. __radd__ and __iadd__")
print("0 + VectorOps(1,1) (uses __radd__):", 0 + VectorOps(1, 1))
print("sum([VectorOps(1,1), VectorOps(2,2)]):", sum([VectorOps(1, 1), VectorOps(2, 2)]))
v += VectorOps(5, 5) # uses __iadd__, mutates v in place
print("v after += (uses __iadd__, mutated in place):", v)
