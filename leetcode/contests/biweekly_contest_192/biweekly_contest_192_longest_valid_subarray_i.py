from typing import List
from collections import Counter

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for l in range(n, 0, -1):
            s = sum(nums[:l])
            counts = Counter((2 * x) % k for x in nums[:l])
            
            if s % k == 0 or (s % k) in counts:
                return l
            
            for i in range(l, n):
                s += nums[i] - nums[i - l]
                out_val = (2 * nums[i - l]) % k
                counts[out_val] -= 1
                if counts[out_val] == 0:
                    del counts[out_val]

                in_val = (2 * nums[i]) % k
                counts[in_val] += 1
                
                if s % k == 0 or (s % k) in counts:
                    return l
                    
        return 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestSubarray([4, 1, 2], 3) == 3
    assert sol.longestSubarray([5, 3, 4], 7) == 2
    assert sol.longestSubarray([2, 2, 5], 6) == 2
    print("ALL TESTS PASSED! Biweekly Contest 192 Q3 verified.")
