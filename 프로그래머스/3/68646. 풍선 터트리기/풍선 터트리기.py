def solution(a):
    n = len(a)
    if n <= 2:
        return n
        
    left_min = [0] * n
    right_min = [0] * n
    
    current_min = a[0]
    for i in range(n):
        if a[i] < current_min:
            current_min = a[i]
        left_min[i] = current_min
        
    current_min = a[-1]
    for i in range(n - 1, -1, -1):
        if a[i] < current_min:
            current_min = a[i]
        right_min[i] = current_min
        
    answer = 0
    for i in range(n):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
            
    return answer