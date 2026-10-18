"""
Module 04: Object-Oriented Programming (OOP) & Clean Architecture
Lesson 04: Encapsulation, Name Mangling, @property, Descriptors, and Domain Invariants

Run this file with:
    python 04_encapsulation_properties.py
"""

from functools import cached_property
import math
import time
from typing import Any, Dict, List, Optional

# =====================================================================
# 1. Access Conventions & Name Mangling Mechanics
# =====================================================================
# Python does NOT have strict compiler-enforced access specifiers (private/public).
# Philosophy: "We are all consenting adults here."
#
# Three Tiers of Access:
# 1. `name` (Public): Part of the official public interface.
# 2. `_name` (Protected): Strong naming convention indicating internal implementation.
#    Linters flag external access, but CPython does not prohibit it.
# 3. `__name` (Private / Name Mangling): CPython mechanically rewrites `__name` to
#    `_ClassName__name` inside bytecode!
#    Purpose: Avoid ACCIDENTAL variable collisions in subclasses, NOT security!

class BasePaymentMethod:
    def __init__(self, token: str) -> None:
        self.public_provider = "Stripe"
        self._internal_retry_count = 3       # Protected convention
        self.__secret_vault_token = token    # Name-mangled private attribute

    def get_token_prefix(self) -> str:
        return self.__secret_vault_token[:4]


class SubclassedPayment(BasePaymentMethod):
    def __init__(self, token: str, network: str) -> None:
        super().__init__(token)
        # Defining __secret_vault_token in child will NOT collide with parent:
        self.__secret_vault_token = f"child_salt_{token}"


pay = BasePaymentMethod("tok_live_987654321")
assert pay.public_provider == "Stripe"
assert pay._internal_retry_count == 3
assert pay.get_token_prefix() == "tok_"

# Direct access to `pay.__secret_vault_token` raises AttributeError:
try:
    _ = pay.__secret_vault_token  # type: ignore[attr-defined]
    raise AssertionError("Should have raised AttributeError!")
except AttributeError as e:
    print(f"Caught expected name-mangled AttributeError: {e}")

# Under the hood, Python renamed it to `_BasePaymentMethod__secret_vault_token`:
assert "_BasePaymentMethod__secret_vault_token" in pay.__dict__
assert pay._BasePaymentMethod__secret_vault_token == "tok_live_987654321"

# Proving collision avoidance in subclass:
sub_pay = SubclassedPayment("tok_live_987654321", "Visa")
assert "_BasePaymentMethod__secret_vault_token" in sub_pay.__dict__
assert "_SubclassedPayment__secret_vault_token" in sub_pay.__dict__
assert sub_pay._BasePaymentMethod__secret_vault_token != sub_pay._SubclassedPayment__secret_vault_token
print("--- 1. Access Conventions & Name Mangling: PASSED ---")

# =====================================================================
# 2. The Pythonic @property Protocol: Uniform Access Principle
# =====================================================================
# In Java or C++, developers write boilerplate getters and setters:
#   account.getBalance(), account.setBalance(50)
#
# IN PYTHON, THIS IS AN ANTI-PATTERN!
# The Uniform Access Principle states that all services offered by a module
# should be available through a uniform notation.
# Start with plain public attributes: `account.balance`
# If validation or computed logic is needed later, wrap with `@property`
# WITHOUT breaking a single line of caller code!

class TemperatureSensor:
    """Encapsulates temperature with automatic unit conversion and validation."""

    ABSOLUTE_ZERO_CELSIUS = -273.15

    def __init__(self, celsius: float = 20.0) -> None:
        # Use property setter for invariant validation:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Getter: returns temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Setter: validates physical constraint."""
        if value < self.ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(f"Temperature cannot be below absolute zero ({self.ABSOLUTE_ZERO_CELSIUS}°C)")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        """Computed property: converts Celsius to Fahrenheit."""
        return (self._celsius * 9.0 / 5.0) + 32.0

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Setter: sets Celsius from Fahrenheit input."""
        self.celsius = (value - 32.0) * 5.0 / 9.0


sensor = TemperatureSensor(0.0)
assert sensor.celsius == 0.0
assert sensor.fahrenheit == 32.0

sensor.celsius = 100.0
assert sensor.fahrenheit == 212.0

sensor.fahrenheit = 68.0
assert math.isclose(sensor.celsius, 20.0)

# Violation of domain invariant raises ValueError:
try:
    sensor.celsius = -300.0
    raise AssertionError("Should have raised ValueError!")
except ValueError as e:
    print(f"Caught expected temperature ValueError: {e}")
print("--- 2. Pythonic @property & Invariant Enforcement: PASSED ---")

# =====================================================================
# 3. High-Performance Caching: @functools.cached_property
# =====================================================================
# For expensive calculations that should only be computed once per instance,
# `@cached_property` computes the value on first access and stores it directly
# in the instance's `__dict__`.
# Subsequent accesses read directly from `__dict__`, bypassing the getter!

class DatasetRecord:
    def __init__(self, raw_numbers: List[float]) -> None:
        self.raw_numbers: List[float] = raw_numbers
        self.computation_count: int = 0

    @cached_property
    def variance(self) -> float:
        """Expensive O(N) calculation computed only once."""
        self.computation_count += 1
        n = len(self.raw_numbers)
        if n <= 1:
            return 0.0
        mean = sum(self.raw_numbers) / n
        return sum((x - mean) ** 2 for x in self.raw_numbers) / (n - 1)


dataset = DatasetRecord([10.0, 20.0, 30.0, 40.0, 50.0])
assert dataset.computation_count == 0  # Not yet computed (lazy!)

# First access triggers calculation:
var1 = dataset.variance
assert math.isclose(var1, 250.0)
assert dataset.computation_count == 1

# Second access reads directly from instance __dict__:
var2 = dataset.variance
assert var1 == var2
assert dataset.computation_count == 1  # No re-computation!

# Invalidation: To clear cache, simply delete the key from instance:
del dataset.variance
var3 = dataset.variance
assert dataset.computation_count == 2  # Recomputed!
print("--- 3. Lazy High-Performance @cached_property: PASSED ---")

# =====================================================================
# 4. The Descriptor Protocol: The Engine Behind Properties
# =====================================================================
# What makes `@property`, methods, and `@classmethod` work?
# The Python DESCRIPTOR PROTOCOL!
#
# A descriptor is any object that implements at least one of:
# - `__get__(self, instance, owner)`
# - `__set__(self, instance, value)`
# - `__delete__(self, instance)`
#
# Data Descriptor: Implements `__set__` or `__delete__`.
#   Takes precedence over instance `__dict__`!
# Non-Data Descriptor: Implements only `__get__` (e.g. regular methods).
#
# Clean Architecture Benefit:
# Descriptors eliminate repetitive property validation across multiple fields!

class ValidatedFloat:
    """Reusable Data Descriptor enforcing min and max bounds."""

    def __init__(self, min_val: Optional[float] = None, max_val: Optional[float] = None) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner: type, name: str) -> None:
        # Python 3.6+ automatically tells the descriptor its attribute name:
        self.private_name = f"_{name}"

    def __get__(self, instance: Optional[object], owner: type) -> Any:
        if instance is None:
            # Accessed on the class directly (e.g. Product.price):
            return self
        return getattr(instance, self.private_name, 0.0)

    def __set__(self, instance: object, value: Any) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be a number, got {type(value).__name__}")
        float_val = float(value)
        if self.min_val is not None and float_val < self.min_val:
            raise ValueError(f"Value {float_val} is less than minimum {self.min_val}")
        if self.max_val is not None and float_val > self.max_val:
            raise ValueError(f"Value {float_val} exceeds maximum {self.max_val}")
        setattr(instance, self.private_name, float_val)


class FinancialProduct:
    # Clean, declarative attribute validation with ZERO repetitive boilerplate:
    price = ValidatedFloat(min_val=0.01)
    risk_score = ValidatedFloat(min_val=0.0, max_val=10.0)

    def __init__(self, symbol: str, price: float, risk_score: float) -> None:
        self.symbol = symbol
        self.price = price            # Invokes ValidatedFloat.__set__
        self.risk_score = risk_score  # Invokes ValidatedFloat.__set__


product = FinancialProduct("AAPL", 185.50, 4.2)
assert product.price == 185.50
assert product.risk_score == 4.2

# Invariant violation:
try:
    product.price = -10.0
    raise AssertionError("Should have raised ValueError!")
except ValueError as e:
    print(f"Caught expected descriptor ValueError: {e}")

try:
    product.risk_score = 15.0
    raise AssertionError("Should have raised ValueError!")
except ValueError as e:
    print(f"Caught expected descriptor bounds ValueError: {e}")
print("--- 4. Descriptor Protocol & Reusable Validation: PASSED ---")

# =====================================================================
# 5. Clean Architecture: Production Domain Aggregate (Finite State Machine)
# =====================================================================
# In Clean Architecture / Domain-Driven Design (DDD):
# An Aggregate Root encapsulates entities, enforces invariants, and
# prevents invalid state transitions.

class OrderStatus:
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"


class OrderAggregate:
    """Domain aggregate encapsulating line items, financial totals, and state transitions."""

    VALID_TRANSITIONS = {
        OrderStatus.DRAFT: {OrderStatus.SUBMITTED, OrderStatus.CANCELLED},
        OrderStatus.SUBMITTED: {OrderStatus.APPROVED, OrderStatus.CANCELLED},
        OrderStatus.APPROVED: set(),  # Terminal state
        OrderStatus.CANCELLED: set(), # Terminal state
    }

    def __init__(self, order_id: str, customer_id: str) -> None:
        self._order_id: str = order_id
        self._customer_id: str = customer_id
        self._items: Dict[str, Tuple[int, float]] = {}  # sku -> (qty, unit_price)
        self._status: str = OrderStatus.DRAFT

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def status(self) -> str:
        return self._status

    @property
    def total_amount(self) -> float:
        """Dynamically calculated total amount."""
        return sum(qty * price for qty, price in self._items.values())

    def add_item(self, sku: str, quantity: int, unit_price: float) -> None:
        # Invariant: Cannot modify items unless order is in DRAFT status:
        if self._status != OrderStatus.DRAFT:
            raise RuntimeError(f"Cannot mutate items in status {self._status}")
        if quantity <= 0 or unit_price <= 0:
            raise ValueError("Quantity and price must be strictly positive")
        self._items[sku] = (quantity, unit_price)

    def transition_to(self, new_status: str) -> None:
        """Enforces finite state machine transition graph."""
        allowed = self.VALID_TRANSITIONS.get(self._status, set())
        if new_status not in allowed:
            raise ValueError(f"Illegal transition: {self._status} -> {new_status}")
        if new_status == OrderStatus.SUBMITTED and len(self._items) == 0:
            raise ValueError("Cannot submit empty order with 0 items")
        self._status = new_status


order = OrderAggregate("ORD_5001", "CUST_99")
assert order.status == OrderStatus.DRAFT
assert order.total_amount == 0.0

# Add items:
order.add_item("BOOK_PY", 2, 45.0)
order.add_item("STICKER", 5, 2.0)
assert order.total_amount == 100.0  # (2 * 45) + (5 * 2)

# State transitions:
order.transition_to(OrderStatus.SUBMITTED)
assert order.status == OrderStatus.SUBMITTED

# Mutating items once submitted is prohibited:
try:
    order.add_item("BONUS", 1, 0.0)
    raise AssertionError("Should have raised RuntimeError!")
except RuntimeError as e:
    print(f"Caught expected State Machine RuntimeError: {e}")

# Transition to approved:
order.transition_to(OrderStatus.APPROVED)
assert order.status == OrderStatus.APPROVED

# Attempting illegal transition from approved raises ValueError:
try:
    order.transition_to(OrderStatus.DRAFT)
    raise AssertionError("Should have raised ValueError!")
except ValueError as e:
    print(f"Caught expected invalid transition ValueError: {e}")
print("--- 5. Clean Architecture Domain Aggregate & State Invariants: PASSED ---")

print("\n=======================================================")
print("ALL LESSON 04 ASSERTIONS PASSED! ENCAPSULATION MASTERED.")
print("=======================================================")
