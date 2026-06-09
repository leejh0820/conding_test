def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)
    
    max_dp = [[float('-inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
        
    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            for k in range(i, j):
                if ops[k] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                elif ops[k] == '-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    return max_dp[0][n-1]