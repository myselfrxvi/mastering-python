# Module 02: Data Structures & Pythonic Idioms

Master the core built-in data structures of Python, their underlying CPython memory layouts, algorithmic Big-O complexities, and idiomatic expressive patterns.

---

## 1. Big-O Complexity Master Reference

| Data Structure | Access by Index | Search by Value (`x in s`) | Insert / Append | Delete | Hashable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** (`list`) | `O(1)` | `O(N)` | `O(1)` amortized append / `O(N)` insert | `O(1)` pop / `O(N)` delete | ❌ No (Mutable) |
| **Tuple** (`tuple`) | `O(1)` | `O(N)` | N/A (Immutable) | N/A (Immutable) | ✅ Yes (If items hashable) |
| **Dict** (`dict`) | `O(1)` by key | `O(1)` average by key | `O(1)` average | `O(1)` average | ❌ No (Mutable) |
| **Set** (`set`) | N/A (Unordered) | `O(1)` average | `O(1)` average | `O(1)` average | ❌ No (Mutable) |
| **FrozenSet** (`frozenset`) | N/A (Unordered) | `O(1)` average | N/A (Immutable) | N/A (Immutable) | ✅ Yes |

---

## 2. Memory Architecture & Mental Models

### Dynamic Array (`PyListObject`)
Lists store contiguous arrays of pointers to heap objects. CPython over-allocates memory so `.append()` runs in amortized `O(1)` time:
```text
List Header (Length, Allocated Capacity)
  └── [ ptr_0 | ptr_1 | ptr_2 | ptr_3 | (unused slots...) ]
          │       │       │       │
          ▼       ▼       ▼       ▼
        [10]    [20]    [30]    [40]
```

### Compact Hash Table (`PyDictObject` since Python 3.7)
Maintains strict insertion order by decoupling indices from entries:
```text
Indices Array:  [ -1 | 0 | -1 | 1 | ... ]   (Sparse array based on hash % size)
Entries Array:  [ ("key1", val1), ("key2", val2) ] (Dense contiguous array in arrival order)
```

---

## 3. Curriculum & Lab Files

Run each interactive lab script with `python <filename>`:

1. **[01_lists_and_mutability.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/01_lists_and_mutability.py)**: Dynamic arrays, in-place vs new-list operations, aliasing vs shallow copying vs deep copying.
2. **[02_slicing_mastery.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/02_slicing_mastery.py)**: The `[start:stop:step]` stride protocol, reversal, surgical in-place slice assignments, and `slice()` objects.
3. **[03_tuples_and_unpacking.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/03_tuples_and_unpacking.py)**: Fixed-size immutability, memory savings, tuple hashability rules, structural unpacking (`*rest`), and `namedtuple`.
4. **[04_dictionaries.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/04_dictionaries.py)**: Hash tables, `.get()`, `.setdefault()`, dynamic views (`keys & other_keys`), `defaultdict`, and `Counter`.
5. **[05_sets.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/05_sets.py)**: Hash sets, Venn diagram algebra (`|`, `&`, `-`, `^`), disjointness, `.discard()` vs `.remove()`, and `frozenset`.
6. **[06_comprehensions.py](file:///c:/Users/ravin/OneDrive/Desktop/python/python_fundamentals/02_data_structures/06_comprehensions.py)**: Bytecode-optimized comprehensions, list/dict/set variants, generator expressions, and 2D matrix flattening/transposing.
