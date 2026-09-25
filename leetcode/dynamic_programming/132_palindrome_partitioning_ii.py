class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i - 1 for i in range(n + 1)]
        for mid in range(n):
            l, r = mid, mid
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
                
            l, r = mid, mid + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    assert sol.minCut("aab") == 1
    assert sol.minCut("a") == 0
    assert sol.minCut("ab") == 1
    assert sol.minCut("aba") == 0
    assert sol.minCut("abcd") == 3
    assert sol.minCut("aaaa") == 0
    print("ALL TESTS PASSED! Ready for submission.")
