def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        
        for stone in stones:
            if stone < mid:
                count += 1
            else:
                count = 0
            if count == k:
                break
                
        if count == k:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    return answer