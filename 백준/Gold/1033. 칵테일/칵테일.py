import sys, math
N = int(sys.stdin.readline())

if N == 1:
    print(1)
    sys.exit()

A = [[] for _ in range(N)]
visited = [False] * N
D = [0] * N
total_lcm = 1

for _ in range(N - 1):
    a, b, p, q = map(int, sys.stdin.readline().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    total_lcm *= math.lcm(p, q)

def DFS(v):
    visited[v] = True
    for next_node, p, q in A[v]:
        if not visited[next_node]:
            D[next_node] = D[v] * q // p
            DFS(next_node)

D[0] = total_lcm
DFS(0)

mgcd = D[0]
for i in range(1, N):
    mgcd = math.gcd(mgcd, D[i])

for i in range(N):
    print(D[i] // mgcd, end=' ')