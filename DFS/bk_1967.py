import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().split())

    graph[p].append([c, w])
    graph[c].append([p, w])

def dfs(start, graph, weight):
    for node, wei in graph[start]:
        if weight[node] == -1:
            weight[node] = weight[start] + wei
            dfs(node, graph, weight)

weight = [-1] * (N+1)
weight[1] = 0
dfs(1, graph, weight)

start = weight.index(max(weight))

weight = [-1] * (N+1)
weight[start] = 0
dfs(start, graph, weight)

result = max(weight)
print(result)