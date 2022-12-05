import sys

S = sys.stdin.readline().rstrip()
arr = []

for i in range(len(S)):
    arr.append(S[i:len(S)])

arr.sort()

for idx in range(len(S)):
    print(arr[idx])