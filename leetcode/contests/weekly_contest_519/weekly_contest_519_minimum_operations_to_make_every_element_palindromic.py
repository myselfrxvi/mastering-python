from bisect import bisect_left
from typing import List

odds = []
even = []

for length in range(1, 10):
    half = (length + 1) // 2
    start = 10 ** (half - 1)
    end = 10 ** half
    for h in range(start, end):
        s = str(h)
        if length % 2 == 0:
            p = int(s + s[::-1])
        else:
            p = int(s + s[-2::-1])
        if p % 2 == 0:
            even.append(p)
        else:
            odds.append(p)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_operations = 0
        for x in nums:
            target_list = even if x % 2 == 0 else odds
            idx = bisect_left(target_list, x)
            if idx == 0:
                diff = abs(x - target_list[0])
            elif idx == len(target_list):
                diff = abs(x - target_list[-1])
            else:
                diff = min(abs(x - target_list[idx]), abs(x - target_list[idx - 1]))
            total_operations += diff // 2
        return total_operations