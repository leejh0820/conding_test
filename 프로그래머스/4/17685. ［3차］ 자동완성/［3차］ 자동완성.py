def solution(words):
    n = len(words)
    words.sort()
    
    overlap = [0] * n
    
    for i in range(n - 1):
        left_word = words[i]
        right_word = words[i+1]
        same_cnt = 0
        
        for char1, char2 in zip(left_word, right_word):
            if char1 == char2:
                same_cnt += 1
            else:
                break
                
        overlap[i] = max(overlap[i], same_cnt)
        overlap[i+1] = max(overlap[i+1], same_cnt)
            
    answer = 0
    
    for i in range(n):
        answer += min(len(words[i]), overlap[i] + 1)
        
    return answer
    
