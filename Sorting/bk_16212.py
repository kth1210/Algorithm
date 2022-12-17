import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

for idx in range(N):
    print(arr[idx], end = ' ')