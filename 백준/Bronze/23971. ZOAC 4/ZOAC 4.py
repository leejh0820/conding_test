import sys
H, W, N, M = map(int,sys.stdin.readline().split())
row = (H + (N + 1) - 1) // (N + 1)
col = (W + (M + 1) - 1) // (M + 1)
print(row*col)