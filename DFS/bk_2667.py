import sys

N = int(sys.stdin.readline().rstrip())
graph = []
result = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y, cnt):
    if x < 0 or x >= N or y < 0 or y >= N:
        return cnt
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt = dfs(x+1, y, cnt)
        cnt = dfs(x, y+1, cnt)
        cnt = dfs(x-1, y, cnt)
        cnt = dfs(x, y-1, cnt)

        cnt += 1
        return cnt
    else:
        return cnt

result = []
cnt = 0
for i in range(N):
    for j in range(N):
        t = dfs(i, j, cnt)
        if t > 0:
            result.append(t)
result.sort()
print(len(result))
for idx in range(len(result)):
    print(result[idx])