import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ai = []
bi = []

if n > 0:
    ai = list(map(int, input().split()))
else:
    input().strip()

if m > 0:
    bi = list(map(int, input().split()))

ai.sort(reverse=True)
bi.sort(reverse=True)

A, B = 1, 0
i, j = 0, 0

while True:
    while B > 0 and j < m:
        B -= 1
        A += bi[j]
        j += 1

    if B == 0 and i < n and A > 0 and j < m:
        A -= 1
        B += ai[i]
        i += 1
        continue
    break

print(A)