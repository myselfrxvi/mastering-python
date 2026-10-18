# Module 04: Object-Oriented Programming (OOP) & Clean Architecture

Master the CPython object model, instance instantiation lifecycle, dunder protocol operator overloading, multiple inheritance resolution (C3 Linearization / MRO), encapsulation via descriptors and properties, and Clean Architecture domain modeling.

---

## 1. CPython Object Architecture & Memory Layout

In Python, **everything is an object**—including functions, modules, and classes themselves. At the CPython C-layer, every object is represented by a `PyObject` header:

```text
               PyObject Header
    ┌───────────────────────────────────┐
    │  ob_refcnt  (Reference counter)   │
    ├───────────────────────────────────┤
    │  ob_type    (Pointer to type)     │ ───► PyTypeObject (e.g. BankAccount)
    └───────────────────────────────────┘
                      │
           ┌──────────┴──────────┐
           ▼                     ▼
   Regular Instance       Slotted Instance (__slots__)
  ┌─────────────────┐    ┌─────────────────────────┐
  │  __dict__ ptr   │    │  ptr_0: attribute "x"   │
  │  (Dynamic Dict) │    │  ptr_1: attribute "y"   │
  │  ~150-300 bytes │    │  Fixed C Array: 56 B    │
  └─────────────────┘    └─────────────────────────┘
```

- **`__dict__`**: Default storage for instance attributes. Offers full dynamic flexibility, but incurs hash table memory overhead (~150–300 bytes per instance).
- **`__slots__`**: Suppresses `__dict__` creation. Allocates a fixed C-array of descriptor pointers, slashing memory consumption by up to **60%** while speeding up attribute access.

---

## 2. The Python Attribute Lookup Pipeline

When an attribute is accessed via `obj.attr`, CPython executes the following deterministic resolution sequence:

```text
                          obj.attr accessed
                                 │
                                 ▼
         ┌───────────────────────────────────────────────┐
         │ 1. Is 'attr' a DATA DESCRIPTOR on the class?  │
         │    (Implements __set__ or __delete__)         │
         └───────────────────────┬───────────────────────┘
                     YES ┌───────┴───────┐ NO
                         ▼               ▼
                 Invoke __get__()  ┌──────────────────────────────────┐
                                   │ 2. Is 'attr' in obj.__dict__?    │
                                   └─────────────┬────────────────────┘
                                     YES ┌───────┴───────┐ NO
                                         ▼               ▼
                                    Return value  ┌────────────────────────────────────────┐
                                                  │ 3. Is 'attr' a NON-DATA DESCRIPTOR or   │
                                                  │    standard method on class/bases MRO? │
                                                  └──────────────┬─────────────────────────┘
                                                     YES ┌───────┴───────┐ NO
                                                         ▼               ▼
                                                 Invoke __get__()  ┌──────────────────────────────┐
                                                                   │ 4. Is 'attr' a CLASS VALUE   │
                                                                   │    in class or bases dict?   │
                                                                   └──────────────┬───────────────┘
                                                                      YES ┌───────┴───────┐ NO
                                                                          ▼               ▼
                                                                     Return val     Invoke __getattr__
                                                                                    or raise AttributeError
```

---

## 3. The Diamond Problem & C3 Linearization (MRO)

Python handles multiple inheritance using the **C3 Linearization Algorithm**, guaranteeing monotonicity and local precedence order:

```text
                  Base (A)
                 /        \
             Left (B)    Right (C)
                 \        /
                  Child (D)

MRO Sequence: D ──► B ──► C ──► A ──► object
```

- **Cooperative `super()`**: When each class in the hierarchy invokes `super().__init__(**kwargs)`, Python traverses the linear MRO sequence without executing any ancestor constructor twice.

---

## 4. Clean Architecture & SOLID Principles

1. **Single Responsibility (SRP)**: Classes encapsulate a single domain boundary (e.g. `OrderAggregate` manages order items and transitions, while `MessageSender` handles dispatch).
2. **Open-Closed Principle (OCP)**: Interfaces and Abstract Base Classes (`abc.ABC`) allow extending behavior without modifying existing classes.
3. **Liskov Substitution (LSP)**: Derived classes must honor supertype contracts and protocol signatures.
4. **Interface Segregation (ISP)**: Lightweight `typing.Protocol` interfaces define precise duck-typing boundaries.
5. **Dependency Inversion (DIP)**: High-level orchestration services depend on abstract protocols, not concrete database or network clients.
6. **Composition over Inheritance**: Prefer building systems by composing small, focused objects rather than deep, fragile inheritance trees.

---

## 5. Curriculum & Lab Files

Run each interactive lab script with `python <filename>`:

1. **[01_classes_and_instances.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/04_oop_and_clean_architecture/01_classes_and_instances.py)**: Classes, instances, the `self` binding protocol, `__new__` allocator vs `__init__` initializer, class attributes vs instance attributes, the shadowing trap, method types (`@classmethod`, `@staticmethod`), and high-performance `__slots__` optimization.
2. **[02_dunder_methods.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/04_oop_and_clean_architecture/02_dunder_methods.py)**: The Python Data Model, `__repr__` vs `__str__`, equality & hash invariants (`__eq__` and `__hash__`), rich comparisons with `@total_ordering`, the container/sequence protocol (`__len__`, `__getitem__`, `__contains__`), arithmetic operator overloading (`__add__`, `__rmul__`), callable instances (`__call__`), and truthiness (`__bool__`).
3. **[03_inheritance_and_mro.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/04_oop_and_clean_architecture/03_inheritance_and_mro.py)**: Single inheritance, initializer chaining with `super()`, multiple inheritance, solving the Diamond Problem with cooperative `super()`, the C3 Linearization algorithm (`__mro__`), contract enforcement with Abstract Base Classes (`abc.ABC`, `@abstractmethod`), and Clean Architecture composition over inheritance.
4. **[04_encapsulation_properties.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/04_oop_and_clean_architecture/04_encapsulation_properties.py)**: Access conventions (`_protected`, `__mangled`), the Uniform Access Principle, `@property` getters, setters, and deleters, high-performance lazy `@cached_property`, the Descriptor Protocol (`__get__`, `__set__`), and a production-grade Clean Architecture finite state machine domain aggregate (`OrderAggregate`).
