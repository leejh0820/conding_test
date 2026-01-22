import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
s = 0  

dp = [0] * M
dp[0] = 1

for i in numbers:
    s = (s + i) % M
    dp[s] += 1

for j in dp:
    answer += j * (j-1) // 2

print(answer)