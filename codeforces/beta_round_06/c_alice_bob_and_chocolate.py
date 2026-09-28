import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    t = [int(x) for x in input_data[1:n + 1]]
    
    l, r = 0, n - 1
    time_a = 0
    time_b = 0
    bars_a = 0
    bars_b = 0
    
    while l <= r:
        if time_a <= time_b:
            time_a += t[l]
            bars_a += 1
            l += 1
        else:
            time_b += t[r]
            bars_b += 1
            r -= 1
            
    print(f"{bars_a} {bars_b}")

solve()


