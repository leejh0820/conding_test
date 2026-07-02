def solution(e, starts):
    counts = [0] * (e + 1)
    
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            counts[j] += 1
            
    queries = sorted([(s, idx) for idx, s in enumerate(starts)])
    
    answer = [0] * len(starts)
    max_cnt = 0
    best_num = 0
    curr = e
    
    for s, idx in reversed(queries):
        while curr >= s:
            if counts[curr] >= max_cnt:
                max_cnt = counts[curr]
                best_num = curr
            curr -= 1
            
        answer[idx] = best_num
        
    return answer