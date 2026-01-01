import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

ptr = 0
t_str = input_data[ptr]
ptr += 1
t = int(t_str)

for _ in range(t):
    n = int(input_data[ptr])
    m = int(input_data[ptr+1])
    ptr += 2
    
    max_r = 0
    max_w = 0
    
    for _ in range(m):
        r = int(input_data[ptr])
        w = int(input_data[ptr+1])
        ptr += 2
        
        if r > max_r: max_r = r
        if w > max_w: max_w = w
            
    if max_r + max_w > n:
        print("IMPOSSIBLE")
    else:
        print('R' * max_r + 'W' * (n - max_r))