import sys
N, D = map(int, sys.stdin.readline().split())
distance = [i for i in range(D + 1)]
shortcut = []

for _ in range(N):
    start, end, dist = map(int, sys.stdin.readline().split())
    if end <= D:
        shortcut.append((start, end, dist))

for i in range(D + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1] + 1)
    for start, end, dist in shortcut:
        if i == start:
            if distance[i] + dist < distance[end]:
                distance[end] = distance[i] + dist
print(distance[D])