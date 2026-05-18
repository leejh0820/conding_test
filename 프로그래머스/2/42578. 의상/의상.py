from collections import Counter

def solution(clothes):
    answer = 1
    clothes_counter = Counter([category for name, category in clothes])
    
    for count in clothes_counter.values():
        answer *= (count + 1)

    return answer - 1