import sys
from collections import deque
N, L = map(int, sys.stdin.readline().split())
A_list = list(map(int, sys.stdin.readline().split()))
mydeque = deque()

for i in range(N):
    while mydeque and mydeque[-1][0] > A_list[i]:
        mydeque.pop()
    mydeque.append((A_list[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')