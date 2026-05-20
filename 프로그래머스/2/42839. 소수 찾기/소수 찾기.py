from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    unique_numbers = set()
    
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            unique_numbers.add(num)
            
    answer = 0
    for num in unique_numbers:
        if is_prime(num):
            answer += 1
            
    return answer