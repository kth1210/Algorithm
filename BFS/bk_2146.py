import sys
from collections import deque
from tabnanny import check
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline().rstrip())
graph = []
visited = [[False] * N for _ in range(N)]
weight = 2
result = sys.maxsize

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y, weight, visited):
    graph[x][y] = weight
    visited[x][y] = True

    for idx in range(4):
        nextX = x + dx[idx]
        nextY = y + dy[idx]

        if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
            continue
            
        if graph[nextX][nextY] == 1:
            dfs(nextX, nextY, weight, visited)


def bfs(weight):
    global result

    queue = deque()
    visited = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == weight:
                queue.append([i, j])
                visited[i][j] = 0

    while queue:
        curX, curY = queue.popleft()

        for idx in range(4):
            nextX = curX + dx[idx]
            nextY = curY + dy[idx]

            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                continue
            
            if graph[nextX][nextY] != weight and graph[nextX][nextY] != 0:
                if result >= visited[curX][curY]:
                    result = visited[curX][curY]
                    return
            
            if graph[nextX][nextY] == 0 and visited[nextX][nextY] == -1:
                visited[nextX][nextY] = visited[curX][curY] + 1
                queue.append([nextX, nextY])


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            weight += 1
            dfs(i, j, weight, visited)
        
for w in range(2, weight):
    bfs(w)

print(result)