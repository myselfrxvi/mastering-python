"""
Module 02: Data Structures & Pythonic Idioms
Lesson 01: Dynamic Arrays, Mutability, and Memory References

Run this file with:
    python 01_lists_and_mutability.py
"""

import copy
import sys

# =====================================================================
# 1. What is a Python List? (CPython PyListObject)
# =====================================================================
# In Python, lists are NOT linked lists. They are DYNAMIC ARRAYS of
# pointers (references) to objects on the heap.
#
# Memory Layout:
# List object: [ ptr_0 | ptr_1 | ptr_2 | ... ]
#                 │       │       │
#                 ▼       ▼       ▼
#               Obj_A   Obj_B   Obj_C

nums = [10, 20, 30]
print("--- 1. List Inspection & Memory ---")
print(f"nums: {nums}")
print(f"Length: {len(nums)}")
print(f"Memory size of list object itself (bytes): {sys.getsizeof(nums)}")

# =====================================================================
# 2. In-Place Mutations vs New List Creations
# =====================================================================
# Lists are MUTABLE. You can change their contents in place without
# altering the identity (memory address) of the list.

original_id = id(nums)
nums.append(40)          # O(1) amortized: Appends at the end
nums.extend([50, 60])    # O(K): Appends multiple elements from iterable
nums.insert(0, 5)        # O(N): Shifts all elements rightward! Avoid in hot loops.

print("\n--- 2. In-Place Modifications ---")
print(f"After modifications: {nums}")
print(f"Did identity change? {id(nums) == original_id}")  # True!

popped_item = nums.pop()      # O(1): Removes and returns last element (60)
removed_first = nums.pop(0)   # O(N): Removes first element (5), shifts rest left
nums.remove(30)               # O(N): Finds first occurrence of value 30 and removes it

print(f"Popped item: {popped_item}")
print(f"Removed first item: {removed_first}")
print(f"After pops and remove: {nums}")

# =====================================================================
# 3. The Golden Trap: Aliasing vs Copying
# =====================================================================
print("\n--- 3. Aliasing vs Copying ---")

# Aliasing: Two variable names pointing to the EXACT same object
a = [1, 2, 3]
b = a
b.append(99)
print(f"Aliasing: b modified -> a is also modified: {a}")
assert a is b  # 'is' checks identical memory address (id(a) == id(b))

# Shallow Copy: Creates a new container, but elements inside still point to same items
c = a.copy()    # Equivalent to c = list(a) or c = a[:]
c.append(500)
print(f"Shallow Copy: c modified -> a is unaffected: a={a}, c={c}")
assert c is not a
assert c != a

# Deep Copy Trap with Nested Objects:
nested = [[1, 2], [3, 4]]
shallow_nested = nested.copy()
shallow_nested[0].append(999)
# The inner list [1, 2] was modified because shallow copy copies the pointers!
print(f"Shallow copy on nested list: nested[0] is modified: {nested[0]}")
assert nested[0] == [1, 2, 999]

# True Isolation requires deepcopy:
safe_nested = copy.deepcopy(nested)
safe_nested[0].append(888)
print(f"Deep copy isolation: nested[0]={nested[0]} vs safe[0]={safe_nested[0]}")
assert nested[0] != safe_nested[0]

# =====================================================================
# 4. Self-Testing Verification
# =====================================================================
# Exercise 1: Build a list [1, 2, 3], append 4, pop the first element,
# and verify length and contents.
test_list = [1, 2, 3]
test_list.append(4)
first = test_list.pop(0)
assert first == 1
assert test_list == [2, 3, 4]

# Exercise 2: Sort in-place vs sorted() returning a new list
unsorted = [5, 2, 8, 1, 9]
new_sorted = sorted(unsorted)
assert unsorted == [5, 2, 8, 1, 9]     # original unchanged
assert new_sorted == [1, 2, 5, 8, 9]

unsorted.sort()                         # in-place sort
assert unsorted == [1, 2, 5, 8, 9]

print("\nAll 01_lists_and_mutability self-tests passed successfully!")
