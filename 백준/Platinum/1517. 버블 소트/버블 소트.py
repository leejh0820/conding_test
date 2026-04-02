import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def merge_sort(start, end):
    global swap_count
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        
        temp = []
        i, j = start, mid + 1
        
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                swap_count += (mid - i + 1)
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= end:
            temp.append(arr[j])
            j += 1
            
        for k in range(len(temp)):
            arr[start + k] = temp[k]

swap_count = 0
merge_sort(0, N - 1)
print(swap_count)