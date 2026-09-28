import sys

def max_card_money(n: int, k: int) -> int:
    return (1 << (n - k + 1)) + 2 * (k - 1)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        out.append(str(max_card_money(n, k)))
    print("\n".join(out))

solve()
