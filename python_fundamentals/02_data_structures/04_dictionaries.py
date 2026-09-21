"""
Module 02: Data Structures & Pythonic Idioms
Lesson 04: Dictionaries, Hash Tables & Dynamic Views

Run this file with:
    python 04_dictionaries.py
"""

from collections import Counter, defaultdict

# =====================================================================
# 1. How Python Dictionaries Work (CPython Hash Table)
# =====================================================================
# Under the hood, Python dicts use a sparse hash table with open addressing.
# Since Python 3.7, dictionaries maintain INSERTION ORDER by using a compact
# array of indices pointing to entries!
#
# Lookup / Insert / Delete Time Complexity:
# - Average Case: O(1)
# - Worst Case (extreme hash collisions): O(N)

user_profile = {
    "username": "coder_pro",
    "level": 42,
    "verified": True,
}

print("--- 1. Dictionary Operations ---")
print(f"user_profile: {user_profile}")

# Access: Direct lookup raises KeyError if missing!
# Safe access: .get() provides an optional fallback default
print(f"Direct lookup: {user_profile['username']}")
print(f"Safe lookup:   {user_profile.get('bio', 'No bio provided')}")
assert user_profile.get("bio") is None
assert user_profile.get("bio", "Default") == "Default"

# =====================================================================
# 2. Mutating Dictionaries
# =====================================================================
# 1. Assignment / Overwrite
user_profile["location"] = "Tokyo"

# 2. .setdefault(key, default): Sets only if key DOES NOT exist, returns value
bio = user_profile.setdefault("bio", "Software Architect")
print(f"\nAfter setdefault: bio = {bio}")
# Calling again returns existing value without overwriting:
same_bio = user_profile.setdefault("bio", "Different Bio")
assert same_bio == "Software Architect"

# 3. .update(): Merge another dictionary or key-value pairs
user_profile.update({"country": "Japan", "level": 43})
print(f"After update: {user_profile}")
assert user_profile["level"] == 43

# 4. .pop(key, default): Removes key and returns value
removed_country = user_profile.pop("country", None)
assert removed_country == "Japan"
assert "country" not in user_profile

# =====================================================================
# 3. Dictionary Views (.keys(), .values(), .items())
# =====================================================================
# Dict views are dynamic and reflect underlying dictionary changes instantly!
# Keys views even support set operations (&, |, -)!

inventory = {"apples": 5, "oranges": 10, "bananas": 8}
keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()

print("\n--- 2. Dynamic Views ---")
print(f"Keys:   {list(keys_view)}")
print(f"Values: {list(values_view)}")

# Set operations on dict keys:
wishlist = {"apples": 2, "strawberries": 15, "mangoes": 4}
common_items = inventory.keys() & wishlist.keys()
print(f"Common keys (&): {common_items}")
assert common_items == {"apples"}

# =====================================================================
# 4. Pro Patterns: defaultdict and Counter
# =====================================================================
print("\n--- 3. collections.defaultdict & Counter ---")

# defaultdict: Eliminates KeyError by automatically instantiating missing keys!
grouped = defaultdict(list)
pairs = [("frontend", "React"), ("backend", "FastAPI"), ("frontend", "Vue"), ("backend", "Django")]
for category, tech in pairs:
    grouped[category].append(tech)

print("Grouped by category:", dict(grouped))
assert grouped["frontend"] == ["React", "Vue"]
assert grouped["backend"] == ["FastAPI", "Django"]

# Counter: High-performance multiset / frequency tracker
text = "banana"
char_counts = Counter(text)
print(f"Counter for '{text}': {char_counts}")
print(f"Most common 2 elements: {char_counts.most_common(2)}")
assert char_counts["a"] == 3
assert char_counts["b"] == 1
assert char_counts["z"] == 0  # Missing key returns 0 instead of KeyError!

# =====================================================================
# 5. Self-Testing Verification
# =====================================================================
# Exercise 1: Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {val: key for key, val in original.items()}
assert inverted == {1: "a", 2: "b", 3: "c"}

# Exercise 2: Word frequency counter with dictionary
words = ["python", "java", "python", "rust", "python", "rust"]
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
assert freq == {"python": 3, "java": 1, "rust": 2}

print("\nAll 04_dictionaries self-tests passed successfully!")
