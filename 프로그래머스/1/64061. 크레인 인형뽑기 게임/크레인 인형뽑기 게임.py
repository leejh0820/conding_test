def solution(board, moves):
    stack = []
    answer = 0
    n = len(board)
    
    for move in moves:
        col = move - 1
        
        for row in range(n):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0
                
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                    
                break
    
    return answer