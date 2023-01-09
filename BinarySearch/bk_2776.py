import sys

def bin_search(arr, val, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if arr[mid] < val:
        return bin_search(arr, val, mid + 1, end)
    elif arr[mid] == val:
        return 1
    else:
        return bin_search(arr, val, start, mid - 1)

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr_one = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline().rstrip())
    arr_two = list(map(int, sys.stdin.readline().split()))

    arr_one.sort()

    for v in arr_two:
        print(bin_search(arr_one, v, 0, N - 1))

