def solution(a, b, g, s, w, t):
    low = 0
    high = 10**15
    answer = high

    while low <= high:
        mid = (low + high) // 2
        
        total_g = 0
        total_s = 0
        total_total = 0

        for i in range(len(g)):
            current_g = g[i]
            current_s = s[i]
            current_w = w[i]
            current_t = t[i]

            move_cnt = mid // (current_t * 2)
            if mid % (current_t * 2) >= current_t:
                move_cnt += 1

            max_weight = move_cnt * current_w

            total_g += min(current_g, max_weight)
            total_s += min(current_s, max_weight)
            total_total += min(current_g + current_s, max_weight)

        if total_g >= a and total_s >= b and total_total >= a + b:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer