from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            new_dp[num_mod] += 1
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * num_mod) % k
                    new_dp[new_rem] += dp[r]
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp

        return ans
