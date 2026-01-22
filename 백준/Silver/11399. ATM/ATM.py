import sys
N = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))
people.sort()
answer = 0

for i in range(N):
    answer += people[i] * (N-i)

print(answer)