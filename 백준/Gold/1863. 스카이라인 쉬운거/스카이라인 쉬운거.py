import sys
n = int(sys.stdin.readline())
count = 0
building = [0]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    while building[-1] > y:
        building.pop()
        count += 1

    if building[-1] < y:
        building.append(y)
    
while building:
    if building.pop() > 0:
        count += 1
    
print(count)