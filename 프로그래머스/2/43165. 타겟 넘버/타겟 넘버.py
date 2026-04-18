def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx, current_num):
        nonlocal answer
        if idx == n:
            if current_num == target:
                answer += 1
            return 
        dfs(idx+1, current_num + numbers[idx])
        dfs(idx+1, current_num - numbers[idx])
        
    dfs(0,0)
    return answer