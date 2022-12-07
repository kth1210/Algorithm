import sys

arr = []
result = 0
result_arr = []

for idx in range(1, 9):
    temp = int(sys.stdin.readline().rstrip())
    arr.append((idx, temp))

arr.sort(key=lambda x: x[1], reverse=True)

for idx in range(5):
    result += arr[idx][1]

print(result)
for idx in range(5):
    result_arr.append(arr[idx][0])

result_arr.sort()
for idx in range(5):
    print(result_arr[idx], end=' ')