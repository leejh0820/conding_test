import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[0])
    
    heap = []
    current_time = 0
    job_idx = 0
    completed_jobs = 0
    n = len(jobs)
    
    while completed_jobs < n:
        while job_idx < n and jobs[job_idx][0] <= current_time:
            heapq.heappush(heap, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1
            
        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            answer += (current_time - request_time)
            completed_jobs += 1
        else:
            current_time = jobs[job_idx][0]
            
    return answer // n