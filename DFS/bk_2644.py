import sys

N = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
val = [0] * (N+1)

for _ in range(M):
    p, c = map(int, sys.stdin.readline().split())
    graph[p].append(c)
    graph[c].append(p)

def dfs(start):
    for i in graph[start]:
        if val[i] == 0:
            val[i] = val[start] + 1
            dfs(i)

dfs(a)
if val[b] == 0:
    print("-1")
else:
    print(val[b])