from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]