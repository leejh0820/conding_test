import sys, math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

dist = x[0]
last_dist = N - x[-1]

if last_dist > dist:
    dist = last_dist

for i in range(1, M):
    distance = x[i] - x[i-1]
    h = math.ceil(distance/2)
    if h > dist:
        dist = h

print(dist)