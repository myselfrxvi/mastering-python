from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start: int) -> None:
            if start == n:
                res.append(nums[:])
                return
            seen = set()
            for i in range(start, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
