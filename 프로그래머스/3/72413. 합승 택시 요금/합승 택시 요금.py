import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        queue = [(0, start)]
        
        while queue:
            d, now = heapq.heappop(queue)
            
            if dist[now] < d:
                continue
                
            for nxt, weight in graph[now]:
                cost = d + weight
                
                if cost < dist[nxt]:
                    dist[nxt] = cost
                    heapq.heappush(queue, (cost, nxt))
        return dist

    ds = dijkstra(s)
    da = dijkstra(a)
    db = dijkstra(b)
    
    return min(ds[k] + da[k] + db[k] for k in range(1, n + 1))