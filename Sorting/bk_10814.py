import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])

for idx in range(N):
    print(arr[idx][0], arr[idx][1])