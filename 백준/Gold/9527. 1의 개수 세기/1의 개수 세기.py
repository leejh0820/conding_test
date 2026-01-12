import sys
memo = {0: 0}

def solve():
    data = sys.stdin.readline().split()
    if not data:
        return
    A, B = map(int, data)
    print(count(B) - count(A - 1))

def count(n):
    if n in memo:
        return memo[n]

    k = 0
    while (1 << (k + 1)) <= n:
        k += 1
    p = 1 << k

    if n == (p << 1) - 1:
        memo[n] = (k + 1) * p
        return memo[n]
    
    memo[n] = count(p - 1) + (n - p + 1) + count(n - p)
    
    return memo[n]

solve()