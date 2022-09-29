import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
queue = deque()
flag = True
max = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        curX, curY = queue.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= M:
                continue

            if graph[nextX][nextY] == 0:
                graph[nextX][nextY] = graph[curX][curY] + 1
                queue.append([nextX, nextY])

bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = False
        
        if max <= graph[i][j]:
            max = graph[i][j]

if flag:
    print(max - 1)
else:
    print('-1')