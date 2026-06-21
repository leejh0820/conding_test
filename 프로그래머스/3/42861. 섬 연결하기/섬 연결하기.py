def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x: x[2])
    p = list(range(n))

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    for u, v, c in costs:
        r1, r2 = find(u), find(v)
        if r1 != r2:
            p[r2] = r1
            answer += c
            
    return answer
