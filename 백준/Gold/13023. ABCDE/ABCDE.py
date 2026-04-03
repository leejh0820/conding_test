import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
visited = [False] * N
result = False

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    global result
    if depth == 5:
        result = True
        return
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[start] = False

for i in range(N):
    dfs(i, 1)
    if result:
        break

if result:
    print(1)
else:
    print(0)

