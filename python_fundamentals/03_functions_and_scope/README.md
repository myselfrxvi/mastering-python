# Module 03: Functions, Scope & Functional Idioms

Master the execution model of Python functions, CPython call stack mechanics, the LEGB lexical scoping hierarchy, closure state encapsulation, and functional sorting idioms.

---

## 1. The Call Frame & Lexical Scope Architecture

In Python, functions are **first-class objects** (`PyFunctionObject`). When a function is called, CPython allocates a **Call Frame** (`PyFrameObject`) on the C call stack:

```text
Global Scope (__main__)
  ├── Built-ins (len, range, print, ...)
  └── Global Variables (module-level symbols)
        ▲
        │  Enclosing Scope (Outer Function)
        │    └── Cell Objects (Free variables captured by closures)
        │          ▲
        │          │  Local Scope (Inner Function)
        │          │    └── Fast Local Array (co_varnames indexed directly by C pointer)
```

### The LEGB Resolution Order
Whenever Python resolves a variable name, it checks in strict sequence:
1. **L (Local):** Names defined inside the currently executing function (stored in `co_varnames`).
2. **E (Enclosing):** Names in enclosing functions from inner to outer (closures via `cell` variables).
3. **G (Global):** Names declared at module level or via the `global` keyword.
4. **B (Built-in):** Built-in names pre-loaded into `builtins` (e.g. `len`, `int`, `ValueError`).

If not found after checking all 4: raises `NameError`.

---

## 2. Parameter Binding Protocol (`/` and `*`)

Python allows total control over how callers provide arguments:

```text
def func(pos_only_1, pos_only_2, /, standard_param, *, kw_only_1, kw_only_2):
         └────────┬────────────┘     └──────┬───────┘   └────────┬──────────┘
                  │                         │                    │
          Positional-Only             Positional or        Keyword-Only
     (Cannot pass by name)               Keyword         (MUST pass by name)
```

- **`/` (Slash):** Enforces that preceding parameters **must** be positional. Useful for API backward compatibility and high-performance C bindings.
- **`*` (Asterisk):** Enforces that subsequent parameters **must** be keyword-only. Prevents ambiguous boolean flags like `set_status(True, False, True)`.

---

## 3. Curriculum & Lab Files

Run each interactive lab script with `python <filename>`:

1. **[01_function_signatures.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/03_functions_and_scope/01_function_signatures.py)**: Positional-only (`/`), keyword-only (`*`), type annotations, and the classic **Mutable Default Parameter Trap** (`target=[]` vs `target=None`).
2. **[02_args_and_kwargs.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/03_functions_and_scope/02_args_and_kwargs.py)**: Dynamic argument packing (`*args` as tuple, `**kwargs` as dict), transparent forwarding, and dictionary merging.
3. **[03_scope_and_closures.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/03_functions_and_scope/03_scope_and_closures.py)**: The LEGB rule in practice, `global` vs `nonlocal`, closure cell objects (`__closure__`), and the famous **Late-Binding Loop Trap**.
4. **[04_lambdas_and_sorting.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/03_functions_and_scope/04_lambdas_and_sorting.py)**: Anonymous lambda functions, multi-key sorting tuples, `operator.itemgetter`, and functional pipelines (`map`, `filter`, `reduce`).
