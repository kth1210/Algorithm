import sys

N, L = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for idx in range(N):
    if arr[idx] <= L:
        L += 1
    else:
        break

print(L)