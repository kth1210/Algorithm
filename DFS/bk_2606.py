import re
import sys

def dfs(graph, v, visited, result):
    visited[v] = True
    result += 1

    for i in graph[v]:
        if not visited[i]:
            result = dfs(graph, i, visited, result)

    return result

Com = int(sys.stdin.readline().rstrip())
Net = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(Com+1)]
visited = [False] * (Com+1)
result = 0

for _ in range(Net):
    f, s = map(int, sys.stdin.readline().split())
    graph[f].append(s)
    graph[s].append(f)

print(dfs(graph, 1, visited, result) - 1)