import sys

arr = list(map(int, sys.stdin.readline().split()))
S = 0

for idx in range(len(arr)):
    S += arr[idx] ** 2

print(S % 10)