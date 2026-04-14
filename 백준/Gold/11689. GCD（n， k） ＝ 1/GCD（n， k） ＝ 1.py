import sys
line = sys.stdin.readline().strip()
n = int(line)
    
result = n
p = 2
temp = n
    
while p * p <= temp:
    if temp % p == 0:
        result -= result // p
        while temp % p == 0:
            temp //= p
    p += 1
    
if temp > 1:
    result -= result // temp
        
print(result)