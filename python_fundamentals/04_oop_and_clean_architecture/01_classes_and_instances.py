"""
Module 04: Object-Oriented Programming (OOP) & Clean Architecture
Lesson 01: Classes, Instances, Bound Methods, Class vs Instance State, and __slots__

Run this file with:
    python 01_classes_and_instances.py
"""

import sys
from typing import ClassVar, Dict, List, Optional, Tuple

# =====================================================================
# 1. Class Anatomy & The `self` Binding Protocol
# =====================================================================
# In Python, a class is a blueprint that defines state and behavior.
# When an instance method is called, Python automatically passes the
# instance itself as the first argument, conventionally named `self`.
#
# Unlike C++ or Java (where `this` is an implicit hidden keyword),
# Python makes `self` explicit ("Explicit is better than implicit").

class BankAccount:
    """A clean domain entity representing a checking bank account."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        # Instance attributes stored inside the instance's __dict__:
        self.owner: str = owner
        self.balance: float = initial_balance
        self.transactions: List[float] = [initial_balance] if initial_balance > 0 else []

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive")
        self.balance += amount
        self.transactions.append(amount)
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be strictly positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: balance {self.balance} < requested {amount}")
        self.balance -= amount
        self.transactions.append(-amount)
        return self.balance


# Instantiation
acc1 = BankAccount("Alice", 100.0)
acc2 = BankAccount("Bob", 50.0)

# Calling instance method syntax:
acc1.deposit(50.0)
assert acc1.balance == 150.0
assert acc1.transactions == [100.0, 50.0]

# Under the hood: acc1.deposit(50.0) is syntactic sugar for:
# BankAccount.deposit(acc1, 50.0)
BankAccount.deposit(acc2, 25.0)
assert acc2.balance == 75.0
assert acc2.transactions == [50.0, 25.0]

# Proving state isolation between instances:
assert acc1.balance != acc2.balance
assert acc1.transactions is not acc2.transactions
print("--- 1. Class Anatomy & Instance Binding (`self`): PASSED ---")

# =====================================================================
# 2. Object Lifecycle: `__new__` (Allocator) vs `__init__` (Initializer)
# =====================================================================
# In Python, object creation is a two-step process:
# 1. `__new__(cls, ...)`: STATIC method that allocates raw heap memory
#    and returns a brand-new instance of `cls`.
# 2. `__init__(self, ...)`: INSTANCE method that receives that new instance
#    and populates its attributes.
#
# Use cases for overriding `__new__`:
# - Implementing the Singleton Pattern
# - Subclassing immutable types (like `int`, `str`, `tuple`)
# - Metaclass construction

class SingletonDatabase:
    """Thread-unsafe demonstration of the Singleton pattern via __new__."""

    _instance: Optional["SingletonDatabase"] = None

    def __new__(cls, connection_string: str = "sqlite:///:memory:") -> "SingletonDatabase":
        if cls._instance is None:
            # Allocate the single instance via super().__new__
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # type: ignore[attr-defined]
        return cls._instance

    def __init__(self, connection_string: str = "sqlite:///:memory:") -> None:
        # Guard to prevent re-initialization if already initialized:
        if getattr(self, "_initialized", False):
            return
        self.connection_string: str = connection_string
        self._initialized: bool = True


db1 = SingletonDatabase("postgres://prod-db:5432/main")
db2 = SingletonDatabase("postgres://analytics-db:5432/warehouse")

assert db1 is db2  # Both point to the EXACT same object in memory!
assert db2.connection_string == "postgres://prod-db:5432/main"  # Preserved original config
print("--- 2. Object Lifecycle (__new__ vs __init__): PASSED ---")

# =====================================================================
# 3. Instance Attributes vs Class Attributes & The Shadowing Trap
# =====================================================================
# Class attributes: Shared across ALL instances; live in Class.__dict__.
# Instance attributes: Unique to EACH instance; live in self.__dict__.
#
# Resolution order:
# Python looks for an attribute in:
#   1. instance.__dict__
#   2. Class.__dict__
#   3. Base classes (via MRO)

class Employee:
    # Class attributes (shared across all employees):
    company_name: ClassVar[str] = "Acme Corp"
    min_hourly_wage: ClassVar[float] = 15.0
    total_employees: ClassVar[int] = 0

    def __init__(self, name: str, hourly_wage: float) -> None:
        self.name: str = name  # Instance attribute
        self.hourly_wage: float = max(hourly_wage, Employee.min_hourly_wage)
        # Safely increment class-level counter:
        Employee.total_employees += 1


e1 = Employee("Alice", 25.0)
e2 = Employee("Bob", 12.0)

# Bob receives min wage:
assert e2.hourly_wage == 15.0
assert Employee.total_employees == 2

# Accessing class attribute via instance or class:
assert e1.company_name == "Acme Corp"
assert e2.company_name == "Acme Corp"
assert Employee.company_name == "Acme Corp"

# =====================================================================
# THE DEADLY TRAP: Attribute Shadowing
# If you assign to `e1.company_name`, you DO NOT modify the class attribute!
# You create a new instance attribute on `e1` that shadows the class attribute!
# =====================================================================
e1.company_name = "Acme Global Ventures"  # Creates instance variable in e1.__dict__!

assert e1.company_name == "Acme Global Ventures"
assert e2.company_name == "Acme Corp"           # Unaffected!
assert Employee.company_name == "Acme Corp"     # Unaffected!

assert "company_name" in e1.__dict__
assert "company_name" not in e2.__dict__

# To change it globally for all instances, mutate on the class directly:
Employee.min_hourly_wage = 18.0
assert Employee.min_hourly_wage == 18.0
print("--- 3. Class Attributes vs Instance Attributes & Shadowing: PASSED ---")

# =====================================================================
# 4. Method Types: Instance Methods, @classmethod, and @staticmethod
# =====================================================================
# 1. Instance Method: Takes `self`. Reads and mutates instance state.
# 2. @classmethod: Takes `cls`. Reads and mutates class state.
#    Primary use case: Alternative Factory Constructors!
# 3. @staticmethod: Takes neither `self` nor `cls`. Pure utility function
#    that conceptually belongs inside the class namespace.

class Configuration:
    default_env: ClassVar[str] = "development"

    def __init__(self, host: str, port: int, env: str) -> None:
        self.host: str = host
        self.port: int = port
        self.env: str = env

    @classmethod
    def from_string(cls, uri_string: str) -> "Configuration":
        """Alternative factory constructor: parse 'host:port' format."""
        parts = uri_string.split(":")
        host = parts[0]
        port = int(parts[1]) if len(parts) > 1 else 8080
        # Call cls(...) to return a fresh instance:
        return cls(host, port, cls.default_env)

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "Configuration":
        """Alternative factory constructor: parse dictionary payload."""
        return cls(
            host=str(data.get("host", "localhost")),
            port=int(str(data.get("port", 8080))),
            env=str(data.get("env", cls.default_env))
        )

    @staticmethod
    def is_valid_port(port: int) -> bool:
        """Pure validation helper function without accessing self or cls."""
        return 1 <= port <= 65535


# Standard constructor
c1 = Configuration("127.0.0.1", 3000, "staging")
assert (c1.host, c1.port, c1.env) == ("127.0.0.1", 3000, "staging")

# Alternative constructor via @classmethod
c2 = Configuration.from_string("api.internal.net:9000")
assert (c2.host, c2.port, c2.env) == ("api.internal.net", 9000, "development")

c3 = Configuration.from_dict({"host": "cache.redis", "port": 6379, "env": "production"})
assert (c3.host, c3.port, c3.env) == ("cache.redis", 6379, "production")

# Utility function via @staticmethod
assert Configuration.is_valid_port(8080) is True
assert Configuration.is_valid_port(99999) is False
assert Configuration.is_valid_port(-1) is False
print("--- 4. Method Types (Instance, @classmethod, @staticmethod): PASSED ---")

# =====================================================================
# 5. Dynamic Reflection: getattr, setattr, hasattr, and delattr
# =====================================================================
# Python provides built-in functions to introspect and modify objects dynamically:

class MetricPoint:
    def __init__(self, timestamp: int, value: float) -> None:
        self.timestamp: int = timestamp
        self.value: float = value


point = MetricPoint(1700000000, 42.5)

# hasattr: checks existence
assert hasattr(point, "timestamp") is True
assert hasattr(point, "anomaly_score") is False

# getattr: dynamically read with optional default fallback
assert getattr(point, "value") == 42.5
assert getattr(point, "anomaly_score", 0.0) == 0.0

# setattr: dynamically write or create
setattr(point, "anomaly_score", 0.95)
assert point.anomaly_score == 0.95  # type: ignore[attr-defined]

# delattr: delete attribute
delattr(point, "anomaly_score")
assert hasattr(point, "anomaly_score") is False
print("--- 5. Dynamic Introspection & Reflection: PASSED ---")

# =====================================================================
# 6. Memory Mechanics: `__slots__` Optimization
# =====================================================================
# By default, Python instances store attributes in a dynamic `__dict__`
# hash table. This provides dynamic flexibility, but comes at a steep cost:
# - Each `__dict__` consumes ~150-300 bytes of heap memory.
# - Lookups require hash table collision resolution.
#
# `__slots__` tells Python NOT to allocate a `__dict__` for instances!
# Instead, Python allocates a fixed C-array of descriptor pointers:
# Benefits:
# 1. 40% - 60% memory reduction per instance (critical for 1M+ objects / graph nodes).
# 2. Faster attribute access.
# 3. Prevents accidental addition of misspelled attributes (`obj.vlaue = 10` raises AttributeError).

class RegularNode:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


class SlottedNode:
    # Explicitly declare fixed attribute slots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


reg = RegularNode(1.0, 2.0, 3.0)
slotted = SlottedNode(1.0, 2.0, 3.0)

# Regular node has an underlying __dict__:
assert hasattr(reg, "__dict__") is True
assert reg.__dict__ == {"x": 1.0, "y": 2.0, "z": 3.0}

# Slotted node has NO __dict__!
assert hasattr(slotted, "__dict__") is False

# Attempting to assign an undeclared attribute on a slotted object raises AttributeError:
try:
    slotted.unregistered_attribute = 999  # type: ignore[attr-defined]
    raise AssertionError("Should have raised AttributeError!")
except AttributeError as e:
    print(f"Caught expected __slots__ AttributeError: {e}")

# Memory footprint proof:
reg_memory = sys.getsizeof(reg) + sys.getsizeof(reg.__dict__)
slotted_memory = sys.getsizeof(slotted)
assert slotted_memory < reg_memory
print(f"Regular instance + __dict__: {reg_memory} bytes | Slotted instance: {slotted_memory} bytes")
print("--- 6. High-Performance `__slots__` Memory Optimization: PASSED ---")

print("\n=======================================================")
print("ALL LESSON 01 ASSERTIONS PASSED! CLASSES & INSTANCES MASTERED.")
print("=======================================================")
