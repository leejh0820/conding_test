def solution(s):
    if len(s) < 2 or s == s[::-1]:
        return len(s)

    max_len = 1
    n = len(s)

    for i in range(n - 1):
        left = i
        right = i
        
        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1
            
            if current_len > max_len:
                max_len = current_len
                
            left -= 1
            right += 1

        left = i
        right = i + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1
            
            if current_len > max_len:
                max_len = current_len
                
            left -= 1
            right += 1

    return max_len