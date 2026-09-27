"""
Module 03: Functions, Scope & Functional Idioms
Lesson 02: Variadic Parameters (*args and **kwargs) and Universal Forwarding

Run this file with:
    python 02_args_and_kwargs.py
"""

from typing import Any, Dict, Tuple

# =====================================================================
# 1. Positional Packing: *args
# =====================================================================
# The asterisk `*` tells Python to pack all excess positional arguments
# into a single immutable tuple named `args`.

def sum_all(*numbers: float) -> float:
    # `numbers` is a tuple!
    assert isinstance(numbers, tuple)
    total = 0.0
    for num in numbers:
        total += num
    return total

assert sum_all() == 0.0
assert sum_all(1, 2, 3) == 6.0
assert sum_all(10.5, 20.5, 30.0, 40.0) == 101.0
print("--- 1. Positional Packing (*args): PASSED ---")

# =====================================================================
# 2. Keyword Packing: **kwargs
# =====================================================================
# The double asterisk `**` tells Python to pack all excess keyword arguments
# into a standard dictionary named `kwargs`.

def build_http_headers(**headers: str) -> Dict[str, str]:
    # `headers` is a dictionary!
    assert isinstance(headers, dict)
    return {k.lower(): v for k, v in headers.items()}

h = build_http_headers(
    Authorization="Bearer token_123",
    Content_Type="application/json",
    Accept="*/*"
)
assert h["authorization"] == "Bearer token_123"
assert h["content_type"] == "application/json"
assert len(h) == 3
print("--- 2. Keyword Packing (**kwargs): PASSED ---")

# =====================================================================
# 3. Parameter Ordering Rule
# =====================================================================
# Standard Python parameter ordering must strictly follow:
# 1. Standard positional parameters
# 2. *args
# 3. Keyword-only parameters (with or without defaults)
# 4. **kwargs

def complex_pipeline(
    stage_name: str,
    *input_data: int,
    retry_count: int = 3,
    **metadata: Any
) -> Tuple[str, Tuple[int, ...], int, Dict[str, Any]]:
    return stage_name, input_data, retry_count, metadata

res = complex_pipeline(
    "ingestion",
    10, 20, 30,          # Packed into *input_data
    retry_count=5,       # Keyword-only
    environment="prod",  # Packed into **metadata
    cluster_id="us-east-1"
)

assert res[0] == "ingestion"
assert res[1] == (10, 20, 30)
assert res[2] == 5
assert res[3] == {"environment": "prod", "cluster_id": "us-east-1"}
print("--- 3. Strict Parameter Ordering: PASSED ---")

# =====================================================================
# 4. Unpacking Arguments at Call Time (* and **)
# =====================================================================
# At the call site, `*` and `**` perform the INVERSE operation:
# they UNPACK an iterable into positional arguments,
# or a dictionary into keyword arguments!

def create_point(x: float, y: float, z: float) -> str:
    return f"Point({x}, {y}, {z})"

coords_list = [1.5, 2.5, 3.5]
coords_dict = {"x": 10.0, "y": 20.0, "z": 30.0}

# Unpacking list into 3 separate positional arguments:
assert create_point(*coords_list) == "Point(1.5, 2.5, 3.5)"

# Unpacking dictionary into 3 separate keyword arguments:
assert create_point(**coords_dict) == "Point(10.0, 20.0, 30.0)"
print("--- 4. Call-Site Argument Unpacking: PASSED ---")

# =====================================================================
# 5. Universal Transparent Forwarding (The Decorator Pattern Foundation)
# =====================================================================
# Any wrapper function can accept (*args, **kwargs) and forward them
# cleanly to an underlying target function without knowing its signature:

def target_worker(task_id: int, payload: str, *, priority: int = 1) -> str:
    return f"Processed task {task_id} with payload '{payload}' at priority {priority}"

call_log = []

def logging_proxy(fn, *args, **kwargs):
    call_log.append(f"Calling {fn.__name__} with args={args}, kwargs={kwargs}")
    # Forward untouched!
    result = fn(*args, **kwargs)
    call_log.append(f"Returned from {fn.__name__}")
    return result

output = logging_proxy(target_worker, 42, "DATA_CHUNK", priority=10)

assert "Processed task 42" in output
assert len(call_log) == 2
assert "'priority': 10" in call_log[0]
print("--- 5. Transparent Forwarding: PASSED ---")

print("\n=======================================================")
print("ALL LESSON 02 ASSERTIONS PASSED! VARIADIC ARGS MASTERED.")
print("=======================================================")
