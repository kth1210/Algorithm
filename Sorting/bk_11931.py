import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse = True)

for idx in range(N):
    print(arr[idx])