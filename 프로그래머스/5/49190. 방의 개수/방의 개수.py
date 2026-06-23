def solution(arrows):
    move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    nodes = {(0, 0)}
    edges = set()
    cy, cx = 0, 0
    answer = 0
    
    for arrow in [a for a in arrows for _ in (0, 1)]:
        dy, dx = move[arrow]
        ny, nx = cy + dy, cx + dx
        
        if (ny, nx) in nodes and (cy, cx, ny, nx) not in edges:
            answer += 1
            
        nodes.add((ny, nx))
        edges.add((cy, cx, ny, nx))
        edges.add((ny, nx, cy, cx))
        cy, cx = ny, nx
        
    return answer