import sys

def bin_search(fa, val, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if fa[mid] == val:
        return result[val]
    elif fa[mid] > val:
        return bin_search(fa, val, start, mid - 1)
    else:
        return bin_search(fa, val, mid + 1, end)


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().split()))

arr.sort()

result = {}

for n in arr:
    if n not in result:
        result[n] = 1
    else:
        result[n] += 1

for f in find:
    print(bin_search(arr, f, 0, len(arr) - 1), end = ' ')