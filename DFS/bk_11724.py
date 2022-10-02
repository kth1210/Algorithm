import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    if visited[v]:
        return False
    else:
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
        return True

for idx in range(1, N+1):
    if dfs(graph, idx, visited):
        result += 1

print(result)