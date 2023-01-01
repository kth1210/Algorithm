import sys

N, K = map(int, sys.stdin.readline().split())
LAN = []

for _ in range(N):
    LAN.append(int(sys.stdin.readline().rstrip()))

LAN.sort()

low = 1
high = LAN[N-1]
result = 0

while low <= high:
    cnt = 0
    mid = (low + high) // 2

    for l in LAN:
        temp = l // mid
        cnt += temp
    
    if cnt < K:
        high = mid - 1
    else:
        result = mid
        low = mid + 1

print(result)
