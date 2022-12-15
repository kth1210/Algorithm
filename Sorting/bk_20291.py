import sys

N = int(sys.stdin.readline().rstrip())
temp = {}

for _ in range(N):
    f, s = sys.stdin.readline().rstrip().split('.')
    
    if s not in temp:
        temp[s] = 1
    else:
        temp[s] += 1

arr = list(temp.items())
arr.sort(key = lambda x : x[0])

for idx in range(len(arr)):
    print(arr[idx][0], arr[idx][1])