def solution(n, count):
    mod = 1000000007
    
    dp = [[0] * (count + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, min(i, count) + 1):
            visible = dp[i-1][j-1]
            hidden = dp[i-1][j] * 2 * (i - 1)
            
            dp[i][j] = (visible + hidden) % mod
            
    return dp[n][count]