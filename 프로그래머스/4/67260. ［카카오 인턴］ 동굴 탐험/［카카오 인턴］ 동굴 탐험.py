from collections import deque

def solution(n, path, order):
    adj = [[] for _ in range(n)]
    for u, v in path:
        adj[u].append(v)
        adj[v].append(u)
        
    key_to_lock = {a: b for a, b in order}
    lock_to_key = {b: a for a, b in order}

    if 0 in lock_to_key:
        return False

    visited = [False] * n
    waiting = [False] * n
    
    q = deque([0])
    visited[0] = True
    count = 0
    
    while q:
        curr = q.popleft()
        count += 1
        
        if curr in key_to_lock:
            lock = key_to_lock[curr]
            if waiting[lock]:
                visited[lock] = True
                q.append(lock)
            del lock_to_key[lock]
            
        for nxt in adj[curr]:
            if visited[nxt]:
                continue
                
            if nxt in lock_to_key:
                waiting[nxt] = True
            else:
                visited[nxt] = True
                q.append(nxt)
                
    return count == n