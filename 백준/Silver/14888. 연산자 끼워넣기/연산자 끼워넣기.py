import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_value = -10**9
min_value = 10**9

def cxx_div(a, b):
    if a < 0:
        return - (abs(a) // b)
    return a // b

def dfs(i, now):
    global max_value, min_value, add, sub, mul, div

    if i == N:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
        return

    if add > 0:
        add -= 1
        dfs(i + 1, now + data[i])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(i + 1, now - data[i])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(i + 1, now * data[i])
        mul += 1

    if div > 0:
        div -= 1
        dfs(i + 1, cxx_div(now, data[i]))
        div += 1

dfs(1, data[0])

print(max_value)
print(min_value)