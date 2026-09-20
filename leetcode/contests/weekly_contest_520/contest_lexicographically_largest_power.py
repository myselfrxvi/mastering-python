class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        buckets = [nums]
        ans = [0] * 15

        for i in range(15):
            b = 14 -i
            new_buckets = []
            cur_pow = 0
            stopped = False

            for bu in buckets:
                if stopped:
                    new_buckets.append(bu)
                else:
                    ones = [x for x in bu if (x>>b) & 1]
                    zeros = [x for x in bu if not ((x >> b) & 1)]
                    cur_pow += len(ones)
                    if len(zeros) > 0:
                        stopped = True
                        if ones:
                            new_buckets.append(ones)
                        new_buckets.append(zeros)
                    else:
                        new_buckets.append(ones)

                    ans[i] = cur_pow
                    buckets = new_buckets
            return ans