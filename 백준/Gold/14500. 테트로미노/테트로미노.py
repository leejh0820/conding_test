import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    B = board
    V = visited
    N, M = n, m

    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    DR, DC = dr, dc

    max_element = max(map(max, B))
    ME = max_element

    ans = 0

    def dfs(r, c, depth, s):
        nonlocal ans

        if s + ME * (4 - depth) <= ans:
            return

        if depth == 4:
            if s > ans:
                ans = s
            return

        for k in range(4):
            nr = r + DR[k]
            nc = c + DC[k]
            if 0 <= nr < N and 0 <= nc < M and not V[nr][nc]:
                V[nr][nc] = True
                dfs(nr, nc, depth + 1, s + B[nr][nc])
                V[nr][nc] = False

    def check_t_shape(r, c):
        nonlocal ans
        center = B[r][c]
        neigh_sum = 0
        min_neigh = 10**9
        cnt = 0

        for k in range(4):
            nr = r + DR[k]
            nc = c + DC[k]
            if 0 <= nr < N and 0 <= nc < M:
                val = B[nr][nc]
                neigh_sum += val
                if val < min_neigh:
                    min_neigh = val
                cnt += 1

        if cnt == 3:
            s = center + neigh_sum
            if s > ans:
                ans = s
        elif cnt == 4:
            s = center + neigh_sum - min_neigh
            if s > ans:
                ans = s

    for r in range(N):
        for c in range(M):
            V[r][c] = True
            dfs(r, c, 1, B[r][c])
            V[r][c] = False
            check_t_shape(r, c)

    print(ans)

if __name__ == "__main__":
    solve()
