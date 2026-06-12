def solution(n):
    
    MOD = 1000000007
    
    if n == 1: return 1
    if n == 2: return 3
    if n == 3: return 10
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    dp[2], dp[3] = 3, 10
    
    pattern_sum = [0] * (n + 1)
    
    for i in range(4, n + 1):
        if i >= 4: pattern_sum[i] = (dp[i-4] * 2) % MOD
        if i >= 5: pattern_sum[i] = (pattern_sum[i] + dp[i-5] * 2) % MOD
        if i >= 6: pattern_sum[i] = (pattern_sum[i] + dp[i-6] * 4) % MOD
        if i >= 7: pattern_sum[i] = (pattern_sum[i] + pattern_sum[i-3]) % MOD
            
        dp[i] = (dp[i-1]*1 + dp[i-2]*2 + dp[i-3]*5) % MOD
        dp[i] = (dp[i] + pattern_sum[i]) % MOD
        
    return dp[n]
    
  