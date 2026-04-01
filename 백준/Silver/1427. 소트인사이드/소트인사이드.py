import sys
N = sys.stdin.read().strip()
numbers = sorted(list(N), reverse = True)
print("".join(numbers))