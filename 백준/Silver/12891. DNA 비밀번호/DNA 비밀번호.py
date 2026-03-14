import sys

s_len, p_len = map(int, sys.stdin.readline().split())
dna_str = sys.stdin.readline().strip()
min_counts = list(map(int, sys.stdin.readline().split())) 

current_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
check_bits = 0 
def add_char(char):
    global check_bits
    current_counts[char] += 1
    idx = 'ACGT'.find(char)
    if current_counts[char] == min_counts[idx]:
        check_bits += 1

def remove_char(char):
    global check_bits
    idx = 'ACGT'.find(char)
    if current_counts[char] == min_counts[idx]:
        check_bits -= 1
    current_counts[char] -= 1

for i in range(4):
    if min_counts[i] == 0:
        check_bits += 1

for i in range(p_len):
    add_char(dna_str[i])

result = 0
if check_bits == 4:
    result += 1

for i in range(p_len, s_len):
    j = i - p_len 
    add_char(dna_str[i])    
    remove_char(dna_str[j]) 
    
    if check_bits == 4:
        result += 1

print(result)