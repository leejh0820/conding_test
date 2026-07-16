def solution(order):
    stack = []
    n = len(order)
    numbers = list(range(1, n+1))
    answer = 0
    numbers_idx = 0 
    
    for target in order:
        while numbers_idx < n and numbers[numbers_idx] <= target:
            stack.append(numbers[numbers_idx])
            numbers_idx += 1
            
        if stack and stack[-1] == target:
            stack.pop()
            answer += 1
        else:
            break
    
    return answer

