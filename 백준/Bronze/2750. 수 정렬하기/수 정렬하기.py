import sys

N = int(sys.stdin.readline())

array = [int(sys.stdin.readline()) for _ in range(N)]
array.sort()

for i in array:
    print(i)