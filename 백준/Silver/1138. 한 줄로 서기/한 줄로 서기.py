import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

people = []

for i in range(N, 0, -1):
    people.insert(data[i-1], i)

print(*(people))