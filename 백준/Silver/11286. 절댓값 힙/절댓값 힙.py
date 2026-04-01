import heapq
import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
commands = input_data[1:]

abs_heap = []
output = []

for i in range(N):
    x = int(commands[i])
    
    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if not abs_heap:
            output.append("0")
        else:
            output.append(str(heapq.heappop(abs_heap)[1]))

sys.stdout.write("\n".join(output) + "\n")