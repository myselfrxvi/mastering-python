class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
        numbers = list(range(1, n+1))
        res = []
        k -= 1
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k %= factorials[i]
            res.append(str(numbers.pop(idx)))
        return "".join(res)