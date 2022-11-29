import sys

N = sys.stdin.readline().rstrip()
arr = []

for num in N:
    arr.append(int(num))

arr.sort(reverse=True)

for idx in range(len(arr)):
    print(arr[idx], end='')