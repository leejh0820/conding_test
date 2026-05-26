def solution(n, computers):
    answer = 0
    vistied = [False] * n
    
    def dfs(com):
        vistied[com] = True
        for connect in range(n):
            if computers[com][connect] == 1 and not vistied[connect]:
                dfs(connect)
        
    for i in range(n):
        if not vistied[i]:
            dfs(i)
            answer += 1
    
    return answer