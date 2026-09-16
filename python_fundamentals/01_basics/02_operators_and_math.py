"""
Module 01: Basics
Lesson 02: Operators, Arithmetic & Identity

Run this file with:
    python 02_operators_and_math.py
"""
import math

# =====================================================================
# 1. Arithmetic Operators & Division Gotchas
# =====================================================================
a = 7
b = 2

print("--- 1. Division Mechanics ---")
# Normal division `/` ALWAYS produces a float!
print(f"7 / 2  = {a / b}   (type: {type(a / b)})")   # 3.5

# Floor division `//` rounds DOWN towards negative infinity:
print(f"7 // 2 = {a // b}   (type: {type(a // b)})")   # 3
print(f"-7 // 2 = {-7 // 2} (rounds down towards -inf, NOT towards 0!)") # -4!

# Modulus `%` (Remainder):
print(f"7 % 2  = {a % b}")   # 1

# Exponentiation `**`:
print(f"2 ** 10 = {2 ** 10}") # 1024

# =====================================================================
# 2. Equality (==) vs Object Identity (is)
# =====================================================================
# This is one of the MOST common Python interview questions!
# `==` checks if values are EQUAL.
# `is` checks if they are the EXACT SAME OBJECT IN MEMORY (same memory address).

print("\n--- 2. Equality (==) vs Identity (is) ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2) # True: Both hold elements [1, 2, 3]
print("list1 is list2:", list1 is list2) # False: Two distinct lists in memory!
print("list1 is list3:", list1 is list3) # True: Both names point to the same list!

# Always use `is` when checking for None:
val = None
if val is None:
    print("Correct Pythonic check: 'val is None'")

# =====================================================================
# 3. The IEEE 754 Floating Point Gotcha
# =====================================================================
# Because computers represent floats in binary (base 2), 0.1 cannot be
# represented exactly, just like 1/3 cannot be represented in decimal!
print("\n--- 3. Floating Point Precision ---")
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3) # False! (0.30000000000000004)
print("0.1 + 0.2 =", 0.1 + 0.2)

# Production Solution: Use math.isclose() for float comparisons!
print("math.isclose(0.1 + 0.2, 0.3):", math.isclose(0.1 + 0.2, 0.3)) # True!

# =====================================================================
# 4. Self-Checking Exercises
# =====================================================================
print("\n--- 4. Running Self-Checking Exercises ---")

def calculate_time_parts(total_seconds: int) -> tuple:
    """Break total seconds into (hours, minutes, seconds) using // and %"""
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds

def are_floats_equal(a: float, b: float) -> bool:
    """Check if two floats are equal within standard precision"""
    return math.isclose(a, b)

# Verification Tests:
assert calculate_time_parts(3665) == (1, 1, 5)
assert calculate_time_parts(7200) == (2, 0, 0)
assert calculate_time_parts(59) == (0, 0, 59)
assert are_floats_equal(0.1 + 0.2, 0.3) is True
assert are_floats_equal(1.0000001, 1.0) is False

print("All tests passed! You have mastered operators and numerical mechanics.")
