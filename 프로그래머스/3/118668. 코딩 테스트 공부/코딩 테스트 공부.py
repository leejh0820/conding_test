def solution(alp, cop, problems):
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    inf = float('inf')
    
    dp = [[inf] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
                
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
                
            for req_alp, req_cop, rwd_alp, rwd_cop, cost in problems:
                if i >= req_alp and j >= req_cop:
                    next_alp = min(i + rwd_alp, max_alp)
                    next_cop = min(j + rwd_cop, max_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
    return dp[max_alp][max_cop]