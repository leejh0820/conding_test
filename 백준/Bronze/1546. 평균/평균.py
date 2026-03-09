import sys
N = int(sys.stdin.readline())
grade = list(map(int, sys.stdin.readline().split()))

print(sum(grade)*100 / max(grade) / N)  