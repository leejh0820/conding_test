import sys
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse = True)
answer = 0

for coin in coins:
    if K >= coin:
        answer += K // coin
        K %= coin
        if K <= 0:
            break

print(answer)