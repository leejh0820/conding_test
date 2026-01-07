import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
robots = deque([False] * N)
step = 0

while True:
    step += 1
    belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = False

    for i in range(N-1, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] >= 1:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
    robots[N-1] = False

    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

    if belt.count(0) >= K:
        print(step)
        break