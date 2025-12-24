import sys

def solve():
    N, M, H = map(int, sys.stdin.readline().split())
    board = [[0] * (N + 2) for _ in range(H + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        board[a][b] = 1

    def mismatch():
        mis = 0
        for start in range(1, N + 1):
            cur = start
            for r in range(1, H + 1):
                if board[r][cur]:
                    cur += 1
                elif board[r][cur - 1]:
                    cur -= 1
            if cur != start:
                mis += 1
        return mis

    if mismatch() == 0:
        print(0)
        return

    def dfs(limit, cnt, sr, sc):
        mis = mismatch()
        if mis == 0:
            return True

        rem = limit - cnt
        if (mis + 1) // 2 > rem:
            return False

        if cnt == limit:
            return False

        for r in range(sr, H + 1):
            c = sc if r == sr else 1
            while c <= N - 1:
                if board[r][c] == 0 and board[r][c - 1] == 0 and board[r][c + 1] == 0:
                    board[r][c] = 1
                    if dfs(limit, cnt + 1, r, c + 2):
                        return True
                    board[r][c] = 0
                c += 1
            sc = 1
        return False

    for limit in range(1, 4):
        if dfs(limit, 0, 1, 1):
            print(limit)
            return
    print(-1)

solve()

