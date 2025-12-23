import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    found_empty = False

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0:
                found_empty = True
                break

    if not found_empty:
        back_r = r - dr[d]
        back_c = c - dc[d]
        if 0 <= back_r < n and 0 <= back_c < m and board[back_r][back_c] != 1:
            r, c = back_r, back_c
        else:
            break
            

    else:
        d = (d + 3) % 4

        front_r = r + dr[d]
        front_c = c + dc[d]
        
        if 0 <= front_r < n and 0 <= front_c < m and board[front_r][front_c] == 0:
            r, c = front_r, front_c

print(count)