from typing import List, Dict, Optional, Union, Tuple, Callable, TypeVar, Protocol, TypedDict

# 01. Typing Module - Introduction
# ------------------------------------
# - Type hints document expected types; Python does NOT enforce them at
#   runtime (no error if violated) - tools like mypy check them statically.
# - Basic annotations (x: int) covered in 01-Functions.py #12; this file
#   covers the `typing` module's generic/composite types.

print("# 01. Typing Module - Introduction")
print("# ------------------------------------")

def add(a: int, b: int) -> int:
    return a + b

print("\nbasic annotation recap:", add(2, 3))
print("runtime does NOT enforce it:", add("2", "3"))  # no error, just string concat

# 02. Generic Collection Types
# ------------------------------------
def total(numbers: List[int]) -> int:
    return sum(numbers)

def user_ages(ages: Dict[str, int]) -> None:
    print(ages)

print("\n# 02. Generic Collection Types")
print(total([1, 2, 3]))
user_ages({"Debanjan": 25})

# 03. Optional - a Value or None
# ------------------------------------
def find_user(user_id: int) -> Optional[str]:  # same as Union[str, None]
    return "Debanjan" if user_id == 1 else None

print("\n# 03. Optional")
print(find_user(1))
print(find_user(2))

# 04. Union - One of Several Types
# ------------------------------------
def process(value: Union[int, str]) -> str:
    return f"processed {value}"

print("\n# 04. Union")
print(process(5))
print(process("five"))

# 05. Tuple with Fixed Structure
# ------------------------------------
def get_point() -> Tuple[int, int]:
    return (3, 4)

print("\n# 05. Tuple")
print(get_point())

# 06. Callable - Function Signatures as Types
# ------------------------------------
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print("\n# 06. Callable")
print(apply(add, 4, 5))

# 07. TypeVar - Generic Functions
# ------------------------------------
T = TypeVar("T")

def first_item(items: List[T]) -> T:
    return items[0]

print("\n# 07. TypeVar")
print(first_item([1, 2, 3]))
print(first_item(["a", "b"]))

# 08. Protocol - Structural Typing (duck typing, but checkable)
# ------------------------------------
class HasSpeak(Protocol):
    def speak(self) -> str: ...

class Dog:
    def speak(self) -> str:
        return "Woof!"

def make_it_speak(entity: HasSpeak) -> None:
    print(entity.speak())  # any object with .speak() satisfies HasSpeak

print("\n# 08. Protocol")
make_it_speak(Dog())

# 09. TypedDict - Dicts with a Known Shape
# ------------------------------------
class Movie(TypedDict):
    title: str
    year: int

print("\n# 09. TypedDict")
movie: Movie = {"title": "Inception", "year": 2010}
print(movie)

# 10. Modern Syntax (Python 3.9+/3.10+) - reference
# ------------------------------------
print("\n# 10. Modern Syntax (reference)")
print("# - list[int] instead of List[int]           (3.9+, no import needed)")
print("# - dict[str, int] instead of Dict[str, int]  (3.9+)")
print("# - int | None instead of Optional[int]       (3.10+)")
print("# - int | str instead of Union[int, str]      (3.10+)")

def modern_add(a: int | None, b: int) -> int:
    return (a or 0) + b

print(modern_add(None, 5))

# 11. Literal - Restrict to Specific Values
# ------------------------------------
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> str:
    return f"mode set to {mode}"  # a type checker flags mode="delete" as invalid

print("\n# 11. Literal")
print(set_mode("write"))

# 12. Final - Constants That Shouldn't Be Reassigned
# ------------------------------------
from typing import Final

MAX_RETRIES: Final = 3   # a type checker flags any later "MAX_RETRIES = 5"
print("\n# 12. Final")
print("MAX_RETRIES:", MAX_RETRIES)

# 13. @overload - Multiple Valid Signatures for One Function
# ------------------------------------
from typing import overload

@overload
def stringify(value: int) -> str: ...
@overload
def stringify(value: list) -> str: ...
def stringify(value):  # the actual implementation, no @overload here
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value)

print("\n# 13. @overload")
print(stringify(42))
print(stringify([1, 2, 3]))

# 14. NewType - Lightweight Distinct Types
# ------------------------------------
# - UserId is still an int at runtime (zero overhead) but a type checker
#   treats it as distinct, so passing a raw int where UserId is expected
#   is flagged as an error even though ints and UserIds print identically.
from typing import NewType

UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> str:
    return f"user #{user_id}"

print("\n# 14. NewType")
uid = UserId(42)
print(get_user(uid))
print("still just an int at runtime:", type(uid))

# 15. TYPE_CHECKING - Import Only for Type Checkers
# ------------------------------------
# - Imports under this guard never run at runtime (avoids circular imports
#   and import cost), but are visible to type checkers like mypy.
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import collections  # only "imported" during static analysis

print("\n# 15. TYPE_CHECKING")
print("# - Code under `if TYPE_CHECKING:` never executes at runtime.")
print("# - Use it for imports needed only for type hints.")

# 16. Any vs object
# ------------------------------------
# - Any turns off type checking entirely for that value - anything goes.
# - object is a real type: a type checker requires narrowing/casting
#   before you can call type-specific methods on it.
from typing import Any

def accepts_any(value: Any) -> None:
    value.whatever_method()  # type checker allows this, may fail at runtime

def accepts_object(value: object) -> None:
    print(str(value))  # only methods common to all objects are allowed

print("\n# 16. Any vs object")
accepts_object("hello")
print("# - Any: no static checking at all. object: safest, most restrictive.")
