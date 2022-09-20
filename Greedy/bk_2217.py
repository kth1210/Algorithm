import sys

cnt = int(input())
R = []
W = 0

for _ in range(cnt):
    R.append(int(sys.stdin.readline()))

R.sort()

for i in range(cnt):
    if W <= R[i] * (cnt - i):
        W = R[i] * (cnt - i)

print(W)