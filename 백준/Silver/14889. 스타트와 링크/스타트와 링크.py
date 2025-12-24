import sys
from itertools import combinations

n = int(sys.stdin.readline())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
people = list(range(n))
result = 100

for team_a in combinations(people, n//2):
    team_b = [p for p in people if p not in team_a]

    a_score = 0
    b_score = 0

    for i in team_a:
        for j in team_a:
            a_score += stats[i][j]
    
    for i in team_b:
        for j in team_b:
            b_score += stats[i][j]
    
    diff = abs(a_score - b_score)
    if diff < result:
        result = diff

print(result)