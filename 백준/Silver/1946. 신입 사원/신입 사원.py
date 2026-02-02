import sys

def solve():
    N = int(sys.stdin.readline())
    candidates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    candidates.sort()

    count = 1
    min_interview = candidates[0][1]

    for i in range(1, N):
        if candidates[i][1] < min_interview:
            count += 1
            min_interview = candidates[i][1]

    print(count)

T = int(sys.stdin.readline())
for _ in range(T):
    solve()