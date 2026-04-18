def solution(n, lost, reserve):

    actual_reserve = set(reserve) - set(lost)
    actual_lost = set(lost) - set(reserve)    
    
    for i in sorted(actual_reserve):
        if i - 1 in actual_lost:
            actual_lost.remove(i - 1)
        elif i + 1 in actual_lost:
            actual_lost.remove(i + 1)
            
    return n - len(actual_lost)

    