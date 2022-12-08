import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

scope = 0

for idx in range(N):
    if arr[idx] <= scope + 1:
        scope += arr[idx]
    else:
        break

print(scope + 1)