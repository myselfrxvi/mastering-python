from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for x in nums:
            curr_sum = max(x, curr_sum+x)
            max_sum = max(max_sum, curr_sum)

        return max_sum
