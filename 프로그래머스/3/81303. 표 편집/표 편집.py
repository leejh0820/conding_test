def solution(n, k, cmd):
    prev_node = [i - 1 for i in range(n)]
    next_node = [i + 1 for i in range(n)]
    next_node[n - 1] = -1
    
    deleted_stack = []
    current_row = k
    row_status = ["O"] * n
    
    for command in cmd:
        if command.startswith("U"):
            _, move_count = command.split()
            for _ in range(int(move_count)):
                current_row = prev_node[current_row]
        
        elif command.startswith("D"):
            _, move_count = command.split()
            for _ in range(int(move_count)):
                current_row = next_node[current_row]
                
        elif command == "C":
            row_status[current_row] = "X"
            deleted_stack.append(current_row)
            
            up = prev_node[current_row]
            down = next_node[current_row]
            
            if up != -1:
                next_node[up] = down
            if down != -1:
                prev_node[down] = up
                current_row = down
            else:
                current_row = up
                
        elif command == "Z":
            target_row = deleted_stack.pop()
            row_status[target_row] = "O"
            
            up = prev_node[target_row]
            down = next_node[target_row]
            
            if up != -1:
                next_node[up] = target_row
            if down != -1:
                prev_node[down] = target_row
                
    return "".join(row_status)