import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    print(prefix_sum[v] - prefix_sum[u-1])