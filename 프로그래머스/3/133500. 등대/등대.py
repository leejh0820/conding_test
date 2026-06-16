import sys
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    adj = [[] for _ in range(n + 1)]
    
    for u, v in lighthouse:
        adj[u].append(v)
        adj[v].append(u)
        
    dp = [[0, 1] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += dp[v][1]
                dp[u][1] += min(dp[v][0], dp[v][1])
                
    dfs(1)
    
    return min(dp[1][0], dp[1][1])