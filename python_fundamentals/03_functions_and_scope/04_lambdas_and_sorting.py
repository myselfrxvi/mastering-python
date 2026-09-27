"""
Module 03: Functions, Scope & Functional Idioms
Lesson 04: Anonymous Lambdas, Functional Pipelines, and Multi-Key Sorting Idioms

Run this file with:
    python 04_lambdas_and_sorting.py
"""

from functools import reduce
import operator
from typing import List, NamedTuple

# =====================================================================
# 1. Anonymous Functions: The Lambda Protocol
# =====================================================================
# Syntax: lambda arg1, arg2, ...: expression
#
# Rules:
# - Can contain only a SINGLE expression (no statements like `return`, `pass`, assignments).
# - Automatically returns the evaluated expression.
# - Best for short, throwaway transformations.

square = lambda x: x * x
assert square(5) == 25

add = lambda a, b: a + b
assert add(10, 20) == 30
print("--- 1. Lambda Protocol: PASSED ---")

# =====================================================================
# 2. Functional Primitives: map, filter, vs Comprehensions
# =====================================================================
nums = [1, 2, 3, 4, 5, 6]

# map(): applies a transformation to each item (returns a lazy iterator)
mapped = list(map(lambda x: x * 10, nums))
assert mapped == [10, 20, 30, 40, 50, 60]

# filter(): keeps items where predicate is True (returns a lazy iterator)
evens = list(filter(lambda x: x % 2 == 0, nums))
assert evens == [2, 4, 6]

# Pythonic Guideline: Comprehensions are almost always faster and more readable!
comp_evens = [x * 10 for x in nums if x % 2 == 0]
assert comp_evens == [20, 40, 60]
print("--- 2. Map & Filter vs Comprehensions: PASSED ---")

# =====================================================================
# 3. Reducing Streams: `functools.reduce` and `operator`
# =====================================================================
# reduce(func, iterable, [initial]) folds an iterable down to a single value.

numbers = [1, 2, 3, 4, 5]

# Sum using reduce + lambda:
sum_val = reduce(lambda acc, x: acc + x, numbers, 0)
assert sum_val == 15

# Professional Optimization: Use the C-implemented `operator` module!
# operator.add is substantially faster than compiling a Python lambda:
c_sum = reduce(operator.add, numbers, 0)
assert c_sum == 15

product = reduce(operator.mul, numbers, 1)
assert product == 120
print("--- 3. Reduce & Operator Module: PASSED ---")

# =====================================================================
# 4. Multi-Criteria Sorting: The Tuple Key Protocol
# =====================================================================
# Python's built-in Timsort is STABLE: equal keys preserve original relative order.
# To sort by multiple criteria, return a tuple from the `key=` function!

class Student(NamedTuple):
    name: str
    grade: int    # 9, 10, 11, 12
    gpa: float    # 0.0 - 4.0

students = [
    Student("Alice", 11, 3.8),
    Student("Bob", 12, 3.9),
    Student("Charlie", 11, 3.9),
    Student("David", 12, 3.5),
    Student("Eve", 11, 3.8),
]

# Criteria:
# 1. Primary: Sort by grade ASCENDING (lower grade first)
# 2. Secondary: Sort by GPA DESCENDING (higher GPA first) -> negate `-s.gpa`!
# 3. Tertiary: Sort by name ALPHABETICALLY -> `s.name`

sorted_students = sorted(
    students,
    key=lambda s: (s.grade, -s.gpa, s.name)
)

expected_names = [
    "Charlie",  # Grade 11, GPA 3.9
    "Alice",    # Grade 11, GPA 3.8, Name 'Alice' < 'Eve'
    "Eve",      # Grade 11, GPA 3.8, Name 'Eve'
    "Bob",      # Grade 12, GPA 3.9
    "David"     # Grade 12, GPA 3.5
]

actual_names = [s.name for s in sorted_students]
assert actual_names == expected_names
print("--- 4. Multi-Criteria Tuple Sorting: PASSED ---")

# =====================================================================
# 5. High-Performance Field Extraction: operator.itemgetter & attrgetter
# =====================================================================
# When sorting dictionaries or objects by existing fields,
# operator.itemgetter and operator.attrgetter avoid Python bytecode evaluation:

records = [
    {"city": "Tokyo", "population": 37_400_000},
    {"city": "Delhi", "population": 30_290_000},
    {"city": "Shanghai", "population": 27_053_000},
]

# Sort by population descending:
sorted_cities = sorted(records, key=operator.itemgetter("population"), reverse=True)
assert sorted_cities[0]["city"] == "Tokyo"
assert sorted_cities[-1]["city"] == "Shanghai"
print("--- 5. C-Speed Key Extraction (itemgetter): PASSED ---")

print("\n=======================================================")
print("ALL LESSON 04 ASSERTIONS PASSED! FUNCTIONAL IDIOMS MASTERED.")
print("=======================================================")
