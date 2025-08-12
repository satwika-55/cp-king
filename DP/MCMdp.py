from functools import cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @cache
        def dp(a, b, i, j):
            if i == j:
                return 0

            return min(
                dp(a, cuts[k], i, k) + dp(cuts[k], b, k + 1, j)
                for k in range(i, j)
            ) + b - a
        return dp(0, n, 0, len(cuts))
