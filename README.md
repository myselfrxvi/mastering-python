# Systems & Algorithmic Engineering Lab

A repository dedicated to end-to-end Python engineering mastery, algorithmic problem-solving on **The Grand Quest (75 / 4,055 Solved — 18 Hards, 42 Mediums, 15 Easies | 15-Day Streak | Global Rank: ~2.5M)**, and PyTorch generative transformer architectures.

---

## Repository Structure

```text
.
├── leetcode/                      # Categorized LeetCode Solutions (The Grand Quest)
│   ├── arrays/                    # In-place two pointers, prefix sums, sliding window
│   ├── strings/                   # String matching, palindromes, conversions
│   ├── linked_lists/              # Pointer rewiring, fast & slow pointers, dummy nodes
│   ├── stack/                     # Monotonic stacks, parenthesis validation
│   ├── binary_search/             # Rotated arrays, median of sorted arrays, O(log N)
│   ├── backtracking/              # State-space trees, permutations, combinations
│   ├── dynamic_programming/       # Distinct subsequences, regex matching, memoization
│   ├── math_and_bits/             # Bit manipulation (<<), exponential division, math
│   ├── daily/                     # Live daily challenges & contest drills
│   ├── DSA_40_PATTERN_MASTER_SHEET.md # 40-pattern priority master tracking index
│   ├── BIG_O_COMPLEXITY_ROADMAP.md# 7-module guide to mastering time & space complexity
│   ├── CONTEST_PLAYBOOK.md        # Fast pattern recognition & constraint decoder
│   └── 6_DAY_CONTEST_PREP_GOAL.md # Sprint schedule for Weekly Contest 519
│
└── python_fundamentals/           # Modern Python Engineering & AI Engine
    ├── ai_engine/                 # PyTorch causal transformer block from scratch, multi-head attention
    └── fintech/                   # Financial time-series PyTorch model, tools & RAG engine
```

---

## LeetCode: The Grand Quest (Goal: 4,047 Problems)

A structured pursuit of conquering every single algorithmic challenge on LeetCode, emphasizing optimal time complexity, minimal auxiliary space, and clean code.

### Highlights by Topic:
- **Hard Tier:**
  - `leetcode/strings/30_substring_with_concatenation_of_all_words.py` (O(N) sliding window with offset alignment)
  - `leetcode/stack/32_longest_valid_parentheses.py` (O(N) single-pass stack index fence technique)
  - `leetcode/linked_lists/25_reverse_nodes_in_k_group.py` (O(1) in-place group pointer reversal)
  - `leetcode/dynamic_programming/115_distinct_subsequences.py` & `940_distinct_subsequences_ii.py` (O(N) duplicate subtraction with modulo arithmetic)
  - `leetcode/binary_search/04_median_of_two_sorted_arrays.py` (O(log(min(M, N))) binary partition search)
- **Medium & In-Place Two Pointers:**
  - `leetcode/arrays/31_next_permutation.py` (Lexicographical dip-and-swap with suffix reversal)
  - `leetcode/binary_search/33_search_in_rotated_sorted_array.py` (O(log N) decision tree)
  - `leetcode/math_and_bits/29_divide_two_integers.py` (Bit-shift exponential doubling with 32-bit overflow guard)

---

## AI & Deep Learning Core (`python_fundamentals/ai_engine`)

- **Custom Transformer Architecture:** Built from scratch in PyTorch implementing multi-head self-attention, causal masking, layer normalization, and feed-forward blocks.
- **Streaming & Memory:** Token streaming pipelines, sliding window chat history, and structured Pydantic outputs.

