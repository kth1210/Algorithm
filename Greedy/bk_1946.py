import sys

T = int(sys.stdin.readline().rstrip())
result = []

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    point = [[0] * 2 for _ in range(N)]
    hired = 1

    for i in range(N):
        point[i][0], point[i][1] = map(int, sys.stdin.readline().split())

    point.sort(key = lambda x : x[0])

    criteria = point[0][1]
    for i in range(1, N):
        if point[i][1] < criteria:
            hired += 1
            criteria = point[i][1]
    
    result.append(hired)

for idx in range(T):
    print(result[idx])