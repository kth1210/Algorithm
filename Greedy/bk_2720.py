import sys

T = int(sys.stdin.readline().rstrip())
result = []
change = [25, 10, 5, 1]

for _ in range(T):
    C = int(sys.stdin.readline().rstrip())
    temp = []

    for m in change:
        temp.append(C // m)
        C %= m
    
    result.append(temp)

for i in range(T):
    for j in range(4):
        print(result[i][j], end=' ')
    print()