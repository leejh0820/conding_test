import sys
N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N):
    line = board[i]
    installed = [False] * N
    possible = True
    
    for k in range(N - 1):
        if line[k] == line[k+1]:
            continue
        
        if abs(line[k] - line[k+1]) > 1:
            possible = False
            break
        
        if line[k] < line[k+1]:
            for j in range(L):
                if k - j < 0 or line[k] != line[k-j] or installed[k-j]:
                    possible = False
                    break
                installed[k-j] = True
        else:
            for j in range(1, L + 1):
                if k + j >= N or line[k+1] != line[k+j] or installed[k+j]:
                    possible = False
                    break
                installed[k+j] = True
        
        if not possible: break
    if possible: result += 1

for j in range(N):
    line = [board[i][j] for i in range(N)]
    installed = [False] * N
    possible = True
    
    for k in range(N - 1):
        if line[k] == line[k+1]:
            continue
        
        if abs(line[k] - line[k+1]) > 1:
            possible = False
            break
        
        if line[k] < line[k+1]:
            for l in range(L):
                if k - l < 0 or line[k] != line[k-l] or installed[k-l]:
                    possible = False
                    break
                installed[k-l] = True
        else:
            for l in range(1, L + 1):
                if k + l >= N or line[k+1] != line[k+l] or installed[k+l]:
                    possible = False
                    break
                installed[k+l] = True
        
        if not possible: break
    if possible: result += 1

print(result)