import sys

N_str = sys.stdin.readline().strip()
N = int(N_str)

full_string = "".join(str(i) for i in range(1, N + 1))
print(full_string.find(N_str) + 1)