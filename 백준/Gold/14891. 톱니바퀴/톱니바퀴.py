import sys
from collections import deque

input = sys.stdin.readline
gears = [deque(list(map(int, input().strip()))) for _ in range(4)]

def rotate(idx, direction):
    rotations = [0] * 4
    rotations[idx] = direction
    
    for i in range(idx, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            rotations[i-1] = -rotations[i]
        else:
            break 
            
    for i in range(idx, 3):
        if gears[i][2] != gears[i+1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break
            
    for i in range(4):
        if rotations[i] != 0:
            gears[i].rotate(rotations[i])

N = int(input())
for _ in range(N):
    num, direct = map(int, input().split())
    rotate(num - 1, direct)

score = 0
for i in range(4):
    if gears[i][0] == 1: 
        score += (2 ** i)

print(score)