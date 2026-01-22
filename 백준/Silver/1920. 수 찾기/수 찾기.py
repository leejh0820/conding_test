import sys
N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))

for i in A_list:
    if i in A:
        print(1)
    else:
        print(0)