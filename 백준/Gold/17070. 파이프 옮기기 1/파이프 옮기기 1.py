import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1
    
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            continue
            
        if c + 1 < N and board[r][c+1] == 0:
            dp[0][r][c+1] += dp[0][r][c] + dp[2][r][c]
                
        if r + 1 < N and board[r+1][c] == 0:
            dp[1][r+1][c] += dp[1][r][c] + dp[2][r][c]
                
        if r + 1 < N and c + 1 < N:
            if board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0:
                dp[2][r+1][c+1] += dp[0][r][c] + dp[1][r][c] + dp[2][r][c]
                    
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])