import sys
N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

start = max(lectures)
end = sum(lectures)

answer = end
while start <= end:
    mid = (start + end) // 2 
        
    count = 1 
    current_sum = 0 
        
    for lec in lectures:
        if current_sum + lec > mid:
            count += 1
            current_sum = lec
        else:
            current_sum += lec
        
    if count <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
            
print(answer)