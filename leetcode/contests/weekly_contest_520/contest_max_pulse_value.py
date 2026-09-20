from typing import List

class Solution:
    def maxPulseValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0] if n == 1 else 0

        orig = 0
        pref = [0] * (n + 1)
        for i in range(n):
            sign = 1 if i % 2 == 0 else -1
            orig += sign * nums[i]
            pref[i + 1] = pref[i] + (-2 * sign * nums[i])

        best_delta = 0
        inf = float('inf')
        min_even_pref = pref[1]
        min_even_diff = pref[1] + 2 * nums[0]
        min_odd_pref = inf
        min_odd_diff = inf

        for r in range(1, n):
            cur_p = pref[r + 1]
            if r % 2 == 0:
                if min_even_pref != inf:
                    best_delta = max(best_delta, cur_p - min_even_pref)
                if min_odd_diff != inf:
                    best_delta = max(best_delta, cur_p - min_odd_diff)
            else:
                if min_even_diff != inf:
                    best_delta = max(best_delta, cur_p - min_even_diff)
                if min_odd_pref != inf:
                    best_delta = max(best_delta, cur_p - min_odd_pref)

            l = r
            if l % 2 == 0:
                min_even_pref = min(min_even_pref, pref[l + 1])
                min_even_diff = min(min_even_diff, pref[l + 1] + 2 * nums[l])
            else:
                min_odd_pref = min(min_odd_pref, pref[l + 1])
                min_odd_diff = min(min_odd_diff, pref[l + 1] - 2 * nums[l])

        return orig + best_delta
