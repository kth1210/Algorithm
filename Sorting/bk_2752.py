import sys

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for idx in range(len(arr)):
    print(arr[idx], end=' ')