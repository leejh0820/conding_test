import sys
from collections import deque
N = int(sys.stdin.readline())
cards = deque()

for i in range(1,N+1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])