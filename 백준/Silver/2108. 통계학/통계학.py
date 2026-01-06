import sys
from collections import Counter 

input = sys.stdin.readline
N = int(input())
numbers = list(int(input().strip()) for _ in range(N))
numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N//2])

cnt = Counter(numbers).most_common()
max_freq = cnt[0][1]
modes = [val for val, freq in cnt if freq == max_freq]
modes.sort()

if len(modes) > 1:
    print(modes[1]) 
else:
    print(modes[0])

print(numbers[-1] - numbers[0])