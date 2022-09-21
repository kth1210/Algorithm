import sys

N = int(sys.stdin.readline().rstrip())
Time = [[0] * 2 for _ in range(N)]
cnt = 0

for i in range(N):
    Time[i][0], Time[i][1] = map(int, sys.stdin.readline().split())

Time.sort(key = lambda x : (x[1], x[0]))

endTime = Time[0][1]
cnt += 1

for i in range(1, N):
    if Time[i][0] >= endTime:
        cnt += 1
        endTime = Time[i][1]

print(cnt)