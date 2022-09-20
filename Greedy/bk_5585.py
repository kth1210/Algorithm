Money = 1000 - int(input())
C = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in range(len(C)):
    cnt += Money // C[i]
    Money %= C[i]

print(cnt)