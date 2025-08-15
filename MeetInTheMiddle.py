from itertools import combinations
import bisect

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 2
        total = sum(nums)
        def get_subsets(arr):
            res = {}
            for k in range(len(arr)+1):
                res[k] = [sum(comb) for comb in combinations(arr, k)]
            return res

        left = nums[:n]
        right = nums[n:]
        
        left_sums = get_subsets(left)
        right_sums = get_subsets(right)
        for val in right_sums.values():
            val.sort()

        min_diff = float('inf')
        for k in range(n+1):  # k from 0 to n
            left_list = left_sums[k]
            right_list = right_sums[n - k]
            for left_sum in left_list:
                target = total // 2 - left_sum  
                idx = bisect.bisect_left(right_list, target)
                for i in [idx-1, idx]:
                    if 0 <= i < len(right_list):
                        curr_sum = left_sum + right_list[i]
                        other_sum = total - curr_sum
                        min_diff = min(min_diff, abs(curr_sum - other_sum))
                        
        return min_diff
