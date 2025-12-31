import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)

dist = [-1] * (N + 1)
dist[1] = 0

queue = deque([1])

while queue:
    curr = queue.popleft()
    
    if curr == N:
        break
        
    for next_node in adj[curr]:
        if dist[next_node] == -1:
            dist[next_node] = dist[curr] + 1
            queue.append(next_node)

print(dist[N])