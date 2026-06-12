import sys
sys.setrecursionlimit(1000000)

def solution(a, edges):
    
    if sum(a) != 0:
        return -1

    n = len(a)
    graph = [[] for _ in range(n)]
    
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * n
    answer = 0
    
    def dfs(current):
        nonlocal answer
        visited[current] = True
        
        current_weight = a[current]
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                child_weight = dfs(neighbor)
                current_weight += child_weight
                answer += abs(child_weight)
        
        return current_weight
    
    dfs(0) 
    
    return answer