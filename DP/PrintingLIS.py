def printLIS(nums):
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n  

    max_len = 1
    last_index = 0

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

        if dp[i] > max_len:
            max_len = dp[i]
            last_index = i

    lis = []
    while last_index != -1:
        lis.append(nums[last_index])
        last_index = parent[last_index]

    lis.reverse()
    return lis