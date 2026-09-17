from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        curr_sum = 0
        left = 0

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, min_len[left - 1] + curr_len)
                min_len[right] = min(min_len[right - 1], curr_len) if right > 0 else curr_len
            else:
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')

        return ans if ans != float('inf') else -1
