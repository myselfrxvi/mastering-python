from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        if not ones1 or not ones2:
            return 0

        # --- YOUR TURN: Vector Voting ---
        # For every pair (r1, c1) in ones1 and (r2, c2) in ones2:
        # What shift vector (dr, dc) aligns (r1, c1) onto (r2, c2)?
        # Count the votes for each vector and return the maximum overlap!
        pass
