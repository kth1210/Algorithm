import sys

N = int(sys.stdin.readline().rstrip())
arr = {}

for _ in range(N):
    f, s = sys.stdin.readline().split('.')
    
    if s not in arr:
        arr[s] = 1
    else:
        arr[s] += 1

arr.sort()

for idx in range(N):
    
