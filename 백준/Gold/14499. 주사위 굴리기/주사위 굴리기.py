import sys
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    x = int(data[2]) 
    y = int(data[3]) 
    K = int(data[4])
    
    ptr = 5
    board = []
    for _ in range(N):
        board.append(list(map(int, data[ptr:ptr+M])))
        ptr += M
    
    commands = list(map(int, data[ptr:]))
    
    dice = [0] * 6

    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    
    for cmd in commands:
        nx, ny = x + dx[cmd], y + dy[cmd]
        
        if not (0 <= nx < N and 0 <= ny < M):
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

solve()