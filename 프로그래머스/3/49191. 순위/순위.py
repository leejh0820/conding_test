def solution(n, results):
    wins = {i: set() for i in range(1, n + 1)}
    loses = {i: set() for i in range(1, n + 1)}
    
    for w, l in results:
        wins[w].add(l)
        loses[l].add(w)
        
    for k in range(1, n + 1):
        for winner in loses[k]:
            wins[winner].update(wins[k])
            
        for loser in wins[k]:
            loses[loser].update(loses[k])
            
    answer = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
            
    return answer