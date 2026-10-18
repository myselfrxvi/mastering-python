"""
Module 04: Object-Oriented Programming (OOP) & Clean Architecture
Lesson 03: Inheritance, super(), Method Resolution Order (MRO), and Abstract Base Classes (ABCs)

Run this file with:
    python 03_inheritance_and_mro.py
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Protocol

# =====================================================================
# 1. Single Inheritance & Initializer Chaining with super()
# =====================================================================
# In Python 3, `super()` with zero arguments dynamically binds to the
# next class in the Method Resolution Order (MRO) for the current instance.
#
# Rule: Always invoke `super().__init__(...)` to ensure base state is initialized.

class Entity:
    def __init__(self, entity_id: str, created_at: int) -> None:
        self.entity_id: str = entity_id
        self.created_at: int = created_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "created_at": self.created_at
        }


class User(Entity):
    def __init__(self, entity_id: str, created_at: int, email: str) -> None:
        # Delegate initialization to Entity:
        super().__init__(entity_id, created_at)
        self.email: str = email

    # Method extension (override and extend parent behavior):
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["email"] = self.email
        return data


u = User("usr_1001", 1700000000, "alice@company.internal")
assert isinstance(u, User)
assert isinstance(u, Entity)
assert issubclass(User, Entity)
assert u.to_dict() == {
    "entity_id": "usr_1001",
    "created_at": 1700000000,
    "email": "alice@company.internal"
}
print("--- 1. Single Inheritance & super() Chaining: PASSED ---")

# =====================================================================
# 2. The Diamond Problem & Cooperative Multiple Inheritance
# =====================================================================
# Multiple inheritance introduces the famous "Diamond of Death":
#
#            Base (A)
#           /        \
#       Left (B)    Right (C)
#           \        /
#            Child (D)
#
# NAIVE PITFALL:
# If B and C explicitly call `A.__init__(self)` by name, then A.__init__
# gets executed TWICE when constructing D!
#
# PYTHONIC SOLUTION: Cooperative super()
# In Python, `super()` does NOT mean "call my direct parent class".
# `super()` means "call the NEXT class in this object's MRO sequence"!
# By using `super()` cooperatively with `*args, **kwargs`, every class in the
# hierarchy is visited EXACTLY ONCE in topological order!

call_order: List[str] = []

class BaseLogger:
    def __init__(self, **kwargs: Any) -> None:
        call_order.append("BaseLogger")
        super().__init__(**kwargs)


class TimestampMixin(BaseLogger):
    def __init__(self, timezone: str = "UTC", **kwargs: Any) -> None:
        call_order.append("TimestampMixin")
        self.timezone = timezone
        super().__init__(**kwargs)


class JsonFormatterMixin(BaseLogger):
    def __init__(self, indent: int = 2, **kwargs: Any) -> None:
        call_order.append("JsonFormatterMixin")
        self.indent = indent
        super().__init__(**kwargs)


class ProductionAuditLogger(TimestampMixin, JsonFormatterMixin):
    def __init__(self, service_name: str, **kwargs: Any) -> None:
        call_order.append("ProductionAuditLogger")
        self.service_name = service_name
        super().__init__(**kwargs)


logger = ProductionAuditLogger(
    service_name="payment_gateway",
    timezone="America/New_York",
    indent=4
)

# Verify single execution of each layer:
assert call_order == [
    "ProductionAuditLogger",
    "TimestampMixin",
    "JsonFormatterMixin",
    "BaseLogger"
]
assert logger.service_name == "payment_gateway"
assert logger.timezone == "America/New_York"
assert logger.indent == 4
print("--- 2. Diamond Problem & Cooperative super(): PASSED ---")

# =====================================================================
# 3. The C3 Linearization Algorithm (MRO)
# =====================================================================
# Python resolves multiple inheritance using the C3 Linearization algorithm.
# C3 guarantees two fundamental properties:
# 1. Local Precedence Order: If class C inherits (B1, B2), B1 is checked before B2.
# 2. Monotonicity: If B1 precedes B2 in any class's MRO, B1 must precede B2 in all subclasses.
#
# Inspecting MRO:
# Class.__mro__ (tuple) or Class.mro() (list)

mro_names = [cls.__name__ for cls in ProductionAuditLogger.__mro__]
assert mro_names == [
    "ProductionAuditLogger",
    "TimestampMixin",
    "JsonFormatterMixin",
    "BaseLogger",
    "object"
]

# What happens when inheritance orders conflict?
# Python rejects inconsistent class definitions at compile/declaration time!
class X: pass
class Y(X): pass

try:
    # Attempting to declare Z(X, Y) violates monotonicity because Y inherits from X:
    # Y requires Y before X, but Z(X, Y) specifies X before Y!
    type("Z", (X, Y), {})
    raise AssertionError("Should have raised TypeError!")
except TypeError as e:
    print(f"Caught expected C3 MRO conflict TypeError: {e}")
print("--- 3. C3 Linearization & MRO Verification: PASSED ---")

# =====================================================================
# 4. Abstract Base Classes (ABCs) & Contract Enforcement
# =====================================================================
# Abstract Base Classes (from the `abc` standard library module) enforce
# interface contracts at INSTANTIATION time.
#
# Rules:
# - Inherit from `abc.ABC`.
# - Decorate interface methods with `@abstractmethod`.
# - Attempting to instantiate a subclass that forgot to implement ANY
#   abstract method raises an immediate `TypeError`.

class Repository(ABC):
    """Abstract interface for a storage repository."""

    @abstractmethod
    def save(self, entity_id: str, record: Dict[str, Any]) -> None:
        """Persist a record by entity_id."""
        pass

    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a record or None if absent."""
        pass

    @property
    @abstractmethod
    def storage_engine(self) -> str:
        """Abstract property contract."""
        pass


# 1. Attempting to instantiate the abstract class itself fails:
try:
    Repository()  # type: ignore[abstract]
    raise AssertionError("Should have raised TypeError!")
except TypeError as e:
    print(f"Caught expected ABC instantiation TypeError: {e}")

# 2. Incomplete subclass missing methods also fails at instantiation:
class IncompleteRepo(Repository):
    @property
    def storage_engine(self) -> str:
        return "in-memory"
    # Forgot save() and find_by_id()!

try:
    IncompleteRepo()  # type: ignore[abstract]
    raise AssertionError("Should have raised TypeError!")
except TypeError as e:
    print(f"Caught expected incomplete subclass TypeError: {e}")

# 3. Complete concrete subclass:
class InMemoryRepository(Repository):
    def __init__(self) -> None:
        self._store: Dict[str, Dict[str, Any]] = {}

    @property
    def storage_engine(self) -> str:
        return "in-memory-dict"

    def save(self, entity_id: str, record: Dict[str, Any]) -> None:
        self._store[entity_id] = record.copy()

    def find_by_id(self, entity_id: str) -> Optional[Dict[str, Any]]:
        return self._store.get(entity_id)


repo = InMemoryRepository()
assert repo.storage_engine == "in-memory-dict"
repo.save("order_55", {"amount": 250.0, "status": "settled"})
assert repo.find_by_id("order_55") == {"amount": 250.0, "status": "settled"}
assert repo.find_by_id("missing") is None
print("--- 4. Abstract Base Classes (ABCs) & Enforcement: PASSED ---")

# =====================================================================
# 5. Clean Architecture: Composition Over Inheritance
# =====================================================================
# Gang of Four (GoF) Principle: "Favor object composition over class inheritance."
#
# The Inheritance Trap (Rigid Is-A hierarchy):
# class SQLUserNotifierAdminService(BaseUser, SQLDatabase, TwilioClient, EmailClient): ...
# Leads to tight coupling, fragile base class bugs, and combinatorial explosion.
#
# The Clean Architecture Solution (Flexible Has-A composition):
# Compose small, decoupled components via dependency injection.

class MessageSender(Protocol):
    """Structural interface using typing.Protocol (Duck-typing contract)."""
    def send(self, recipient: str, message: str) -> bool:
        ...


class EmailService:
    def send(self, recipient: str, message: str) -> bool:
        # Real implementation would dispatch SMTP
        return True


class MockSMSService:
    def __init__(self) -> None:
        self.dispatched: List[tuple[str, str]] = []

    def send(self, recipient: str, message: str) -> bool:
        self.dispatched.append((recipient, message))
        return True


class OrderProcessor:
    """High-level domain service depending on abstractions, not concretions."""

    def __init__(self, notifier: MessageSender, repository: Repository) -> None:
        # Injected dependencies:
        self._notifier: MessageSender = notifier
        self._repo: Repository = repository

    def checkout(self, order_id: str, customer_contact: str, total: float) -> bool:
        # Business logic:
        record = {"order_id": order_id, "total": total, "status": "paid"}
        self._repo.save(order_id, record)
        return self._notifier.send(customer_contact, f"Order {order_id} confirmed for ${total:.2f}")


# Composing the system at runtime:
sms_mock = MockSMSService()
order_repo = InMemoryRepository()
processor = OrderProcessor(notifier=sms_mock, repository=order_repo)

success = processor.checkout("ORD_999", "+15551234567", 89.99)
assert success is True
assert len(sms_mock.dispatched) == 1
assert sms_mock.dispatched[0] == ("+15551234567", "Order ORD_999 confirmed for $89.99")
assert order_repo.find_by_id("ORD_999") == {"order_id": "ORD_999", "total": 89.99, "status": "paid"}
print("--- 5. Clean Architecture (Composition over Inheritance): PASSED ---")

print("\n=======================================================")
print("ALL LESSON 03 ASSERTIONS PASSED! INHERITANCE & MRO MASTERED.")
print("=======================================================")
