from typing import List
import bisect

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        tem = intervals
        n = len(intervals)
        start = sorted(iv[0] for iv in intervals)
        non_intersect = 0
        for iv in intervals:
            end = iv[1]
            idx = bisect.bisect_right(start, end)
            non_intersect += (n - idx)
        total_pair = n * (n-1) //2
        return total_pair - non_intersect