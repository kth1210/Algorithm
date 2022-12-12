import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse = True)

for idx in range(len(arr)):
    arr[idx] += idx + 1

arr.sort(reverse = True)
print(arr[0] + 1)