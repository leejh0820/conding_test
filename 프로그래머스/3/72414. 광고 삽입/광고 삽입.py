def str_to_sec(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def sec_to_str(total_sec):
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)
    
    timeline = [0] * (play_sec + 1)
    
    for log in logs:
        start_str, end_str = log.split('-')
        timeline[str_to_sec(start_str)] += 1
        timeline[str_to_sec(end_str)] -= 1
        
    for i in range(1, play_sec + 1):
        timeline[i] += timeline[i - 1]
        
    curr_sum = sum(timeline[:adv_sec])
    max_sum = curr_sum
    best_start = 0
    
    for start in range(1, play_sec - adv_sec + 1):
        end = start + adv_sec - 1
        curr_sum = curr_sum - timeline[start - 1] + timeline[end]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = start
            
    return sec_to_str(best_start)