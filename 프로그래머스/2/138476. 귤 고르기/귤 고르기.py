def solution(k, tangerine):
    answer = 0
    total = 0
    tangerine.sort()
    stack = []
    current_count = 1
    
    for i in range(1, len(tangerine)):
        if tangerine[i] == tangerine[i-1]:
            current_count += 1
        else:
            stack.append(current_count)
            current_count = 1
    stack.append(current_count)
    
    stack.sort(reverse=True)
    
    for count in stack:
        total += count
        answer += 1
        if total >= k:
            break
            
    return answer