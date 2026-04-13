import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())

    max_n = 10000000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    count = 0
    
    for p in primes:
        temp = p * p 
        while temp <= B:
            if temp >= A:
                count += 1
            
            if temp > B / p: 
                break
            temp *= p
            
    print(count)

solve()