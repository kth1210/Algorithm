import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    f, s = map(int, sys.stdin.readline().split())
    tree[f].append(s)
    tree[s].append(f)

def dfs(start, tree, parent):
    for node in tree[start]:
        if parent[node] == 0:
            parent[node] = start
            dfs(node, tree, parent)
        
dfs(1, tree, parent)

for idx in range(2, N+1):
    print(parent[idx])