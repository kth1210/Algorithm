import sys

N = int(sys.stdin.readline().rstrip())
result = {}

arr = list(map(int, sys.stdin.readline().split()))
temp = list(set(arr))
temp.sort()

for idx in range(len(temp)):
    result[temp[idx]] = idx

for idx in range(N):
    print(result[arr[idx]], end=' ')