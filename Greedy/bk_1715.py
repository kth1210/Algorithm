import sys
import heapq

N = int(sys.stdin.readline().rstrip())
size = []
sum = 0
result = 0

for _ in range(N):
    heapq.heappush(size, int(sys.stdin.readline().rstrip()))

if len(size) == 1:
    print('0')
else :
    while len(size) > 1:
        sum = heapq.heappop(size) + heapq.heappop(size)
        result += sum
        heapq.heappush(size, sum)
    
    print(result)