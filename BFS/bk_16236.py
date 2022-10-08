import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
sharkX = 0
sharkY = 0
dx = []
dy = []

for idx in range(N):
    temp = map(int, sys.stdin.readline().split())
    if 9 in temp:
        sharkX = idx
        sharkY = temp.index(9)

def bfs(sharkX, sharkY, graph):
    queue = deque((sharkX, sharkY))
    
    while queue:
        curX, curY = queue.popleft()
