import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

arr.sort()
low = 0
high = arr[-1]
mid = 0
max_budget = 0

S = sum(arr)

if S <= M:
    print(high)
else:
    while low <= high:
        S = 0
        mid = (low + high) // 2

        for val in arr:
            if val > mid:
                S += mid
            else:
                S += val
        
        if S > M:
            high = mid - 1
        else:
            max_budget = mid
            low = mid + 1
    
    print(max_budget)
