import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []

temp = list(map(int, sys.stdin.readline().split()))

for idx in range(N):
    heapq.heappush(arr, temp[idx])

for _ in range(1, N):
    temp = list(map(int, sys.stdin.readline().split()))

    for val in temp:
        if val > arr[0]:
            heapq.heappop(arr)
            heapq.heappush(arr, val)

print(arr[0])