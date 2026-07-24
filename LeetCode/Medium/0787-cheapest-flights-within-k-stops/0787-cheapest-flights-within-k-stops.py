class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        Q = [(0, src, k)]
        visited = {}

        while Q: 
            price, node, k_remain= heapq.heappop(Q)
            
            if node == dst:
                return price

            if node in visited and visited[node] >= k_remain:
                continue
            visited[node] = k_remain
            
            if k_remain >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq,heappush(Q, (alt, v, k_remain - 1))
        
        return -1