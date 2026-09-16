"""
Module 01: Basics
Lesson 04: Loops, Ranges & Pythonic Iteration

Run this file with:
    python 04_loops_and_ranges.py
"""

# =====================================================================
# 1. While Loops
# =====================================================================
print("--- 1. While Loop ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

# =====================================================================
# 2. For Loops & range(start, stop, step)
# =====================================================================
# Remember: stop is EXCLUSIVE! (stops at stop - 1)
print("\n--- 2. range() Mastery ---")
print("range(5):", list(range(5)))             # [0, 1, 2, 3, 4]
print("range(2, 7):", list(range(2, 7)))       # [2, 3, 4, 5, 6]
print("range(10, 0, -2):", list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

# =====================================================================
# 3. Pythonic Rule: NEVER do `for i in range(len(items)):`!
# =====================================================================
# Use `enumerate()` to get both index and item simultaneously:
print("\n--- 3. Enumerate in Action ---")
languages = ["Python", "Rust", "Go", "TypeScript"]
for index, lang in enumerate(languages, start=1):
    print(f"Rank {index}: {lang}")

# =====================================================================
# 4. Parallel Iteration with zip()
# =====================================================================
print("\n--- 4. zip() in Action ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# =====================================================================
# 5. The Unique `for...else` Construct
# =====================================================================
# The `else` block on a loop runs ONLY if the loop finishes normally
# without encountering a `break` statement! Great for searching!
print("\n--- 5. for...else Search ---")
def find_prime_divisor(n: int) -> int:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return d  # Found a divisor!
    else:
        return -1    # No divisor found, n is prime!

print("Divisor for 49:", find_prime_divisor(49)) # 7
print("Divisor for 17:", find_prime_divisor(17)) # -1 (Prime)

# =====================================================================
# 6. Self-Checking Exercises
# =====================================================================
print("\n--- 6. Running Self-Checking Exercises ---")

def sum_even_numbers(limit: int) -> int:
    """Return the sum of all positive even integers <= limit"""
    total = 0
    for x in range(2, limit + 1, 2):
        total += x
    return total

def find_target_index(nums: list, target: int) -> int:
    """Return index of target, or -1 if not found using enumerate"""
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1

# Verification Tests:
assert sum_even_numbers(10) == 30   # 2 + 4 + 6 + 8 + 10 = 30
assert sum_even_numbers(5) == 6     # 2 + 4 = 6
assert find_target_index([10, 20, 30, 40], 30) == 2
assert find_target_index([10, 20, 30, 40], 99) == -1

print("All tests passed! You have mastered loops and iteration in Python.")
