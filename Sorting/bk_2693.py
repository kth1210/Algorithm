import sys

N = int(sys.stdin.readline().rstrip())
result = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)
    result.append(arr[2])
    arr.clear()

for idx in range(N):
    print(result[idx])