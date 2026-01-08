import sys
from itertools import permutations

N = int(sys.stdin.readline())
innings = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

for p in permutations(range(1, 9)):
    p = list(p)
    order = p[:3] + [0] +p[3:]

    score = 0
    idx = 0

    for i in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0

        while out < 3:
            result = i[order[idx]]

            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2: 
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif result == 3: 
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif result == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0  
            idx = (idx + 1) % 9
                
    if score > max_score:
        max_score = score
            
print(max_score)