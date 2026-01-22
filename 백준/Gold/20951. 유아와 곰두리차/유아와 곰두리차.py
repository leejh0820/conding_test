import sys
N, M = map(int, sys.stdin.readline().split())
MOD = 10**9 + 7
edges = []
dp = [1] * N  

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    edges.append((u, v))

for _ in range(7):
    next_dp = [0] * N
    for u, v in edges:
        next_dp[u] = (next_dp[u] + dp[v]) % MOD
        next_dp[v] = (next_dp[v] + dp[u]) % MOD
    dp = next_dp

print(sum(dp) % MOD)