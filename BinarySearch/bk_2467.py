import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

answer = float("inf")
left_answer = 0
right_answer = N - 1

for idx in range(N - 1):
    low = idx + 1
    high = N - 1

    while low <= high:
        mid = (low + high) // 2
        temp = arr[mid] + arr[idx]

        if abs(temp) < answer:
            left_answer = idx
            right_answer = mid
            answer = abs(temp)
        
        if temp == 0:
            break
        elif temp < 0:
            low = mid + 1
        else:
            high = mid - 1

print(arr[left_answer], arr[right_answer])