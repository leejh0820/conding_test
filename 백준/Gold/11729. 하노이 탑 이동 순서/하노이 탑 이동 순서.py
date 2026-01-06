import sys
N = int(sys.stdin.readline())

def hanoi(n, start, end, sub):
    if n == 1:
        print(f"{start} {end}")
        return

    hanoi(n-1, start, sub, end)
    print(f"{start} {end}")

    hanoi(n-1, sub, end, start)
            
print(2**N - 1)
hanoi(N, 1, 3, 2)