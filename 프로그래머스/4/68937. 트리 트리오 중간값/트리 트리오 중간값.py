from collections import deque

def solution(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    def get_dist(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        
        while q:
            curr = q.popleft()
            for nxt in graph[curr]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[curr] + 1
                    q.append(nxt)
        return dist

    d_1 = get_dist(1)
    X = d_1.index(max(d_1))
    
    d_X = get_dist(X)
    D = max(d_X)
    Y = d_X.index(D)
    
    d_Y = get_dist(Y)
    
    end_points = sum(1 for i in range(1, n + 1) if d_X[i] == D or d_Y[i] == D)
            
    return D if end_points >= 3 else D - 1