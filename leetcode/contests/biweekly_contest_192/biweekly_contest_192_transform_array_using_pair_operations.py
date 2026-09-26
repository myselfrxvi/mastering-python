from typing import List

class Solution:
    def canTransform(self, source: List[int], target: List[int]) -> bool:
        # Sum conservation invariant:
        # source[i]' + source[j]' = (source[i] + source[j] - delta) + delta = source[i] + source[j]
        # Any element can be set to delta while dumping residual sum into another index.
        return sum(source) == sum(target)

if __name__ == "__main__":
    sol = Solution()
    assert sol.canTransform([1, 2, 3], [0, 2, 4]) == True
    assert sol.canTransform([-5, -5], [-15, 5]) == True
    assert sol.canTransform([1, 2, 1], [0, 2, 5]) == False
    print("ALL TESTS PASSED! Biweekly Contest 192 Q2 verified.")
