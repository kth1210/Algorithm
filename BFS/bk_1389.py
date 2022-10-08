import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    f, s = map(int, sys.stdin.readline().split())
    graph[f].append(s)
    graph[s].append(f)

def bfs(start, end, graph, visited):
    if start == end:
        return 0

    queue = deque([start])

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if next == end:
                return visited[cur] + 1

            if visited[next] == 0:
                visited[next] = visited[cur] + 1
                queue.append(next)
    return 0

result = []
for start in range(1, N+1):
    bacon = 0

    for end in range(1, N+1):
        visited = [0] * (N+1)
        bacon += bfs(start, end, graph, visited)
    
    result.append(bacon)

print(result.index(min(result)) + 1)