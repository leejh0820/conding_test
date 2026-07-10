def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    left = 1
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        
        current = 0
        remove_rocks = 0
        
        for rock in rocks:
            if rock - current < mid:
                remove_rocks += 1
            else:
                current = rock
        
        if distance - current < mid:
            remove_rocks += 1
        
        if remove_rocks > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer



    
    