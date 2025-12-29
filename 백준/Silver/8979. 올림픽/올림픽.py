import sys

N, K = map(int, sys.stdin.readline().split())
scores = {}

for _ in range(N):
    c, g, s, b = map(int, sys.stdin.readline().split())
    scores[c] = g*10000 + s*100 + b

target_score = scores[K]
rank = 1

for i in scores:
    if scores[i] > target_score:
        rank += 1

print(rank)