def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    changes_board = [[0] * (M + 1) for _ in range(N + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        value = -degree if type == 1 else degree
        
        changes_board[r1][c1] += value
        changes_board[r1][c2 + 1] -= value
        changes_board[r2 + 1][c1] -= value
        changes_board[r2 + 1][c2 + 1] += value

    for r in range(N):
        for c in range(1, M):
            changes_board[r][c] += changes_board[r][c - 1]
            
    for c in range(M):
        for r in range(1, N):
            changes_board[r][c] += changes_board[r - 1][c]
            
    for r in range(N):
        for c in range(M):
            if board[r][c] + changes_board[r][c] > 0:
                answer += 1
                
    return answer