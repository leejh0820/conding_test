import sys

N = int(sys.stdin.readline())
people = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    people.append((x, y))

result = []
for i in range(N):
    rank = 1  
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    result.append(rank)

print(*(result))