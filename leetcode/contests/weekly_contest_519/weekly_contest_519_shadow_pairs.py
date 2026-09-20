from bisect import bisect_left
from collections import defaultdict
from typing import List

class Solution:
    def shadowPairs(self, nums: List[int]) -> int:
        n = len(nums)
        R = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                R[stack.pop()] = i
            stack.append(i)

        pos = defaultdict(list)
        for idx, x in enumerate(nums):
            pos[x].append(idx)

        total_pairs = 0
        for i in range(n):
            total_in_range = R[i] - i - 1
            plist = pos[nums[i]]
            left = bisect_left(plist, i + 1)
            right = bisect_left(plist, R[i])
            count_equal = right - left
            total_pairs += total_in_range - count_equal

        return total_pairs
