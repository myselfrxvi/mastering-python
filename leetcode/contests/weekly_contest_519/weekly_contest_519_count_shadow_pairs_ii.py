from bisect import bisect_left, bisect_right
from typing import List

class SuffixMinBIT:
    __slots__ = ('tree',)
    def __init__(self, size):
        self.tree = [float('inf')] * (size + 2)
    def update(self, i, val):
        i += 1
        while i > 0:
            if val < self.tree[i]:
                self.tree[i] = val
            i -= i & (-i)
    def query(self, i):
        i += 1
        res = float('inf')
        n = len(self.tree)
        while i < n:
            if self.tree[i] < res:
                res = self.tree[i]
            i += i & (-i)
        return res

class PrefixMaxBIT:
    __slots__ = ('tree',)
    def __init__(self, size):
        self.tree = [-float('inf')] * (size + 2)
    def update(self, i, val):
        i += 1
        n = len(self.tree)
        while i < n:
            if val > self.tree[i]:
                self.tree[i] = val
            i += i & (-i)
    def query(self, i):
        i += 1
        res = -float('inf')
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & (-i)
        return res

class Fenwick:
    __slots__ = ('tree',)
    def __init__(self, size):
        self.tree = [0] * (size + 2)
    def add(self, i, delta):
        i += 1
        n = len(self.tree)
        while i < n:
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        if i <= 0:
            return 0
        n = len(self.tree)
        if i >= n:
            i = n - 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def shadowPairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        def brute_range(L, R):
            count = 0
            for j in range(L + 1, R + 1):
                running_max = -float('inf')
                vj = nums[j]
                for i in range(j - 1, L - 1, -1):
                    vi = nums[i]
                    if vi < vj:
                        if vi >= running_max:
                            count += 1
                            running_max = vi
            return count

        def dc(L, R):
            if R - L <= 128:
                return brute_range(L, R)

            mid = (L + R) // 2
            ans = dc(L, mid) + dc(mid + 1, R)

            left_vals = sorted(list(set(nums[L:mid+1])))
            s_min = SuffixMinBIT(len(left_vals))
            left_pts = []
            for i in range(mid, L - 1, -1):
                v = nums[i]
                idx = bisect_right(left_vals, v)
                U = s_min.query(idx) if idx < len(left_vals) else float('inf')
                left_pts.append((v, U))
                s_min.update(bisect_left(left_vals, v), v)

            right_vals = sorted(list(set(nums[mid+1:R+1])))
            p_max = PrefixMaxBIT(len(right_vals))
            right_pts = []
            for j in range(mid + 1, R + 1):
                v = nums[j]
                idx = bisect_left(right_vals, v) - 1
                L_val = p_max.query(idx) if idx >= 0 else -float('inf')
                right_pts.append((L_val, v))
                p_max.update(bisect_left(right_vals, v), v)

            all_x = sorted(list(set([p[0] for p in left_pts] + [q[0] for q in right_pts] + [q[1] for q in right_pts])))
            events = []
            for A, U in left_pts:
                events.append((U, 1, A))
            for L_val, B in right_pts:
                events.append((B, 0, L_val))
            events.sort(key=lambda e: (e[0], e[1]), reverse=True)

            bit = Fenwick(len(all_x))
            for y, kind, val in events:
                if kind == 1:
                    bit.add(bisect_left(all_x, val), 1)
                else:
                    idx_l = bisect_left(all_x, val)
                    idx_r = bisect_right(all_x, y - 1) - 1
                    if idx_l <= idx_r:
                        ans += bit.query(idx_r) - bit.query(idx_l - 1)
            return ans

        return dc(0, n - 1)
