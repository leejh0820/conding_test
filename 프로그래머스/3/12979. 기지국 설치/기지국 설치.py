import math

def solution(n, stations, w):
    answer = 0
    cover_range = 2 * w + 1
    current = 1

    for station in stations:
        if current < station - w:
            length = (station - w) - current
            answer += math.ceil(length / cover_range)
        current = station + w + 1
        
    if current <= n:
        length = n - current + 1
        answer += math.ceil(length / cover_range)

    return answer