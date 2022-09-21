import sys

N = int(sys.stdin.readline())
Bag = [5, 3]
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        N %= 5
        break
    else:
        N -= 3
        cnt += 1

if N != 0:
    print("-1")
else:
    print(cnt)