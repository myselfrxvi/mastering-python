# Module 01: Python Basics & Core Foundations

Welcome to the beginning of your Python engineering journey. Python is an expressive, dynamically-typed, high-level language designed for readability and developer velocity.

---

## 1. How Python Executes Code

Unlike C++ or Rust which compile directly to machine binaries, Python is executed via the **CPython Virtual Machine (VM)**:

```text
  Source Code (.py)
         │
         ▼
     [ Compiler ]
         │
         ▼
   Bytecode (.pyc)      (Platform-independent instructions)
         │
         ▼
    [ Python VM ]       (Reads bytecode instruction by instruction)
         │
         ▼
   Machine Execution
```

---

## 2. The Golden Mental Model: Variables are Name Tags, Not Boxes!

In C++ or Java, a variable is a physical memory box of a fixed size.
In Python: **Variables are name tags attached to objects on the heap.**

```text
C++ (Box Model):
[ int x = 42 ]   <-- 42 lives inside box named x

Python (Name Tag Model):
     "x" (name tag) ───► [ Integer Object: 42 ]
```

When you do:
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Output: [1, 2, 3, 4]! Both name tags point to the EXACT same list!
```

---

## 3. Module Roadmap

Run each script sequentially with `python <filename>`:

1. **`01_variables_and_types.py`**: Primitive types (`int`, `float`, `str`, `bool`, `None`), dynamic typing, type inspection, and conversion.
2. **`02_operators_and_math.py`**: Arithmetic, integer division `//`, modulus `%`, power `**`, bitwise operators, and floating-point precision caveats.
3. **`03_conditionals.py`**: `if` / `elif` / `else`, truthy vs falsy values, short-circuit logic, and one-liner ternary operators.
4. **`04_loops_and_ranges.py`**: `while` loops, `for` loops, `range(start, stop, step)`, `enumerate()`, `break`, `continue`, and the rare `for...else` construct.

Every file contains runnable explanations followed by interactive challenges with self-verifying test assertions.
