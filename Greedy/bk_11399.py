N = int(input())
P = list(map(int, input().split()))
result = 0

P.sort()

for i in range(N):
    for j in range(0, i + 1):
        result += P[j]

print(result)
