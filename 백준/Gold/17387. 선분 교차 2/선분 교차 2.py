import sys

def ccw(p1, p2, p3):
    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if val < 0: return -1
    if val > 0: return 1
    return 0

def solve():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

    A, B = (x1, y1), (x2, y2)
    C, D = (x3, y3), (x4, y4)

    L1 = ccw(A, B, C) * ccw(A, B, D)
    L2 = ccw(C, D, A) * ccw(C, D, B)

    if L1 <= 0 and L2 <= 0:
        if L1 == 0 and L2 == 0:
            if min(A[0], B[0]) <= max(C[0], D[0]) and min(C[0], D[0]) <= max(A[0], B[0]) and \
               min(A[1], B[1]) <= max(C[1], D[1]) and min(C[1], D[1]) <= max(A[1], B[1]):
                return 1
            else:
                return 0
        return 1
    return 0
    
print(solve())