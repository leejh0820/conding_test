def solution(edges, target):
    n = len(target)
    
    adj = [[] for _ in range(n + 1)]
    for parent, child in edges:
        adj[parent].append(child)
        
    for i in range(1, n + 1):
        adj[i].sort()
        
    cur_turn = [0] * (n + 1)
    
    history = []
    count = [0] * (n + 1)
    
    leaf_nodes = [i for i in range(1, n + 1) if not adj[i]]
    
    while True:
        curr = 1
        while adj[curr]:
            turn = cur_turn[curr]
            next_node = adj[curr][turn]
            
            cur_turn[curr] = (turn + 1) % len(adj[curr])
            curr = next_node
            
        history.append(curr)
        count[curr] += 1
        
        is_ok = True
        is_fail = False
        
        for leaf in leaf_nodes:
            if count[leaf] * 3 < target[leaf - 1]:
                is_ok = False
            if count[leaf] > target[leaf - 1]:
                is_fail = True
                break
                
        if is_fail:
            return [-1]
        if is_ok:
            break
            
    answer = []
    for leaf in history:
        count[leaf] -= 1
        
        for val in [1, 2, 3]:
            rem_target = target[leaf - 1] - val
            if count[leaf] <= rem_target <= count[leaf] * 3:
                answer.append(val)
                target[leaf - 1] = rem_target
                break
                
    return answer