import sys

N = int(sys.stdin.readline().rstrip())
temp = []

for _ in range(N):
    temp.append(sys.stdin.readline().rstrip())

arr = list(set(temp))

arr.sort()
arr.sort(key=len)

for idx in range(len(arr)):
    print(arr[idx])