# def solution(sequence):
#     n = len(sequence)
    
#     if n == 1:
#         return max(sequence[0], -sequence[0])
    
#     pulse1 = [0] * n
#     pulse2 = [0] * n
    
#     for i in range(n):
#         if i % 2 == 0:
#             pulse1[i] = sequence[i]*1
#             pulse1[i] = sequence[i]*-1
#         else:
#             pulse1[i] = sequence[i]*-1
#             pulse1[i] = sequence[i]*1            
            
#     def max_sum(arr):
#         max_sum = arr[0]
#         current_sum = arr[0]
        
#         for i in range(1, len(arr)):
#             current_sum = max(arr[i], current_sum + arr[i])
#             max_sum = max(max_sum, current_sum)
            
#         return max_sum

    
    
#     return max(max_sum(pulse1), max_sum(pulse2))

def solution(sequence):
    n = len(sequence)
    if n == 1:
        # 길이가 1일 때는 원래 값과 부호를 바꾼 값 중 큰 놈이 무조건 정답
        return max(sequence[0], -sequence[0])
        
    pulse1 = [0] * n
    pulse2 = [0] * n
    
    for i in range(n):
        if i % 2 == 0:
            pulse1[i] = sequence[i]
            pulse2[i] = -sequence[i]
        else:
            pulse1[i] = -sequence[i]
            pulse2[i] = sequence[i]
            
    def get_max_subarray_sum(arr):
        # ⚠️ 0이 아니라 반드시 첫 번째 원소로 초기화!
        max_total = arr[0]
        current_sum = arr[0]
        
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_total = max(max_total, current_sum)
        return max_total

    return max(get_max_subarray_sum(pulse1), get_max_subarray_sum(pulse2))