import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

def calc(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    return a * b

def dfs(idx, val):
    if idx == N - 1:
        return val
    res = dfs(idx + 2, calc(val, S[idx+1], int(S[idx+2])))

    if idx + 4 <= N - 1:
        bracket = calc(int(S[idx+2]), S[idx+3], int(S[idx+4]))
        res = max(res, dfs(idx + 4, calc(val, S[idx+1], bracket)))
    
    return res

print(dfs(0, int(S[0])))