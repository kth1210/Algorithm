import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

arr.sort(key=lambda x: (x[0], x[1]))

for idx in range(N):
    print(arr[idx][0], arr[idx][1])