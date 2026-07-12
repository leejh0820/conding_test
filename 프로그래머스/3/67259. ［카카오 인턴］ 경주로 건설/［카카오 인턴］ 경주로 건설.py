import heapq

def solution(board):
    N = len(board)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
   

    INF = float('inf')
    cost_map = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    pq = [(0, 0, 0, -1)]
    
    for i in range(4):
        cost_map[0][0][i] = 0
        
    while pq:
        cost, r, c, prev_dir = heapq.heappop(pq)
        
        if prev_dir != -1 and cost > cost_map[r][c][prev_dir]:
            continue
            
        if r == N - 1 and c == N - 1:
            return cost
            
        for next_dir in range(4):
            nr = r + dr[next_dir]
            nc = c + dc[next_dir]
            
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 1:
                continue
                
            if prev_dir == -1 or prev_dir == next_dir:
                next_cost = cost + 100
            else:
                next_cost = cost + 600
                
            if next_cost < cost_map[nr][nc][next_dir]:
                cost_map[nr][nc][next_dir] = next_cost
                heapq.heappush(pq, (next_cost, nr, nc, next_dir))
                
    return min(cost_map[N-1][N-1])
