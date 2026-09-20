from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # --- YOUR TURN: Implement in-place or 1D DP for Minimum Path Sum ---
        # HINT 1: m = len(grid), n = len(grid[0]).
        # HINT 2: Initialize row = [0] * n.
        #         Set row[0] = grid[0][0].
        #         For first row (c from 1 to n - 1): row[c] = row[c - 1] + grid[0][c].
        # HINT 3: For each row r from 1 to m - 1:
        #         First column: row[0] += grid[r][0] (can only come from top!).
        #         Remaining columns (c from 1 to n - 1): row[c] = min(row[c], row[c - 1]) + grid[r][c].
        # HINT 4: Return row[-1].
        pass
