import sys

input = sys.stdin.readline
N = int(input())
S = set()

for _ in range(N):
    command = input().split()

    if command[0] == 'add':
        S.add(int(command[1]))
    
    elif command[0] == 'remove':
        S.discard(int(command[1]))
    
    elif command[0] == 'check':
        x = int(command[1])
        if x in S:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'toggle':
        x = int(command[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    
    elif command[0] == 'all':
        S = set(range(1, 21))
    
    elif command[0] == 'empty':
        S.clear()