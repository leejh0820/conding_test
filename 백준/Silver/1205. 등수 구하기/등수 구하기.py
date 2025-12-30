import sys
N, grade, P = map(int, sys.stdin.readline().split())
scores = list(map(int,sys.stdin.readline().split()))

if N == 0:
    print(1)
else:
    if N == P and scores[-1] >= grade:
        print(-1)
    else:
        rank = 1
        for i in scores:
            if i > grade:
                rank += 1
            else:
                break
        print(rank)