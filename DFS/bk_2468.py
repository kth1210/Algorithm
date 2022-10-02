import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline().rstrip())
graph = []
visited = [[False] * N for _ in range(N)]
maxDepth = 0

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if maxDepth <= max(temp):
        maxDepth = max(temp)
    graph.append(temp)

def dfs(graph, x, y, depth, visited):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if visited[x][y] or graph[x][y] <= depth:
        return False
    else:
        visited[x][y] = True

        dfs(graph, x, y+1, depth, visited)
        dfs(graph, x+1, y, depth, visited)
        dfs(graph, x, y-1, depth, visited)
        dfs(graph, x-1, y, depth, visited)

        return True

result = []
cnt = 0
for depth in range(maxDepth):
    for i in range(N):
        for j in range(N):
            if dfs(graph, i, j, depth, visited):
                cnt += 1
    result.append(cnt)
    cnt = 0
    visited = [[False] * N for _ in range(N)]

print(max(result))