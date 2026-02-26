import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A += [0, 0]  

cost = 0
for i in range(N):
    if A[i+1] > A[i+2]:
        x = min(A[i], A[i+1] - A[i+2])
        A[i] -= x
        A[i+1] -= x
        cost += 5 * x

        y = min(A[i], A[i+1], A[i+2])
        A[i] -= y
        A[i+1] -= y
        A[i+2] -= y
        cost += 7 * y
    else:
        y = min(A[i], A[i+1], A[i+2])
        A[i] -= y
        A[i+1] -= y
        A[i+2] -= y
        cost += 7 * y

        x = min(A[i], A[i+1])
        A[i] -= x
        A[i+1] -= x
        cost += 5 * x

    cost += 3 * A[i]
    A[i] = 0
    
print(cost)