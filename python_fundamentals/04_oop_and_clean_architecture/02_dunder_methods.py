"""
Module 04: Object-Oriented Programming (OOP) & Clean Architecture
Lesson 02: The Python Data Model, Dunder Methods & Operator Overloading

Run this file with:
    python 02_dunder_methods.py
"""

from functools import total_ordering
import math
from typing import Any, Iterator, List, Optional, Tuple, Union

# =====================================================================
# 1. String Representations: __repr__ vs __str__
# =====================================================================
# Python provides two distinct dunder methods for string conversion:
#
# 1. `__repr__(self)`: Unambiguous representation intended for DEVELOPERS & DEBUGGERS.
#    Golden rule: Should look like valid Python code to recreate the object if possible.
#    e.g. eval(repr(obj)) == obj
#
# 2. `__str__(self)`: Human-friendly representation intended for END USERS & LOGS.
#
# Fallback Rule:
# If __str__ is NOT implemented, Python automatically falls back to __repr__.
# If __repr__ is NOT implemented, Python falls back to the default <ClassName object at 0x...>.
# Therefore, ALWAYS implement __repr__ first!

class ComplexNumber:
    def __init__(self, real: float, imag: float) -> None:
        self.real: float = float(real)
        self.imag: float = float(imag)

    def __repr__(self) -> str:
        # Code-like representation:
        return f"ComplexNumber(real={self.real}, imag={self.imag})"

    def __str__(self) -> str:
        # Readable mathematical format:
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}i)"


c = ComplexNumber(3.0, -4.5)
assert repr(c) == "ComplexNumber(real=3.0, imag=-4.5)"
assert str(c) == "(3.0 - 4.5i)"
assert f"Value is: {c}" == "Value is: (3.0 - 4.5i)"  # f-string defaults to __str__
assert f"Debug is: {c!r}" == "Debug is: ComplexNumber(real=3.0, imag=-4.5)"  # !r forces __repr__
print("--- 1. String Representations (__repr__ vs __str__): PASSED ---")

# =====================================================================
# 2. Equality (__eq__) and Hashing (__hash__) Mechanics
# =====================================================================
# Default behavior (inherited from object):
# - `__eq__` checks memory identity (`is`).
# - `__hash__` returns identity hash.
#
# CRITICAL PYTHON INVARIANT:
# If two objects are equal (`a == b`), they MUST produce the EXACT same hash:
#   `a == b` => `hash(a) == hash(b)`
#
# Python Safeguard:
# Whenever you define a custom `__eq__`, Python AUTOMATICALLY sets `__hash__ = None`!
# This marks the class as UNHASHABLE to prevent mutable objects from breaking
# hash table invariants when inserted into sets or dictionaries.
#
# To make a class hashable again:
# Implement `__hash__` using immutable fields (e.g. hashing a tuple of values).

class ImmutablePoint:
    __slots__ = ("_x", "_y")

    def __init__(self, x: int, y: int) -> None:
        # Use object.__setattr__ because fields are treated as frozen
        object.__setattr__(self, "_x", x)
        object.__setattr__(self, "_y", y)

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ImmutablePoint):
            return NotImplemented  # Let Python try the reflected operator or fallback
        return self._x == other._x and self._y == other._y

    def __hash__(self) -> int:
        # Hash an immutable tuple of identifying fields:
        return hash((self._x, self._y))

    def __repr__(self) -> str:
        return f"ImmutablePoint({self._x}, {self._y})"


p1 = ImmutablePoint(10, 20)
p2 = ImmutablePoint(10, 20)
p3 = ImmutablePoint(30, 40)

# Equality checks:
assert p1 == p2
assert p1 is not p2  # Different memory allocations
assert p1 != p3

# Hash equality:
assert hash(p1) == hash(p2)

# Usable as keys in dictionaries and elements in sets:
point_set = {p1, p2, p3}
assert len(point_set) == 2  # p1 and p2 deduplicated!
assert p1 in point_set
assert ImmutablePoint(10, 20) in point_set

point_cache = {p1: "origin_offset"}
assert point_cache[ImmutablePoint(10, 20)] == "origin_offset"
print("--- 2. Equality & Hashing (__eq__ and __hash__): PASSED ---")

# =====================================================================
# 3. Rich Comparisons & @total_ordering
# =====================================================================
# Implementing all 6 comparison dunders (__lt__, __le__, __gt__, __ge__, __eq__, __ne__)
# involves tedious boilerplate.
# The `@total_ordering` decorator from `functools` requires only:
# - `__eq__` AND
# - ONE of (`__lt__`, __le__, __gt__, __ge__)
# and synthesizes all remaining comparison operators automatically!

@total_ordering
class SemVer:
    """Semantic versioning comparator: major.minor.patch."""

    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def _as_tuple(self) -> Tuple[int, int, int]:
        return (self.major, self.minor, self.patch)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented
        return self._as_tuple() == other._as_tuple()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented
        return self._as_tuple() < other._as_tuple()

    def __repr__(self) -> str:
        return f"SemVer({self.major}.{self.minor}.{self.patch})"


v1_0_0 = SemVer(1, 0, 0)
v1_2_0 = SemVer(1, 2, 0)
v1_2_1 = SemVer(1, 2, 1)
v2_0_0 = SemVer(2, 0, 0)

assert v1_0_0 < v1_2_0
assert v1_2_0 <= v1_2_1
assert v2_0_0 > v1_2_1
assert v2_0_0 >= v1_0_0
assert v1_2_1 != v1_2_0
assert sorted([v2_0_0, v1_0_0, v1_2_1, v1_2_0]) == [v1_0_0, v1_2_0, v1_2_1, v2_0_0]
print("--- 3. Rich Comparisons & @total_ordering: PASSED ---")

# =====================================================================
# 4. The Container & Sequence Protocol
# =====================================================================
# Python collections implement protocols by defining:
# - `__len__`: Returns number of items for `len(obj)`.
# - `__getitem__`: Handles `obj[key]` access (integers, keys, or `slice` objects!).
# - `__setitem__`: Handles `obj[key] = val`.
# - `__delitem__`: Handles `del obj[key]`.
# - `__contains__`: Handles `val in obj` (falls back to linear scan if missing).

class CircularBuffer:
    """A fixed-capacity circular buffer with Pythonic slicing and indexing."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity: int = capacity
        self._data: List[Any] = []

    def append(self, item: Any) -> None:
        if len(self._data) >= self._capacity:
            self._data.pop(0)  # Drop oldest
        self._data.append(item)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: Union[int, slice]) -> Any:
        # Demonstrating full slicing support:
        if isinstance(index, slice):
            return self._data[index]
        return self._data[index]

    def __contains__(self, item: Any) -> bool:
        return item in self._data

    def __repr__(self) -> str:
        return f"CircularBuffer(capacity={self._capacity}, items={self._data!r})"


buf = CircularBuffer(3)
buf.append("A")
buf.append("B")
assert len(buf) == 2
assert buf[0] == "A"
assert buf[-1] == "B"

buf.append("C")
assert list(buf) == ["A", "B", "C"]  # Iteration works automatically via __getitem__!

# Capacity exceeded: oldest element "A" dropped:
buf.append("D")
assert len(buf) == 3
assert buf[0] == "B"
assert buf[-1] == "D"
assert "A" not in buf
assert "C" in buf
assert buf[1:] == ["C", "D"]  # Slicing works!
print("--- 4. Container & Sequence Protocol: PASSED ---")

# =====================================================================
# 5. Arithmetic Operator Overloading & Reflection (__add__, __radd__, __mul__)
# =====================================================================
# Operator overloading allows domain objects (Vectors, Money, Matrices)
# to use intuitive mathematical operators:
# - `__add__(self, other)`: Left-hand operator: `self + other`
# - `__radd__(self, other)`: Reflected/Right-hand operator: `other + self`
#   (Invoked when the left operand does not support the operation with self).

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = float(x)
        self.y: float = float(y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        """Scalar multiplication: Vector * scalar."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        """Reflected scalar multiplication: scalar * Vector."""
        # scalar * vec delegates directly to vec * scalar:
        return self.__mul__(scalar)

    def __abs__(self) -> float:
        """Euclidean norm / magnitude via abs(v):"""
        return math.hypot(self.x, self.y)


vec1 = Vector2D(3.0, 4.0)
vec2 = Vector2D(1.0, 2.0)

# Addition and Subtraction:
assert vec1 + vec2 == Vector2D(4.0, 6.0)
assert vec1 - vec2 == Vector2D(2.0, 2.0)

# Left and Right Multiplication:
assert vec1 * 2 == Vector2D(6.0, 8.0)
assert 3 * vec2 == Vector2D(3.0, 6.0)  # Triggers __rmul__!

# abs() dunder:
assert abs(vec1) == 5.0
print("--- 5. Arithmetic Overloading & Reflection (__add__, __rmul__): PASSED ---")

# =====================================================================
# 6. Callable Objects: The `__call__` Protocol
# =====================================================================
# Implementing `__call__` makes an instance callable like a standard function:
# `instance(arg1, arg2)`.
# Use case: Stateful function objects, rate limiters, middleware pipelines.

class TokenBucketRateLimiter:
    """In-memory rate limiter maintaining state across invocations."""

    def __init__(self, max_tokens: int) -> None:
        self.capacity: int = max_tokens
        self.tokens: int = max_tokens

    def __call__(self, tokens_needed: int = 1) -> bool:
        """Attempt to consume tokens. Returns True if permitted, False otherwise."""
        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        return False

    def reset(self) -> None:
        self.tokens = self.capacity


limiter = TokenBucketRateLimiter(max_tokens=3)
assert callable(limiter) is True

# Invoking instance as a function:
assert limiter(1) is True   # Tokens left: 2
assert limiter(2) is True   # Tokens left: 0
assert limiter(1) is False  # Denied!
limiter.reset()
assert limiter(1) is True   # Allowed again!
print("--- 6. Callable Instances (__call__): PASSED ---")

# =====================================================================
# 7. Truthiness Protocol: `__bool__` vs `__len__` Fallback
# =====================================================================
# When evaluating `bool(obj)` or `if obj:`:
# 1. Python looks for `__bool__()`.
# 2. If `__bool__` is absent, Python looks for `__len__()` (0 is False, >0 is True).
# 3. If neither is defined, the object evaluates to `True`.

class TransactionBatch:
    def __init__(self, tx_ids: List[str]) -> None:
        self.tx_ids = tx_ids

    def __len__(self) -> int:
        return len(self.tx_ids)

    # Note: no __bool__ defined! Falls back to __len__() != 0.


empty_batch = TransactionBatch([])
loaded_batch = TransactionBatch(["tx_101", "tx_102"])

assert bool(empty_batch) is False
assert bool(loaded_batch) is True
print("--- 7. Truthiness Protocol (__bool__ & __len__): PASSED ---")

print("\n=======================================================")
print("ALL LESSON 02 ASSERTIONS PASSED! DUNDER METHODS MASTERED.")
print("=======================================================")
