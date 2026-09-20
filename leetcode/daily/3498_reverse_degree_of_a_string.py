class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            rank = 26 - (ord(char) - ord('a'))
            total += rank * (i + 1)
        return total
