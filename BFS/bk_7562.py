import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(curX, curY, board, resultX, resultY, L):
    queue = deque()
    queue.append([curX, curY])

    if curX == resultX and curY == resultY:
        return board[curX][curY]

    while queue:
        x, y = queue.popleft()

        for idx in range(8):
            nextX = x + dx[idx]
            nextY = y + dy[idx]

            if nextX < 0 or nextX >= L or nextY < 0 or nextY >= L:
                continue
            
            if nextX == resultX and nextY == resultY:
                return board[x][y] + 1
            
            if board[nextX][nextY] == 0:
                board[nextX][nextY] = board[x][y] + 1
                queue.append([nextX, nextY])

result = []
for _ in range(T):
    L = int(sys.stdin.readline())
    board = [[0] * L for _ in range(L)]
    curX, curY = map(int, sys.stdin.readline().split())
    resultX, resultY = map(int, sys.stdin.readline().split())
    
    result.append(bfs(curX, curY, board, resultX, resultY, L))

for i in range(T):
    print(result[i])