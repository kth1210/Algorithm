import sys
from collections import deque

def DFS(graph, n, visited):
    visited[n] = True
    print(n, end= ' ')

    graph[n].sort()
    for i in graph[n]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for _ in range(M):
    f, s = map(int, sys.stdin.readline().split())
    
    graph[f].append(s)
    graph[s].append(f)

DFS(graph, V, visited_dfs)
print()
BFS(graph, V, visited_bfs)