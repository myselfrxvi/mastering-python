from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for ch in first:
            left = first[ch]
            right = last[ch]
            valid = True
            i = left
            while i <= right:
                c = s[i]
                if first[c] < left:
                    valid = False
                    break
                right = max(right, last[c])
                i += 1
            if valid:
                intervals.append((right, left))

        intervals.sort()
        res = []
        prev_end = -1
        for right, left in intervals:
            if left > prev_end:
                res.append(s[left:right + 1])
                prev_end = right

        return res
