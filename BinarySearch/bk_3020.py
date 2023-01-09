import sys

def bin_search(arr, val, start, end):
    result = len(arr)
    while (start <= end):
        mid = (start + end) // 2

        if arr[mid] < val:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    return result

N, H = map(int, sys.stdin.readline().split())

bottom = []
top = []

for idx in range(N):
    if idx % 2 == 0:
        bottom.append(int(sys.stdin.readline().rstrip()))
    else:
        top.append(int(sys.stdin.readline().rstrip()))

bottom.sort()
top.sort()

result_val = float("inf")
result_cnt = 0

for idx in range(1, H+1):
    val = bin_search(bottom, idx, 0, N//2 - 1) + bin_search(top, H-idx+1, 0, N//2 - 1)

    val = N - val
    if result_val > val:
        result_val = val
        result_cnt = 1
    elif result_val == val:
        result_cnt += 1

print(result_val, result_cnt)