import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    s = 0

    if arr[len(arr)-2] - arr[1] >= 4:
        print("KIN")
    else:
        for idx in range(1, len(arr)-1):
            s += arr[idx]
        print(s)