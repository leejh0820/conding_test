import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
factor = list(map(int, input().split()))
factor.sort()

count = 0
i = 0
j = N - 1

while i < j:
    if factor[i] + factor[j] == M:
        count += 1
        i += 1
        j -= 1
    elif factor[i] + factor[j] < M:
        i += 1
    else:
        j -= 1

print(count)