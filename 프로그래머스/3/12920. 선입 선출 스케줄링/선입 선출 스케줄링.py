import heapq

def solution(n, cores):
    if n <= len(cores):
        return n
    
    n -= len(cores)
    left = 1
    right = max(cores) * n
    time = 0
    
    while left <= right:
        mid = (left + right) // 2
        if sum(mid // c for c in cores) >= n:
            time = mid
            right = mid - 1
        else:
            left = mid + 1
            
    n -= sum((time - 1) // c for c in cores)
    
    for i, c in enumerate(cores):
        if time % c == 0:
            n -= 1
            if n == 0: 
                return i + 1