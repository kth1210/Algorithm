import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for idx in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        curX, curY = queue.popleft()

        for idx in range(4):
            nextX = curX + dx[idx]
            nextY = curY + dy[idx]

            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= M:
                continue
            else:
                if graph[nextX][nextY] == 0:
                    continue
                elif graph[nextX][nextY] == 1:
                    graph[nextX][nextY] = graph[curX][curY] + 1
                    queue.append((nextX, nextY))

bfs()
print(graph[N-1][M-1])