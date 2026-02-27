import sys
N = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
result = 0
cost = price[0]

for i in range(N-1):
    if price[i] < cost:
        cost = price[i]
    
    result += cost * d[i]

print(result)