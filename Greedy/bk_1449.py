import sys

N, L = map(int, sys.stdin.readline().split())
tape = L - 1
hole = list(map(int, sys.stdin.readline().split()))
cnt = 0

hole.sort()

temp = hole[0]
for idx in range(1, N):
    if hole[idx] - temp > tape:
        cnt += 1
        temp = hole[idx]
cnt += 1

print(cnt)