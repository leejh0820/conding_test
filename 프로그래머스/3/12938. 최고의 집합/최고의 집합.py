def solution(n, s):
    if s < n:
        return [-1]
    
    num1 = s // n
    num2 = s % n
    
    answer = [num1] * n
    
    for i in range(num2):
        answer[n - 1 -i] += 1
    
    return answer