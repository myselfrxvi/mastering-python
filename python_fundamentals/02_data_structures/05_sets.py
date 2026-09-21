"""
Module 02: Data Structures & Pythonic Idioms
Lesson 05: Sets, Mathematical Algebra & O(1) Lookups

Run this file with:
    python 05_sets.py
"""

# =====================================================================
# 1. Sets: Hash-Based Containers with Unique Elements
# =====================================================================
# Under the hood, a set is like a dictionary with keys and NO values.
# Elements must be HASHABLE (immutable).
#
# Time Complexity:
# - Membership test (x in my_set): O(1) average!
# - Adding / Removing elements:   O(1) average!
# Compare to List: (x in my_list) is O(N) linear scan!

primes = {2, 3, 5, 7, 11}
evens = set([2, 4, 6, 8, 10])

print("--- 1. Set Creation & The Empty Set Trap ---")
print(f"primes: {primes}")
print(f"evens:  {evens}")

# THE TRAP: How to create an empty set?
empty_dict = {}          # This creates a dict!
empty_set = set()        # THIS creates an empty set!
print(f"type({{}}):     {type(empty_dict)}")
print(f"type(set()): {type(empty_set)}")
assert isinstance(empty_dict, dict)
assert isinstance(empty_set, set)

# =====================================================================
# 2. Mathematical Set Operations (Venn Diagram Algebra)
# =====================================================================
# Let A = {1, 2, 3, 4}, B = {3, 4, 5, 6}
#
#   Set A        Set B
#  ┌───────┬───┬───────┐
#  │  1 2  │3 4│  5 6  │
#  └───────┴───┴───────┘
#     A-B   A&B   B-A
#  └───────────────────┘
#          A | B

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\n--- 2. Mathematical Set Operations ---")
# 1. Union (All elements in A, B, or both): A | B
union_res = set_a | set_b
print(f"Union (A | B):                {union_res}")
assert union_res == {1, 2, 3, 4, 5, 6}

# 2. Intersection (Elements common to both): A & B
inter_res = set_a & set_b
print(f"Intersection (A & B):         {inter_res}")
assert inter_res == {3, 4}

# 3. Difference (Elements in A that are NOT in B): A - B
diff_res = set_a - set_b
print(f"Difference (A - B):           {diff_res}")
assert diff_res == {1, 2}

# 4. Symmetric Difference (Elements in A or B, but NOT both): A ^ B
sym_diff = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {sym_diff}")
assert sym_diff == {1, 2, 5, 6}

# =====================================================================
# 3. Subsets, Supersets & Disjointness
# =====================================================================
sub = {1, 2}
print("\n--- 3. Subsets & Disjointness ---")
print(f"Is sub a subset of set_a? ({sub} <= {set_a}): {sub <= set_a}")
print(f"Is set_a a superset of sub? ({set_a} >= {sub}): {set_a >= sub}")
print(f"Is sub disjoint with {{99, 100}}? {sub.isdisjoint({99, 100})}")
assert sub.issubset(set_a)
assert set_a.issuperset(sub)
assert sub.isdisjoint({99, 100})

# =====================================================================
# 4. Mutations: .remove() vs .discard()
# =====================================================================
my_set = {10, 20, 30}
my_set.add(40)

# .discard() silently ignores missing elements (safe!):
my_set.discard(999)

# .remove() raises KeyError if element does not exist:
try:
    my_set.remove(999)
except KeyError:
    print("\nCaught expected KeyError on .remove(999)")

# =====================================================================
# 5. frozenset: The Immutable, Hashable Set
# =====================================================================
# Standard sets are mutable, so they CANNOT be placed inside other sets
# or used as dictionary keys.
# Enter frozenset:
immutable_group = frozenset([1, 2, 3])
permissions = {
    immutable_group: "AdminAccessGroup",
    frozenset([4, 5]): "GuestAccessGroup"
}
print("\n--- 4. frozenset as Dictionary Keys ---")
print(f"Permissions: {permissions}")
assert permissions[immutable_group] == "AdminAccessGroup"

# =====================================================================
# 6. Self-Testing Verification
# =====================================================================
# Exercise 1: Deduplicate a list while preserving or checking uniqueness
raw_ids = [101, 102, 101, 105, 102, 108]
unique_ids = set(raw_ids)
assert unique_ids == {101, 102, 105, 108}

# Exercise 2: Find characters present in both strings
str1 = "algorithm"
str2 = "logarithm"
common_chars = set(str1) & set(str2)
assert common_chars == set(str1)

print("\nAll 05_sets self-tests passed successfully!")
