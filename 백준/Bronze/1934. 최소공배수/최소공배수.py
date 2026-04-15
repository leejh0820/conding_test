import sys, math
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    lcm = int(math.lcm(A, B))
    print(lcm)