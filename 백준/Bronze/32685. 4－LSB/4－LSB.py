import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

res = ((a & 15) << 8) | ((b & 15) << 4) | (c & 15)

print(f"{res:04d}")