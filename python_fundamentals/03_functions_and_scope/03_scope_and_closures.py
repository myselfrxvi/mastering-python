"""
Module 03: Functions, Scope & Functional Idioms
Lesson 03: Lexical Scope (LEGB), Global vs Nonlocal, Closures & The Late-Binding Trap

Run this file with:
    python 03_scope_and_closures.py
"""

# =====================================================================
# 1. The LEGB Scope Resolution Hierarchy
# =====================================================================
# L: Local      (Names assigned inside the current function)
# E: Enclosing  (Names in any enclosing outer functions)
# G: Global     (Module-level names)
# B: Built-in   (Python's built-in namespace: len, range, str, etc.)

x = "GLOBAL_X"

def outer():
    x = "ENCLOSING_X"
    def inner():
        x = "LOCAL_X"
        return x
    return inner()

assert outer() == "LOCAL_X"
assert x == "GLOBAL_X"
print("--- 1. LEGB Hierarchy: PASSED ---")

# =====================================================================
# 2. Modifying Enclosing Scope: `nonlocal` vs `global`
# =====================================================================
# In Python, assigning to a variable automatically marks it as LOCAL
# to that function scope unless declared otherwise!

counter_global = 0

def increment_global():
    global counter_global
    counter_global += 1

increment_global()
increment_global()
assert counter_global == 2

def make_counter(start: int = 0):
    count = start
    def step():
        nonlocal count  # Binds to the enclosing `count`, NOT global!
        count += 1
        return count
    return step

c1 = make_counter(10)
c2 = make_counter(100)

assert c1() == 11
assert c1() == 12
assert c2() == 101  # c2 has its own completely isolated closure state!
print("--- 2. Global vs Nonlocal: PASSED ---")

# =====================================================================
# 3. What is a Closure? CPython `cell` Objects
# =====================================================================
# A closure is a function that retains access to free variables from its
# enclosing lexical scope even after the outer function has finished executing!
#
# Under the hood, CPython creates a `cell` object in the function's `__closure__`
# tuple that acts as a reference to the shared heap value:

closure_fn = make_counter(500)
assert closure_fn.__closure__ is not None
# The cell object wraps the live value:
cell = closure_fn.__closure__[0]
assert cell.cell_contents == 500
closure_fn()
assert cell.cell_contents == 501  # Value mutated inside the cell!
print("--- 3. Closure Cell Internals (__closure__): PASSED ---")

# =====================================================================
# 4. THE DEADLY TRAP: Late-Binding Closures in Loops
# =====================================================================
# Python closures bind to the variable NAME, NOT the value at definition time!
# If you create closures inside a loop, all closures look up the variable
# at the time they are CALLED, by which point the loop has finished!

bad_handlers = []
for i in range(4):
    bad_handlers.append(lambda: i)  # Binds to `i` by name!

# Everyone returns 3! Because at call time, i == 3!
results_bad = [fn() for fn in bad_handlers]
print(f"\n--- 4. Late-Binding Trap Results: {results_bad} ---")
assert results_bad == [3, 3, 3, 3]

# =====================================================================
# 5. The Production Fix: Default Argument Binding
# =====================================================================
# Function default arguments are evaluated at DEFINITION time.
# By setting `val=i`, we capture the current value of `i` as a default:

good_handlers = []
for i in range(4):
    good_handlers.append(lambda val=i: val)  # Early-binds `val`!

results_good = [fn() for fn in good_handlers]
print(f"Fixed Early-Binding Results: {results_good}")
assert results_good == [0, 1, 2, 3]

print("\n=======================================================")
print("ALL LESSON 03 ASSERTIONS PASSED! SCOPE & CLOSURES MASTERED.")
print("=======================================================")
