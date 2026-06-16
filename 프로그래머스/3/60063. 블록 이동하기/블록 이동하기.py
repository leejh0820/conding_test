from collections import deque

def solution(board):
    n = len(board)
    b = [[1] * (n + 2) for _ in range(n + 2)]
    
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] = board[i][j]

    q = deque([(((1, 1), (1, 2)), 0)])
    visited = {((1, 1), (1, 2))}

    while q:
        pos, cost = q.popleft()
        (r1, c1), (r2, c2) = pos

        if (n, n) in pos:
            return cost

        nxt = []
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if b[r1+dr][c1+dc] == 0 and b[r2+dr][c2+dc] == 0:
                nxt.append(((r1+dr, c1+dc), (r2+dr, c2+dc)))

        if r1 == r2:
            for d in [-1, 1]:
                if b[r1+d][c1] == 0 and b[r2+d][c2] == 0:
                    nxt.append(((r1, c1), (r1+d, c1)))
                    nxt.append(((r2, c2), (r2+d, c2)))
        else:
            for d in [-1, 1]:
                if b[r1][c1+d] == 0 and b[r2][c2+d] == 0:
                    nxt.append(((r1, c1), (r1, c1+d)))
                    nxt.append(((r2, c2), (r2, c2+d)))

        for n_pos in nxt:
            s_pos = tuple(sorted(n_pos))
            if s_pos not in visited:
                visited.add(s_pos)
                q.append((s_pos, cost + 1))