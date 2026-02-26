import sys
from collections import deque
input = sys.stdin.readline

def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(V):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
print() 
bfs(V)