from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = []

        def backtrack(row: int) -> None:
            if row == n:
                solution = ["." * c + "Q" + "." * (n - 1 - c) for c in board]
                res.append(solution)
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board.append(col)
                backtrack(row + 1)
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board.pop()

        backtrack(0)
        return res
