N = int(input())
count = 1
index_1 = 1
index_2 = 1
total = 1

while index_2 != N:
    if total == N:
        count += 1
        index_2 += 1
        total += index_2
    
    elif total > N:
        total -= index_1
        index_1 += 1
    
    else:
        index_2 += 1
        total += index_2

print(count)