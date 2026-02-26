import sys
N = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))
new_line = []
count = 1

for s in students:
    new_line.append(s)

    while new_line and new_line[-1] == count:
        new_line.pop()
        count += 1

if not new_line:
    print("Nice")
else:
    print("Sad")