import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N  

for a in A:
    rem = a - B
    if rem > 0:
        ans += (rem + C - 1) // C  

print(ans)
