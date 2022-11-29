import sys

N = int(sys.stdin.readline().rstrip())

arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline().rstrip())] += 1

for idx in range(1, 10001):
    if arr[idx] != 0:
        for _ in range(arr[idx]):
            print(idx)