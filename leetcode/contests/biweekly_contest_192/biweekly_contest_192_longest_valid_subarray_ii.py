from typing import List
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        first_P = {}
        last_P = {}
        curr = 0
        first_P[0] = 0
        last_P[0] = 0
        pos = defaultdict(list)
        
        for m, x in enumerate(nums):
            curr = (curr + x) % k
            if curr not in first_P:
                first_P[curr] = m + 1
            last_P[curr] = m + 1
            
            d = (2 * x) % k
            pos[d].append(m)
            
        ans = 0

        # Case 1: No negation needed
        for r in first_P:
            ans = max(ans, last_P[r] - first_P[r])
            
        # Case 2: One element negated
        for D, indices in pos.items():
            min_m = indices[0]
            max_m = indices[-1]
            
            for r_j, j in first_P.items():
                r_i = (r_j + D) % k
                if r_i not in last_P:
                    continue
                
                i = last_P[r_i]
                if i - j <= ans:
                    continue
                
                # Fast range verification: boundary checks followed by binary search
                if j <= min_m < i or j <= max_m < i:
                    ans = i - j
                else:
                    idx = bisect_left(indices, j)
                    if idx < len(indices) and indices[idx] < i:
                        ans = i - j
                        
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestSubarray([4, 1, 2], 3) == 3
    assert sol.longestSubarray([5, 3, 4], 7) == 2
    assert sol.longestSubarray([2, 2, 5], 6) == 2
    print("ALL TESTS PASSED! Biweekly Contest 192 Q4 verified.")
