import sys

N, M = map(int, sys.stdin.readline().split())

daily_money = []

for _ in range(N):
    daily_money.append(int(sys.stdin.readline().rstrip()))

low = max(daily_money)
high = sum(daily_money)
result = 0

while low <= high:
    cnt = 1

    K = (low + high) // 2
    remaining = K

    for use in daily_money:
        # 남은 돈이 오늘 쓸 돈보다 적으면 무조건 다시 뽑아야 됨
        if remaining < use:
            remaining = K
            cnt += 1
            remaining -= use
        else:
            remaining -= use
    
    if cnt > M:
        low = K + 1
    # elif cnt < M:
    #     high = K - 1
    else:
        result = K
        high = K - 1

print(result)