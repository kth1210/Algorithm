import sys

N, H = map(int, sys.stdin.readline().split())

bottom = []
top = []

for idx in range(N):
    if idx % 2 == 0:
        bottom.append(int(sys.stdin.readline().rstrip()))
    else:
        top.append(int(sys.stdin.readline().rstrip()))

# print(odd)
# print(even)

bottom.sort()
top.sort()
# print(bottom)
# print(top)

result_val = float("inf")
result_cnt = 0

def bin_search(arr, val, start, end):
    result = val
    while (start <= end):
        mid = (start + end) // 2

        if arr[mid] < val:
            # end = mid - 1
            result = mid
            start = mid + 1
        elif arr[mid] == val:
            return mid + 1
        else:
            # result = mid
            # start = mid + 1
            end = mid - 1
    return result

# print()
for idx in range(1, H+1):
    val = bin_search(bottom, idx, 0, N//2 - 1) + bin_search(top, H-idx+1, 0, N//2 - 1)
    # print(val)
    
    if result_val > val:
        result_val = val
        result_cnt = 1
    elif result_val == val:
        result_cnt += 1

print(result_val, result_cnt)



    