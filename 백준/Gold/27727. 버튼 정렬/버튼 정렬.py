import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
K = int(input().strip())

if N == 1:
    print(K)
    sys.exit(0)

if N == 2:
    x, y = A[0], A[1]
    if x <= y:
        d = y - x
        if K <= d:
            print(K)
        else:
            print(d + (K - d) // 2)
    else:
        d = x - y
        if K < d:
            print(0)
        else:
            print(1 + (K - d) // 2)
    sys.exit(0)

ans = 0
sorted0 = True
for i in range(N - 1):
    if A[i] > A[i + 1]:
        sorted0 = False
        break

if sorted0 and A[0] < A[1]:
    t = min(K, A[1] - A[0])
    ans += t
    K -= t
    A[0] += t
    if K == 0:
        print(ans)
        sys.exit(0)

nodes = [(A[i], i) for i in range(N)]
nodes.sort()

curK = 0
asc = 0

startInd = 1
for i in range(N - 1, 1, -1):
    if nodes[i][1] != i:
        startInd = i
        break

target = nodes[startInd][0]
for i in range(startInd):
    curK += target - nodes[i][0]
    if curK > K:
        print(ans + asc)
        sys.exit(0)

if curK > 0:
    asc += 1

nextInd = startInd + 1
while nextInd < N:
    if nodes[nextInd - 1][0] != nodes[nextInd][0]:
        diff = nodes[nextInd][0] - nodes[nextInd - 1][0]
        need = nextInd * diff
        if curK + need > K:
            break
        curK += need
        asc += diff
    nextInd += 1

asc += (K - curK) // nextInd
print(ans + asc)