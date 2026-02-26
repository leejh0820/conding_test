import sys
equation = sys.stdin.readline().strip().split('-')
result = 0

for num in equation[0].split('+'):
    result += int(num)

for i in range(1, len(equation)):
    answer = sum(map(int, equation[i].split('+')))
    result -= answer

print(result)