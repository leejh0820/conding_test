def solution(target):
    singles_bull = [i for i in range(1, 21)] + [50]
    multiples = [i * 2 for i in range(1, 21)] + [i * 3 for i in range(1, 21)]
    
    INF = 999999
    dp = [[INF, -1] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    for i in range(1, target + 1):
        best_darts = INF
        best_bonus = -1
        
        for s in singles_bull:
            if i >= s:
                cand_darts = dp[i - s][0] + 1
                cand_bonus = dp[i - s][1] + 1
                
                if cand_darts < best_darts:
                    best_darts = cand_darts
                    best_bonus = cand_bonus
                elif cand_darts == best_darts and cand_bonus > best_bonus:
                    best_bonus = cand_bonus
                    
        for m in multiples:
            if i >= m:
                cand_darts = dp[i - m][0] + 1
                cand_bonus = dp[i - m][1] + 0
                
                if cand_darts < best_darts:
                    best_darts = cand_darts
                    best_bonus = cand_bonus
                elif cand_darts == best_darts and cand_bonus > best_bonus:
                    best_bonus = cand_bonus
                    
        dp[i] = [best_darts, best_bonus]
        
    return dp[target]