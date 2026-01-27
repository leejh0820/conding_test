import sys
N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())

    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)
    
print(dp[K])