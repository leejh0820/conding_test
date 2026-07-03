from itertools import permutations

def solution(n, weak, dist):
    w_len = len(weak)
    
    for i in range(w_len):
        weak.append(weak[i] + n)
        
    min_friends = len(dist) + 1
    
    for start in range(w_len):
        for f_order in permutations(dist):
            count = 1
            curr_pos = weak[start] + f_order[count - 1]
            
            for idx in range(start, start + w_len):
                if curr_pos < weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    curr_pos = weak[idx] + f_order[count - 1]
            
            if count < min_friends:
                min_friends = count
            
    if min_friends > len(dist):
        return -1
        
    return min_friends


