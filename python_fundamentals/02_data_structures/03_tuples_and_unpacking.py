"""
Module 02: Data Structures & Pythonic Idioms
Lesson 03: Tuples, Immutability & Structural Unpacking

Run this file with:
    python 03_tuples_and_unpacking.py
"""

from collections import namedtuple
import sys

# =====================================================================
# 1. Tuples: Lightweight Immutable Sequences
# =====================================================================
# Tuples are created using parentheses () or commas.
# Once created, their length and pointers CANNOT be changed.

point = (10, 20, 30)
coords = 10, 20, 30  # Parentheses are optional! The comma creates the tuple.

print("--- 1. Tuples & The Trailing Comma Quirk ---")
print(f"point: {point} | type: {type(point)}")

# THE QUIRK: Single element tuple requires a trailing comma!
not_a_tuple = (42)     # Just an integer inside parentheses: int!
real_tuple = (42,)     # A 1-element tuple: tuple!

print(f"(42)  is: {type(not_a_tuple)}")
print(f"(42,) is: {type(real_tuple)}")
assert not isinstance(not_a_tuple, tuple)
assert isinstance(real_tuple, tuple)

# =====================================================================
# 2. Why Use Tuples Instead of Lists?
# =====================================================================
# Reason A: Memory & Performance
# CPython allocates exact memory for tuples (fixed size), whereas lists
# over-allocate capacity to allow fast amortized .append().
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print("\n--- 2. Memory Comparison ---")
print(f"List sizeof:  {sys.getsizeof(list_example)} bytes")
print(f"Tuple sizeof: {sys.getsizeof(tuple_example)} bytes")
assert sys.getsizeof(tuple_example) < sys.getsizeof(list_example)

# Reason B: Hashability (Dict Keys & Set Members)
# Because tuples are immutable, they are HASHABLE if all items inside are hashable!
grid_cache = {}
grid_cache[(0, 0)] = "Start"
grid_cache[(4, 4)] = "Goal"
print(f"Tuple as dict keys: {grid_cache}")

# But beware: A tuple containing a mutable object (like a list) is NOT hashable!
try:
    bad_key = (1, [2, 3])
    hash(bad_key)
except TypeError as e:
    print(f"Caught expected TypeError: {e}")

# =====================================================================
# 3. Structural Unpacking Mastery (PEP 3132)
# =====================================================================
print("\n--- 3. Pythonic Unpacking ---")

# 1. Elegant Swapping (No temp variable!)
x, y = 100, 200
x, y = y, x
print(f"Swapped: x={x}, y={y}")
assert x == 200 and y == 100

# 2. Extended Unpacking with Asterisk (*)
record = ["Alice", "Google", "Engineer", "Mountain View", "CA"]
name, company, *details = record
print(f"name: {name}, company: {company}, details: {details}")
assert name == "Alice"
assert details == ["Engineer", "Mountain View", "CA"]

# Head, Body, Tail extraction
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(f"first: {first}, middle: {middle}, last: {last}")
assert first == 1
assert middle == [2, 3, 4, 5]
assert last == 6

# =====================================================================
# 4. Named Tuples: Self-Documenting Data Records
# =====================================================================
# collections.namedtuple gives tuple memory efficiency with attribute access!
Point3D = namedtuple("Point3D", ["x", "y", "z"])
p = Point3D(x=1.5, y=2.0, z=5.5)

print("\n--- 4. Named Tuples ---")
print(f"p: {p}")
print(f"Access by attribute: p.x = {p.x}, p.y = {p.y}")
print(f"Access by index:     p[0] = {p[0]}")
assert p.x == 1.5
assert p[0] == 1.5

# =====================================================================
# 5. Self-Testing Verification
# =====================================================================
# Exercise 1: Function returning multiple values via tuple unpacking
def min_max_avg(values):
    return min(values), max(values), sum(values) / len(values)

low, high, avg = min_max_avg([10, 20, 30, 40])
assert low == 10
assert high == 40
assert avg == 25.0

# Exercise 2: Unpack first two elements, discard middle, keep last
items = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
f1, f2, *_, last_item = items
assert f1 == "apple"
assert f2 == "banana"
assert last_item == "fig"

print("\nAll 03_tuples_and_unpacking self-tests passed successfully!")
