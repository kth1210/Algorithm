N, K = map(int, input().split())
A = []
cnt = 0

for _ in range(N):
    A.append(int(input()))

for i in reversed(range(N)):
    cnt += K // A[i]
    K = K % A[i]

print(cnt)