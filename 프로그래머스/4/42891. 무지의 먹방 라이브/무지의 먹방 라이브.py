import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    pq = []
    for idx, time in enumerate(food_times):
        heapq.heappush(pq, (time, idx + 1))
        
    total_time = 0      
    prev_time = 0    
    remain_cnt = len(food_times) 
    
    while total_time + ((pq[0][0] - prev_time) * remain_cnt) <= k:
        curr_time, _ = heapq.heappop(pq)
        
        total_time += (curr_time - prev_time) * remain_cnt
        remain_cnt -= 1
        prev_time = curr_time
        
    remain_foods = sorted(pq, key=lambda x: x[1])
    
    target_idx = (k - total_time) % remain_cnt
    answer = remain_foods[target_idx][1]
    
    return answer