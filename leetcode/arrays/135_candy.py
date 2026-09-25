from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

if __name__ == "__main__":
    sol = Solution()
    assert sol.candy([1, 0, 2]) == 5
    assert sol.candy([1, 2, 2]) == 4
    assert sol.candy([5, 4, 3, 2, 1]) == 15
    assert sol.candy([1, 2, 3, 4, 5]) == 15
    assert sol.candy([1]) == 1
    assert sol.candy([1, 3, 2, 2, 1]) == 7
    print("ALL TESTS PASSED! Ready for submission.")