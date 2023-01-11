import sys

def bin_search(arr, val, start, end):
    if arr[0] >= val:
        return 0

    result = 0

    while (start <= end):
        mid = (start + end) // 2

        if arr[mid] >= val:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    
    return result + 1

    


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    result = 0

    B.sort()

    for n in A:
        result += bin_search(B, n, 0, M - 1)
    
    print(result)
