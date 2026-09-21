"""
Module 02: Data Structures & Pythonic Idioms
Lesson 06: Comprehensions, Generator Expressions & Matrix Flattening

Run this file with:
    python 06_comprehensions.py
"""

import sys

# =====================================================================
# 1. Why Comprehensions?
# =====================================================================
# Comprehensions are not just syntactic sugar; they are FASTER than
# standard for-loops because CPython optimizes the loop at the C-level
# using dedicated bytecode instructions (LIST_APPEND) without repeatedly
# looking up the .append method in Python scope!

# Traditional Loop:
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x ** 2)

# List Comprehension:
squares_comp = [x ** 2 for x in range(1, 6)]

print("--- 1. List Comprehensions ---")
print(f"squares_comp: {squares_comp}")
assert squares_loop == squares_comp

# Filtering with `if`:
evens = [x for x in range(10) if x % 2 == 0]
print(f"evens: {evens}")
assert evens == [0, 2, 4, 6, 8]

# =====================================================================
# 2. Filtering vs Ternary: The Placement of `if`
# =====================================================================
# Case A: Filter (placed at the END, drops elements)
# [expr for x in iterable if condition]
positives = [x for x in [-2, -1, 0, 1, 2] if x > 0]
assert positives == [1, 2]

# Case B: Transformation / Ternary (placed at the FRONT, keeps same length!)
# [expr_true if condition else expr_false for x in iterable]
clamped = [x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]]
print("\n--- 2. Ternary vs Filter Placement ---")
print(f"clamped (keeps length 5): {clamped}")
assert clamped == [0, 0, 0, 1, 2]

# =====================================================================
# 3. Dict and Set Comprehensions
# =====================================================================
# Dict Comprehension: {key: value for ...}
names = ["alice", "bob", "charlie"]
name_lengths = {name: len(name) for name in names}
print("\n--- 3. Dict and Set Comprehensions ---")
print(f"name_lengths: {name_lengths}")
assert name_lengths == {"alice": 5, "bob": 3, "charlie": 7}

# Set Comprehension: {expr for ...} (automatically deduplicates)
word = "abracadabra"
unique_vowels = {ch for ch in word if ch in "aeiou"}
print(f"unique_vowels in '{word}': {unique_vowels}")
assert unique_vowels == {"a"}

# =====================================================================
# 4. Generator Expressions: O(1) Memory Streams!
# =====================================================================
# Replacing [] with () creates a GENERATOR instead of building the whole list in RAM!
num_count = 1_000_000

# List comp: Allocates all 1,000,000 ints in RAM immediately (~8 MB)
# Generator: Generates each value on the fly (104 bytes fixed memory!)
gen_exp = (x ** 2 for x in range(num_count))
print("\n--- 4. Memory: List Comp vs Generator Expression ---")
print(f"Generator memory usage: {sys.getsizeof(gen_exp)} bytes for 1M items!")
assert sys.getsizeof(gen_exp) < 500

# Summing via generator directly (no intermediate list allocation!):
sum_first_five = sum(x for x in range(1, 6))
assert sum_first_five == 15

# =====================================================================
# 5. Nested Comprehensions: 2D Matrix Flattening
# =====================================================================
# Golden Rule of Nested Order: Read it from left to right as if it were nested loops!
# for row in matrix:
#     for val in row:
#         ...
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [val for row in matrix for val in row]
print("\n--- 5. 2D Matrix Flattening ---")
print(f"Flattened: {flattened}")
assert flattened == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transposing a matrix:
transposed = [[row[c] for row in matrix] for c in range(len(matrix[0]))]
print(f"Transposed: {transposed}")
assert transposed == [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# =====================================================================
# 6. Self-Testing Verification
# =====================================================================
# Exercise 1: Extract all palindromes from words list, lowercased
words_list = ["Radar", "Python", "Level", "World", "Kayak"]
palindromes = [w.lower() for w in words_list if w.lower() == w.lower()[::-1]]
assert palindromes == ["radar", "level", "kayak"]

# Exercise 2: Create a coordinate grid of (x, y) for 0 <= x < 3 and 0 <= y < 3 where x != y
grid_points = [(x, y) for x in range(3) for y in range(3) if x != y]
assert (0, 0) not in grid_points
assert (0, 1) in grid_points
assert len(grid_points) == 6

print("\nAll 06_comprehensions self-tests passed successfully!")
