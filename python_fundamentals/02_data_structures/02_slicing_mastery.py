"""
Module 02: Data Structures & Pythonic Idioms
Lesson 02: Slicing Mastery & The Stride Protocol

Run this file with:
    python 02_slicing_mastery.py
"""

# =====================================================================
# 1. The Slicing Protocol: sequence[start:stop:step]
# =====================================================================
# - start: inclusive index (defaults to 0 if step > 0, or end if step < 0)
# - stop:  exclusive index (defaults to len(sequence) if step > 0, or before 0 if step < 0)
# - step:  stride (defaults to 1). Can be negative for reverse direction!
#
# Indexing Diagram:
# Value:   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Index:     0    1    2    3    4    5    6
# Neg-Idx:  -7   -6   -5   -4   -3   -2   -1

chars = ["a", "b", "c", "d", "e", "f", "g"]
print("--- 1. Basic Slicing ---")
print(f"chars[1:4]   (indices 1, 2, 3):     {chars[1:4]}")
print(f"chars[:3]    (first 3 elements):    {chars[:3]}")
print(f"chars[4:]    (from index 4 to end): {chars[4:]}")
print(f"chars[::2]   (every 2nd element):   {chars[::2]}")
print(f"chars[::-1]  (complete reversal):   {chars[::-1]}")

# =====================================================================
# 2. Golden Feature: Slices Never Raise IndexError!
# =====================================================================
# Direct index lookup `chars[100]` raises IndexError.
# But slice boundaries are gracefully clamped to valid ranges:
print("\n--- 2. Clamped Slice Boundaries ---")
print(f"chars[2:1000]: {chars[2:1000]}")  # from index 2 to end!
print(f"chars[100:200]: {chars[100:200]}")  # empty list [] without error!

# =====================================================================
# 3. Slice Assignment: In-Place Surgical Editing
# =====================================================================
# You can assign to slices to replace, insert, or delete in place
# without changing the list's memory address!

numbers = [0, 1, 2, 3, 4, 5]
list_id = id(numbers)

# 1. Replace a subsegment
numbers[1:4] = [10, 20, 30]
print("\n--- 3. Slice Assignment ---")
print(f"Replaced [1:4]: {numbers}")
assert numbers == [0, 10, 20, 30, 4, 5]

# 2. Insert elements without removing anything (empty slice)
numbers[2:2] = [999]
print(f"Inserted at index 2: {numbers}")
assert numbers == [0, 10, 999, 20, 30, 4, 5]

# 3. Delete elements via empty assignment or del
numbers[1:3] = []
print(f"Deleted slice [1:3]: {numbers}")
assert numbers == [0, 20, 30, 4, 5]

# 4. Clear all elements in-place: numbers[:] = []
numbers[:] = [1, 2, 3]
print(f"Overwrote entire list in-place: {numbers}")
assert id(numbers) == list_id  # Same memory identity!

# =====================================================================
# 4. Named Slices with slice() Object
# =====================================================================
# In production code (parsing fixed-width logs or files), avoid hardcoded numbers:
log_record = "2026-09-20 ERROR DatabaseConnectionTimeout"
DATE_SLICE = slice(0, 10)
LEVEL_SLICE = slice(11, 16)
MSG_SLICE = slice(17, None)

print("\n--- 4. Named slice Objects ---")
print(f"Date:    {log_record[DATE_SLICE]}")
print(f"Level:   {log_record[LEVEL_SLICE]}")
print(f"Message: {log_record[MSG_SLICE]}")

# =====================================================================
# 5. Self-Testing Verification
# =====================================================================
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1: Extract the middle 4 elements ([4, 5, 6, 7])
middle = data[3:7]
assert middle == [4, 5, 6, 7]

# Exercise 2: Reverse only elements from index 2 to 6 in-place
sub_reversed = data[2:7][::-1]
data[2:7] = sub_reversed
assert data == [1, 2, 7, 6, 5, 4, 3, 8, 9, 10]

# Exercise 3: Palindrome verification using slicing
def is_palindrome(s: str) -> bool:
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False

print("\nAll 02_slicing_mastery self-tests passed successfully!")
