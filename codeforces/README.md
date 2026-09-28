# Codeforces Arena & Competitive Programming Hub

A high-performance arena for **Codeforces rounds, Div 2/3/4 battles, and Educational contests**, organized with zero-boilerplate Python & C++ templates.

---

## ⚡ Fast I/O Templates

### Python 3 Fast I/O Template
```python
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    # Read tokens linearly:
    # t = int(data[0])
    ...

if __name__ == "__main__":
    solve()
```

### C++ Fast I/O Template
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    // Write test case logic here
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 1;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```

---

## 🏆 Contests & Rounds Archive

### [Codeforces Round 1124 (Div. 2)](round_1124_div2)
- **Problem A:** [a_sausage_bank.py](round_1124_div2/a_sausage_bank.py) — O(1) Convexity of powers of 2 & interval partition maximization.

### [Codeforces Beta Round 6 (Div. 2)](beta_round_06)
- **Problem C:** [c_alice_bob_and_chocolate.py](beta_round_06/c_alice_bob_and_chocolate.py) — O(N) Two-pointer elapsed-time greedy simulation.

