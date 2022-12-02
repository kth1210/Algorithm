import sys

def binSearch(arr, val, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if arr[mid] > val:
        return binSearch(arr, val, start, mid - 1)
    elif arr[mid] < val:
        return binSearch(arr, val, mid + 1, end)
    else:
        return 1

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

for idx in range(M):
    print(binSearch(A, B[idx], 0, N-1), end=' ')
