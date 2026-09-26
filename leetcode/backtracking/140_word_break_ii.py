from typing import List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        max_len = max(len(w) for w in words)
        n = len(s)
        @cache
        def dfs(start):
            if start == n:
                return [""]
            res = []
            for end in range(start + 1, min(n + 1, start + max_len + 1)):
                prefix = s[start:end]
                if prefix in words:
                    for suffix in dfs(end):
                        if suffix:
                            res.append(prefix + " " + suffix)
                        else:
                            res.append(prefix)
            return res
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cats and dog", "cat sand dog"])
    assert sorted(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
    print("ALL TESTS PASSED! Ready for submission.")