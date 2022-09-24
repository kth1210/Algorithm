import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
bag = []
result = 0

for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jew, (M, V))

for _ in range(K):
    val = int(sys.stdin.readline().rstrip())
    heapq.heappush(bag, val)

capable = []
for _ in range(K):
    cur_bag = heapq.heappop(bag)

    while jew and cur_bag >= jew[0][0]:
        heapq.heappush(capable, -(heapq.heappop(jew)[1]))
    
    if capable:
        result -= heapq.heappop(capable)

print(result)
