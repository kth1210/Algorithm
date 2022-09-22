import sys

N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

temp = P[0]
result = 0

for i in range(N-1):
    if temp <= P[i]:
        result += temp * L[i]
    else:
        temp = P[i]
        result += temp * L[i]

print(result)
    

