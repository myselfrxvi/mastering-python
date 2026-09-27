"""
Module 03: Functions, Scope & Functional Idioms
Lesson 01: Function Signatures, Boundary Operators (/ and *), and Default Argument Traps

Run this file with:
    python 01_function_signatures.py
"""

from typing import List, Optional, Tuple

# =====================================================================
# 1. Modern Typed Signatures
# =====================================================================
# Python type annotations do not enforce runtime types by default,
# but they provide critical documentation, IDE autocomplete, and mypy validation.

def calculate_tax(gross_income: float, tax_rate: float = 0.20) -> float:
    """Calculate net tax with a default 20% rate."""
    return gross_income * tax_rate

assert calculate_tax(1000.0) == 200.0
assert calculate_tax(1000.0, 0.15) == 150.0
assert calculate_tax(tax_rate=0.30, gross_income=500.0) == 150.0
print("--- 1. Basic Typed Signatures: PASSED ---")

# =====================================================================
# 2. Positional-Only Parameters: The `/` Boundary
# =====================================================================
# All parameters BEFORE `/` CANNOT be passed by keyword name.
# Callers MUST provide them by position.
#
# Use cases:
# - API stability: Callers can't depend on parameter names that might change.
# - High-performance built-in parity (like len("abc"), not len(obj="abc")).

def power(base: float, exponent: float, /) -> float:
    return base ** exponent

assert power(2.0, 3.0) == 8.0

# Calling power(base=2.0, exponent=3.0) will raise TypeError!
try:
    # Intentionally trigger the error to demonstrate the constraint:
    power(base=2.0, exponent=3.0)  # type: ignore
except TypeError as e:
    print("--- 2. Positional-Only Enforcement (/) ---")
    print(f"Caught expected TypeError: {e}")

# =====================================================================
# 3. Keyword-Only Parameters: The `*` Boundary
# =====================================================================
# All parameters AFTER `*` CANNOT be passed positionally.
# Callers MUST supply their names explicitly.
#
# Prevents deadly "boolean blindness":
# compare(a, b, True, False, True) -> What does each boolean mean?!
# compare(a, b, ignore_case=True, trim_spaces=False, strict=True) -> 100% Clear!

def create_user(
    username: str,
    *,
    is_admin: bool = False,
    is_active: bool = True
) -> dict:
    return {
        "username": username,
        "is_admin": is_admin,
        "is_active": is_active
    }

user1 = create_user("alice", is_admin=True)
assert user1 == {"username": "alice", "is_admin": True, "is_active": True}

# Passing positionally create_user("bob", True) raises TypeError!
try:
    create_user("bob", True)  # type: ignore
except TypeError as e:
    print("\n--- 3. Keyword-Only Enforcement (*) ---")
    print(f"Caught expected TypeError: {e}")

# =====================================================================
# 4. The Combined Clean Master Signature: / and *
# =====================================================================
def configure_cache(
    capacity: int,       # Positional-only
    /,
    eviction_policy: str = "LRU", # Standard (positional or keyword)
    *,
    ttl_seconds: int = 3600,      # Keyword-only
    enable_metrics: bool = True   # Keyword-only
) -> Tuple[int, str, int, bool]:
    return capacity, eviction_policy, ttl_seconds, enable_metrics

cfg = configure_cache(1024, "FIFO", ttl_seconds=600, enable_metrics=False)
assert cfg == (1024, "FIFO", 600, False)
print("\n--- 4. Master Signature Combined: PASSED ---")

# =====================================================================
# 5. THE DEADLY TRAP: Mutable Default Arguments
# =====================================================================
# Default arguments are evaluated ONCE at function DEFINITION time,
# NOT each time the function is called!
# If the default is mutable (list, dict, set), it is shared across all calls!

def bad_append(item: int, target: List[int] = []) -> List[int]:  # Dangerous!
    target.append(item)
    return target

# First call: target is created and gets [1]
call1 = bad_append(1)
# Second call: target is the SAME shared list in memory and gets [1, 2]!
call2 = bad_append(2)

print("\n--- 5. The Mutable Default Trap ---")
print(f"call1 result: {call1}")
print(f"call2 result: {call2}")
assert call1 is call2  # They point to the EXACT same list in memory!

# =====================================================================
# 6. The Production Fix: Sentinel `None`
# =====================================================================
# Always use None as the default for mutable structures,
# and instantiate a fresh instance inside the function body.

def safe_append(item: int, target: Optional[List[int]] = None) -> List[int]:
    if target is None:
        target = []
    target.append(item)
    return target

safe1 = safe_append(1)
safe2 = safe_append(2)
assert safe1 == [1]
assert safe2 == [2]
assert safe1 is not safe2  # Completely independent lists!
print("Safe append isolation verified: PASSED")

print("\n=======================================================")
print("ALL LESSON 01 ASSERTIONS PASSED! SIGNATURES MASTERED.")
print("=======================================================")
