import sys
times = sys.stdin.readline().strip().split(':')
nums = [int(x) for x in times]

cases = [
    (nums[0], nums[1], nums[2]),
    (nums[0], nums[2], nums[1]),
    (nums[1], nums[0], nums[2]),
    (nums[1], nums[2], nums[0]),
    (nums[2], nums[0], nums[1]),
    (nums[2], nums[1], nums[0])
]

count = 0
for h, m, s in cases:
    if 1 <= h <= 12 and 0 <= m <= 59 and 0 <= s <= 59:
        count += 1

print(count)