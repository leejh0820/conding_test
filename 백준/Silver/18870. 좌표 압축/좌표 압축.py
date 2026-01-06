import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
sort_numbers = sorted(list(set(numbers)))

new_numbers = {val: i for i, val in enumerate(sort_numbers)}

for x in numbers:
    sys.stdout.write(str(new_numbers[x]) + " ")