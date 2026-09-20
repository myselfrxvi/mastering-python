from typing import List

class Solution:
    def countIntersections(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = 0
        for i in range(n):
            a, b = intervals[i]
            for j in range(i + 1, n):
                c, d = intervals[j]
                if max(a, c) <= min(b, d):
                    count += 1
        return count
