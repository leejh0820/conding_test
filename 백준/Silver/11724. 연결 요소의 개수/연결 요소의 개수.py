import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    A[u].append(v)
    A[v].append(u)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)