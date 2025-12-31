import sys
from collections import deque

def bfs(maze, start_pos, end_pos, r, c):
    if start_pos == end_pos:
        return 0
    
    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = [[False] * c for _ in range(r)]
    visited[start_pos[0]][start_pos[1]] = True
    
    while queue:
        curr_r, curr_c, dist = queue.popleft()
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr_r + dr, curr_c + dc
            
            if 0 <= nr < r and 0 <= nc < c and maze[nr][nc] != '#' and not visited[nr][nc]:
                if (nr, nc) == end_pos:
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return 0

n = int(sys.stdin.readline())

for _ in range(n):
    r, c, d = map(int, sys.stdin.readline().split())
    maze = [sys.stdin.readline().strip() for _ in range(r)]
    
    points = {}
    for i in range(r):
        for j in range(c):
            char = maze[i][j]
            if char == 'S': points['S'] = (i, j)
            elif char == 'E': points['E'] = (i, j)
            elif '1' <= char <= '9': points[char] = (i, j)
            
    path_order = ['S'] + [str(i) for i in range(1, d + 1)] + ['E']
    
    total_distance = 0
    for k in range(len(path_order) - 1):
        start = points[path_order[k]]
        end = points[path_order[k+1]]
        total_distance += bfs(maze, start, end, r, c)
        
    print(total_distance)