import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().rstrip())
arr = []
sol = PriorityQueue()
result = 0


for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    arr.append([d, w])

arr.sort()
t = arr[N-1][0]

for day in range(t, 0, -1):
    while arr and arr[-1][0] >= day:
        sol.put(-arr.pop()[1])
    
    if not sol.empty():
        result += (-sol.get())

print(result)