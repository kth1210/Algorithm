import sys

arr = []
done = False
for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

S = sum(arr)

for i in range(8):
    for j in range(i+1,9):
        if arr[i] + arr[j] == S - 100:
            arr[i] = 0
            arr[j] = 0
            done = True
            break
    if done:
        break

arr.sort()

for idx in range(2, 9):
    print(arr[idx])