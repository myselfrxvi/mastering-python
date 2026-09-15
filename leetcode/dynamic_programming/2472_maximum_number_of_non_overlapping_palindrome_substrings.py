class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start = 0

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(k - 1, n):
            if i - k + 1 >= start and is_palindrome(i - k + 1, i):
                ans += 1
                start = i + 1
            elif i - k >= start and is_palindrome(i - k, i):
                ans += 1
                start = i + 1

        return ans
