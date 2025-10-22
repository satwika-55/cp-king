# RECURSION -> 
# TC : 0(2^n), SC: 0(n)

# MEMOIZATION 

def lis_memo(arr):
    n = len(arr)

    # @lru_cache(None)
    def dfs(i, prev):
        if i == n:
            return 0
        take = 0
        if prev == -1 or arr[i] > arr[prev]:
            take = 1 + dfs(i + 1, i)
        not_take = dfs(i + 1, prev)
        return max(take, not_take)

    return dfs(0, -1)

# TC : O(n^2), SC: O(n^2) + O(n)


# TABULATION 


def lis_tab(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# TC : O(n^2), SC: O(n)



#BINARY SEARCH




import bisect

def lengthOfLIS(nums):
    dp = []  # dp[i] = min tail of all increasing subsequences of length i+1
    for num in nums:
        # Find the position to replace using binary search
        idx = bisect.bisect_left(dp, num)
        if idx < len(dp):
            dp[idx] = num
        else:
            dp.append(num)
    return len(dp)


# TC : O(n log n), SC: O(n)
