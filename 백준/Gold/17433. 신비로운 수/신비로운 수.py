import sys
import math

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    out = []
    for _ in range(T):
        N = int(input().strip())
        arr = list(map(int, input().split()))

        if all(x == arr[0] for x in arr):
            out.append("INFINITY")
            continue

        base = arr[0]
        g = 0
        for x in arr[1:]:
            g = math.gcd(g, abs(x - base))

        out.append(str(g))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
