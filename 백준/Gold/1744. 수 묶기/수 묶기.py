import sys
N = int(sys.stdin.readline())

plus = []
minus = []
one = 0
total_sum = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        plus.append(num)
    elif num == 1:
        one += 1
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()
        
for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        total_sum += (plus[i] * plus[i+1])
    else:
        total_sum += plus[i]

for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        total_sum += (minus[i] * minus[i+1])
    else:
        total_sum += minus[i]

total_sum += one

print(total_sum)
