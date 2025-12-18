import sys


input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())


board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))


dice = [0] * 6

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for cmd in commands:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    if not (0 <= nx < n and 0 <= ny < m):
        continue  
    
    if cmd == 1: 
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif cmd == 2: 
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif cmd == 3: 
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif cmd == 4: 
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        
       
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:

        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])