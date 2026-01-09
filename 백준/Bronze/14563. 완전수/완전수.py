import sys
T = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for n in numbers:
    if n == 1:
        print ("Deficient")
        continue
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    
    if result == n:
        print("Perfect")
    elif result < n:
        print("Deficient")
    else:
        print("Abundant")