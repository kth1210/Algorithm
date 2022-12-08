import sys
import heapq

N = int(sys.stdin.readline().rstrip())
lecture = []
room = []

for _ in range(N):
    s, t = list(map(int, sys.stdin.readline().split()))
    lecture.append([s, t])

lecture.sort()
heapq.heappush(room, lecture[0][1])

for idx in range(1, N):
    if lecture[idx][0] < room[0]:
        heapq.heappush(room, lecture[idx][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[idx][1])

print(len(room))