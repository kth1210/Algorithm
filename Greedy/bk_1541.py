FM = input().split('-')
cnt = len(FM)
num = [0 for _ in range(cnt)]

for i in range(cnt):
    temp = FM[i].split('+')

    for j in range(len(temp)):
        if temp[j] != '+':
            num[i] += int(temp[j])

res = num[0]
for i in range(1, cnt):
    res -= num[i]

print(res)