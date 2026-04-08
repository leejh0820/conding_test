import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
cards = PriorityQueue()

for _ in range(N):
    card = int(sys.stdin.readline())
    cards.put(card)

card1 = 0
card2 = 0
answer = 0

while cards.qsize()>1:
    card1 = cards.get()
    card2 = cards.get()
    temp = card1 + card2
    answer += temp
    cards.put(temp)

print(answer)
