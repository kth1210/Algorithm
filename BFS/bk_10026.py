import sys
import copy
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
dup = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

dup = copy.deepcopy(graph)

def normalBfs(x, y):
    queue = deque()
    if graph[x][y] != 0:
        queue.append([x, y])
        curC = graph[x][y]
        
        while queue:
            curX, curY = queue.popleft()

            for idx in range(4):
                nextX = curX + dx[idx]
                nextY = curY + dy[idx]

                if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                    continue
                
                if graph[nextX][nextY] == curC:
                    graph[nextX][nextY] = 0
                    queue.append([nextX, nextY])
        return True
    else:
        return False

def colorBfs(x,y):
    queue = deque()
    if dup[x][y] != 0:
        queue.append([x, y])
        curC = dup[x][y]
        
        while queue:
            curX, curY = queue.popleft()

            for idx in range(4):
                nextX = curX + dx[idx]
                nextY = curY + dy[idx]

                if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                    continue
                
                if curC == "R" or curC == "G":
                    if dup[nextX][nextY] == "R" or dup[nextX][nextY] == "G":
                        dup[nextX][nextY] = 0
                        queue.append([nextX, nextY])
                elif curC == "B":
                    if dup[nextX][nextY] == curC:
                        dup[nextX][nextY] = 0
                        queue.append([nextX, nextY])
        return True
    else:
        return False

normalResult = 0
colorResult = 0    
for i in range(N):
    for j in range(N):
        if normalBfs(i, j):
            normalResult += 1
        
        if colorBfs(i, j):
            colorResult += 1

print(normalResult)
print(colorResult)
