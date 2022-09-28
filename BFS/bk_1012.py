import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
result = []

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]
    temp = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def bfs(x, y):
        queue = deque()

        if graph[y][x] == 0:
            return False
        elif graph[y][x] > 1:
            return False

        queue.append((x, y))

        while queue:
            curX, curY = queue.popleft()

            for idx in range(4):
                nextX = curX + dx[idx]
                nextY = curY + dy[idx]

                if nextX < 0 or nextX >= M or nextY < 0 or nextY >= N:
                    continue
                else:
                    if graph[nextY][nextX] == 0:
                        continue
                    elif graph[nextY][nextX] == 1:
                        graph[nextY][nextX] = graph[curY][curX] + 1
                        queue.append((nextX, nextY))

        return True    
        
    for i in range(N):
        for j in range(M):
            if bfs(j, i):
                temp += 1
    result.append(temp)
    graph.clear()
    temp = 0

for idx in range(T):
    print(result[idx])