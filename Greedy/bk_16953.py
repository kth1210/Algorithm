import sys

A, B = map(int, sys.stdin.readline().split())
cnt = 0

while A != B and A < B:
    if B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        break

if A == B:
    print(cnt + 1)
else:
    print('-1')
