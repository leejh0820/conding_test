import sys
n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
possible = True
num = 1

for i in range(n):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        top = stack.pop()
        if top > su:
            print("NO")
            possible = False
            break
        else:
            result.append('-')

if possible:
    print('\n'.join(result))