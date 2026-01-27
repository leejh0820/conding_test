import sys

def main():
    N = int(sys.stdin.readline())
    dp = []

    for i in range(N):
        x, r = map(int, sys.stdin.readline().split())
        L = x - r
        R = x + r
        dp.append((L, 0, i))
        dp.append((R, 1, i))

    dp.sort()

    for k in range(1, len(dp)):
        if dp[k][0] == dp[k-1][0]:
            print("NO")
            return

    stack = []
    for pos, typ, idx in dp:
        if typ == 0:
            stack.append(idx)
        else:
            if not stack or stack[-1] != idx:
                print("NO")
                return
            stack.pop()

    print("YES")

main()