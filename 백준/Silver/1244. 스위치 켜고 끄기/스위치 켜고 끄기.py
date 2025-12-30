import sys
N = int(sys.stdin.readline())
status = [-1] + list(map(int, sys.stdin.readline().split()))
people = int(sys.stdin.readline())

for _ in range(people):
    student, switch = map(int, sys.stdin.readline().split())

    if student == 1:
        for i in range(switch, N+1, switch):
            status[i] = 1 - status[i]
    else:
        status[switch] = 1 - status[switch]
        offset = 1
        while (switch - offset) >= 1 and (switch + offset) <= N:
            if status[switch - offset] == status[switch + offset]:
                status[switch - offset] = 1 - status[switch - offset]
                status[switch + offset] = 1 - status[switch + offset]
                offset += 1
            else:
                break

for i in range(1, N + 1):
    print(status[i], end=" ")
    if i % 20 == 0:
        print()