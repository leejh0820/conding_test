import sys
input_data = sys.stdin.read().split()

if input_data:
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        sides = sorted([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
        print((sides[0] + sides[1])**2 + sides[2]**2)
        
        idx += 3