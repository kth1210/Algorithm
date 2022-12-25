import sys

N, X = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for idx in range(N):
    if arr[idx] < X:
        print(arr[idx], end = ' ')