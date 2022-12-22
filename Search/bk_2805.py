import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

start = 0
end = tree[len(tree) - 1]
result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2

    for t in tree:
        if t > mid:
            total += t - mid

    if total < M:
        end = mid - 1
    elif total == M:
        result = mid
        break
    else:
        result = mid
        start = mid + 1

print(result)