"""
Module 01: Basics
Lesson 01: Variables, Primitive Types & Type Casting

Run this file with:
    python 01_variables_and_types.py
"""

# =====================================================================
# 1. Variables & Dynamic Typing
# =====================================================================
# In Python, you do NOT declare types explicitly (like int x = 5).
# The Python interpreter infers the type dynamically at runtime.

age = 21                # int: Arbitrary-precision integer
height = 5.11           # float: 64-bit floating point number
name = "Vs Code"    # str: Immutable sequence of Unicode characters
is_coder = True         # bool: True or False (note capitalization!)
nothing = None          # NoneType: Represents absence of value (like null/nil)

# =====================================================================
# 2. Inspecting Types
# =====================================================================
print("--- 1. Inspecting Types ---")
print(f"age: {age} | type: {type(age)}")
print(f"height: {height} | type: {type(height)}")
print(f"name: {name} | type: {type(name)}")
print(f"is_coder: {is_coder} | type: {type(is_coder)}")
print(f"nothing: {nothing} | type: {type(nothing)}")

# Best practice for type checking in production: isinstance()
# isinstance supports checking inheritance subclasses!
print("Is age an int?", isinstance(age, int))        # True
print("Is height a float?", isinstance(height, float))# True

# =====================================================================
# 3. Python Fun Fact: Arbitrary-Precision Integers!
# =====================================================================
# In C++ / Java, 64-bit integers overflow after 9,223,372,036,854,775,807.
# In Python 3, integers automatically grow to fit any size your RAM allows!
giant_number = 2 ** 100
print(f"\n2^100 in Python = {giant_number}")

# =====================================================================
# 4. Type Casting (Conversion)
# =====================================================================
# Converting between types explicitly:
str_val = "100"
converted_int = int(str_val)       # "100" -> 100
converted_float = float(str_val)   # "100" -> 100.0
back_to_str = str(42)              # 42 -> "42"

print("\n--- 2. Type Casting ---")
print(f"converted_int: {converted_int} ({type(converted_int)})")
print(f"converted_float: {converted_float} ({type(converted_float)})")
print(f"back_to_str: '{back_to_str}' ({type(back_to_str)})")

# =====================================================================
# 5. Beginner Exercises & Self-Testing Assertions
# =====================================================================
print("\n--- 3. Running Self-Checking Exercises ---")

def celsius_to_fahrenheit(celsius: float) -> float:
    """Formula: (celsius * 9/5) + 32"""
    return (celsius * 9 / 5) + 32

def parse_user_record(raw_age: str, raw_score: str) -> tuple:
    """Convert raw string inputs into (int, float)"""
    return int(raw_age), float(raw_score)

# Verification Tests:
assert celsius_to_fahrenheit(0) == 32.0
assert celsius_to_fahrenheit(100) == 212.0
assert parse_user_record("25", "98.5") == (25, 98.5)
assert isinstance(parse_user_record("18", "75.0")[0], int)
assert isinstance(parse_user_record("18", "75.0")[1], float)

print("All tests passed! You have mastered variables and types in Python.")
