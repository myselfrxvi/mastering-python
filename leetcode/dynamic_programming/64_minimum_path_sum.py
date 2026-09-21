from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0] * n
        row[0] = grid[0][0]
        for c in range(1, n):
            row[c] = row[c - 1] + grid[0][c]
        for r in range(1, m):
            row[0] += grid[r][0]
            for c in range(1, n):
                row[c] = min(row[c], row[c - 1]) + grid[r][c]
        return row[-1]
