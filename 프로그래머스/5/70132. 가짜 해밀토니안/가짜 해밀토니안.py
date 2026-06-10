import sys
sys.setrecursionlimit(300000)

def solution(t):
    n = len(t) + 1
    adj = [[] for _ in range(n)]
    
    for u, v in t:
        adj[u].append(v)
        adj[v].append(u)

    depth = [0] * n  
    dp = [0] * n     
    top3_depth = [[] for _ in range(n)]

    def dfs1(u, p):
        for v in adj[u]:
            if v != p:
                dfs1(v, u)
                depth[u] = max(depth[u], depth[v] + 1)
                top3_depth[u].append((depth[v] + 1, v))

        top3_depth[u].sort(reverse=True, key=lambda x: x[0])
        top3_depth[u] = top3_depth[u][:3]

        def max_exc(ex):
            for val, nxt in top3_depth[u]:
                if nxt != ex: return val
            return 0

        dp[u] = 1 + (top3_depth[u][0][0] if top3_depth[u] else 0)
        for v in adj[u]:
            if v != p:
                dp[u] = max(dp[u], dp[v] + 1 + max_exc(v))

    dfs1(0, -1)

    ans = 0

    def dfs2(u, p, out_depth):
        nonlocal ans

        def max_exc(ex1, ex2=-1):
            for val, nxt in top3_depth[u]:
                if nxt != ex1 and nxt != ex2: return val
            return 0

        ans = max(ans, 1 + max(out_depth, top3_depth[u][0][0] if top3_depth[u] else 0))

        for v in adj[u]:
            if v != p:
                ans = max(ans, dp[v] + 1 + max(out_depth, max_exc(v)))

        dp_children = sorted([(dp[v], v) for v in adj[u] if v != p], reverse=True, key=lambda x: x[0])[:3]
        cands = list(set([c for _, c in top3_depth[u]] + [c for _, c in dp_children]))
        
        for i in range(len(cands)):
            for j in range(i + 1, len(cands)):
                c1, c2 = cands[i], cands[j]
                ans = max(ans, dp[c1] + dp[c2] + 1 + max(out_depth, max_exc(c1, c2)))

        for v in adj[u]:
            if v != p:
                dfs2(v, u, max(out_depth, max_exc(v)) + 1)

    dfs2(0, -1, 0)

    return ans