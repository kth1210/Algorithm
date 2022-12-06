import sys

N = int(sys.stdin.readline().rstrip())

arr = list(set(map(int, sys.stdin.readline().split())))

arr.sort()

for idx in range(len(arr)):
    print(arr[idx], end=' ')