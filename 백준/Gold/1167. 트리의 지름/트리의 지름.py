import sys
sys.setrecursionlimit(10 ** 9)
V = int(sys.stdin.readline())
tree = [[] for _ in range(V+1)]

visited = [-1]*(V+1)
visited[1] = 0

for _ in range(V):
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(nums)-2, 2):
        tree[nums[0]].append((nums[i], nums[i + 1]))

def dfs(start, distance):
    for a, b in tree[start]:
        if visited[a] == -1:
            visited[a] = distance + b
            dfs(a, distance + b)
dfs(1,0)

last_Node = visited.index(max(visited))
visited = [-1] * (V + 1)
visited[last_Node] = 0
dfs(last_Node, 0)

print(max(visited))