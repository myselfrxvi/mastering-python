"""
Module 01: Basics
Lesson 03: Conditionals, Truthiness & Logical Operators

Run this file with:
    python 03_conditionals.py
"""

# =====================================================================
# 1. Truthy vs Falsy in Python
# =====================================================================
# In Python, every object has an inherent Boolean truth value.
# You don't need `if len(items) > 0:` — simply `if items:`!

# Exactly what evaluates to False in Python?
# 1. Constants: None, False
# 2. Zero of any numeric type: 0, 0.0, 0j
# 3. Empty sequences and collections: "", (), [], {}, set(), range(0)
# Everything else is TRUTHY!

print("--- 1. Testing Truthiness ---")
empty_list = []
if not empty_list:
    print("empty_list is Falsy! Pythonic check: 'if not empty_list:'")

username = ""
if not username:
    print("empty string is Falsy!")

# =====================================================================
# 2. Chained Comparisons (A Python Superpower!)
# =====================================================================
# In C++ / Java: (0 <= score && score <= 100)
# In Python: 0 <= score <= 100
score = 85
if 80 <= score <= 90:
    print("\n--- 2. Chained Comparisons ---")
    print(f"Score {score} is between 80 and 90! Python syntax: '80 <= score <= 90'")

# =====================================================================
# 3. Short-Circuit Evaluation & Default Values
# =====================================================================
# `and` stops evaluating as soon as it sees a Falsy value.
# `or` stops evaluating as soon as it sees a Truthy value.
# In fact, they return the actual evaluated operand, not just True/False!

user_input = ""
display_name = user_input or "Anonymous User"
print("\n--- 3. Short-Circuit Defaults ---")
print(f"display_name: '{display_name}'")

# =====================================================================
# 4. Ternary Conditional Operator (One-Liner if-else)
# =====================================================================
# Syntax: <value_if_true> if <condition> else <value_if_false>
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status for age {age}: {status}")

# =====================================================================
# 5. Self-Checking Exercises
# =====================================================================
print("\n--- 4. Running Self-Checking Exercises ---")

def categorize_temperature(temp_celsius: float) -> str:
    """Return 'Freezing' if < 0, 'Moderate' if 0 <= temp <= 30, else 'Hot'"""
    if temp_celsius < 0:
        return "Freezing"
    elif 0 <= temp_celsius <= 30:
        return "Moderate"
    else:
        return "Hot"

def sanitize_name(name_input: str) -> str:
    """Return stripped name if non-empty, otherwise 'Guest'"""
    trimmed = name_input.strip()
    return trimmed if trimmed else "Guest"

# Verification Tests:
assert categorize_temperature(-5.0) == "Freezing"
assert categorize_temperature(15.0) == "Moderate"
assert categorize_temperature(30.0) == "Moderate"
assert categorize_temperature(35.0) == "Hot"
assert sanitize_name("  Alice  ") == "Alice"
assert sanitize_name("   ") == "Guest"
assert sanitize_name("") == "Guest"

print("All tests passed! You have mastered conditionals and truthiness in Python.")
