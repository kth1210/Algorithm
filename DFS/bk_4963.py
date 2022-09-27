import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, graph, w, h):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x, y+1, graph, w, h)
        dfs(x+1, y, graph, w, h)
        dfs(x, y-1, graph, w, h)
        dfs(x-1, y, graph, w, h)
        
        dfs(x+1, y+1, graph, w, h)
        dfs(x+1, y-1, graph, w, h)
        dfs(x-1, y-1, graph, w, h)
        dfs(x-1, y+1, graph, w, h)
        return True
    else:
        return False

result = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    graph = []
    cnt = 0

    if w == 0 and h == 0:
        break

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph, w, h):
                cnt += 1
    result.append(cnt)
    graph.clear()
    
for idx in range(len(result)):
    print(result[idx])