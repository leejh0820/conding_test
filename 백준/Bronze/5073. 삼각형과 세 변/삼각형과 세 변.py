import sys

while True:
    sides = list(map(int, sys.stdin.readline().split()))
    sides.sort()

    if sum(sides) == 0:
        break
    
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    
    else:
        distinct_sides = len(set(sides))
        
        if distinct_sides == 1:
            print("Equilateral")
        elif distinct_sides == 2:
            print("Isosceles")
        else:
            print("Scalene")