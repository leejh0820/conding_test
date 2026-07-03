def rotate_90(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            rotated[c][n - 1 - r] = matrix[r][c]
    return rotated

def check_lock(board, n, m):
    for r in range(n):
        for c in range(n):
            if board[m - 1 + r][m - 1 + c] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    board_size = n + (m - 1) * 2
    
    for _ in range(4):
        key = rotate_90(key)
        
        for start_r in range(n + m - 1):
            for start_c in range(n + m - 1):
                
                board = [[0] * board_size for _ in range(board_size)]
                for r in range(n):
                    for c in range(n):
                        board[m - 1 + r][m - 1 + c] = lock[r][c]
                
                for r in range(m):
                    for c in range(m):
                        board[start_r + r][start_c + c] += key[r][c]
                
                if check_lock(board, n, m):
                    return True
                    
    return False