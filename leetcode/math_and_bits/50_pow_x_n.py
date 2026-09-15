class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        res = x**n
        return res
