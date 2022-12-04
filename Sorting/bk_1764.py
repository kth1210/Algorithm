import sys

def binSearch(arr, val, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if arr[mid] > val:
        return binSearch(arr, val, start, mid - 1)
    elif arr[mid] < val:
        return binSearch(arr, val, mid + 1, end)
    else:
        return True

N, M = map(int, sys.stdin.readline().split())

A = []
B = []
result = []

for _ in range(N):
    A.append(sys.stdin.readline().rstrip())

for _ in range(M):
    B.append(sys.stdin.readline().rstrip())

A.sort()

for idx in range(M):
    if binSearch(A, B[idx], 0, N - 1):
        result.append(B[idx])

result.sort()

print(len(result))

for idx in range(len(result)):
    print(result[idx])