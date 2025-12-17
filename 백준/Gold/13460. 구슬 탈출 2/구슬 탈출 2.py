from collections import deque
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    input = sys.stdin.read().split()
    N, M = int(input[0]), int(input[1])
    board = [list(row) for row in input[2:]]

    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    queue = deque()

    rr, rc, br, bc = 0, 0, 0, 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                rr, rc = r, c
            elif board[r][c] == 'B':
                br, bc = r, c
    
    queue.append((rr, rc, br, bc, 1))
    visited[rr][rc][br][bc] = True

    def move(r, c, dr, dc):
        count = 0

        while board[r + dr][c + dc] != '#' and board[r][c] != 'O':
            r += dr
            c += dc
            count += 1
        return r, c, count

    while queue:
        rr, rc, br, bc, depth = queue.popleft()

        if depth > 10:
            break

        for i in range(4):
            nrr, nrc, r_cnt = move(rr, rc, dr[i], dc[i])
            nbr, nbc, b_cnt = move(br, bc, dr[i], dc[i])

            if board[nbr][nbc] == 'O':
                continue
            
            if board[nrr][nrc] == 'O':
                print(depth)
                return

            if nrr == nbr and nrc == nbc:
                if r_cnt > b_cnt: 
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]

            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = True
                queue.append((nrr, nrc, nbr, nbc, depth + 1))

    print(-1)

solve()