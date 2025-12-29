import sys
import copy

n = int(sys.stdin.readline())
board = [list(map(int, input().split())) for _ in range(n)]

def merge_line(line):
    arr = [x for x in line if x != 0]
    res = []
    i = 0
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i + 1]:
            res.append(arr[i] * 2)
            i += 2
        else:
            res.append(arr[i])
            i += 1
    res += [0] * (len(line) - len(res))
    return res

def move(board, direction):
    if direction == 0:  
        for c in range(n):
            col = [board[r][c] for r in range(n)]
            merged = merge_line(col)
            for r in range(n):
                board[r][c] = merged[r]

    elif direction == 1:  
        for c in range(n):
            col = [board[r][c] for r in range(n)][::-1]
            merged = merge_line(col)[::-1]
            for r in range(n):
                board[r][c] = merged[r]

    elif direction == 2:  
        for r in range(n):
            board[r] = merge_line(board[r])

    else:  
        for r in range(n):
            rev = board[r][::-1]
            merged = merge_line(rev)[::-1]
            board[r] = merged

    return board

max_val = 0

def dfs(board, cnt):
    global max_val
    if cnt == 5:
        for row in board:
            max_val = max(max_val, max(row))
        return

    for i in range(4):
        new_board = move(copy.deepcopy(board), i)
        dfs(new_board, cnt + 1)

dfs(board, 0)
print(max_val)