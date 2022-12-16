import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

S = 0
for idx in range(N):
    if (idx + 1) % 3 == 0:
        continue
    else:
        S += arr[idx]

print(S)