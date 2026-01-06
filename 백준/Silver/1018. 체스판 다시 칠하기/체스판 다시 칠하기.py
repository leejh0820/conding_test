import sys
N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
count = 64
for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'W':
                        white += 1
                    if board[a][b] != 'B':
                        black += 1
                else:
                    if board[a][b] != 'B':
                        white += 1
                    if board[a][b] != 'W':
                        black += 1
        count = min(count, white, black)
print(count)