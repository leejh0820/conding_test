import sys
from collections import deque

def move(board, x, y, dx, dy):
    dist = 0
    while True:
        nx, ny = x + dx, y + dy
        cell = board[nx][ny]
        if cell == '#':
            break
        x, y = nx, ny
        dist += 1
        if cell == 'O':
            return x, y, dist, True
    return x, y, dist, False

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    rx = ry = bx = by = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                bx, by = i, j
                board[i][j] = '.'

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # U D L R
    visited = set()
    visited.add((rx, ry, bx, by))
    q = deque([(rx, ry, bx, by, 0)])

    while q:
        rx, ry, bx, by, d = q.popleft()
        if d == 10:
            continue

        for dx, dy in dirs:
            nrx, nry, rdist, r_hole = move(board, rx, ry, dx, dy)
            nbx, nby, bdist, b_hole = move(board, bx, by, dx, dy)

            if b_hole:
                continue

            if r_hole:
                print(d + 1)
                return

            if nrx == nbx and nry == nby:
                if rdist > bdist:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, d + 1))

    print(-1)

if __name__ == "__main__":
    solve()
