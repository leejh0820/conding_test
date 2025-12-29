import sys
N = int(sys.stdin.readline())

n = 0
while 3*n**2 + 3*n + 1 < N:
    n += 1

print(n + 1)