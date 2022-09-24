import sys

N = int(sys.stdin.readline().rstrip())
alpha = []
alpha_val = {}
result = []
val = 0

for _ in range(N):
    alpha.append(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_val:
            alpha_val[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)
        else:
            alpha_val[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)

for temp in alpha_val.values():
    result.append(temp)

result.sort(reverse=True)

mul = 9
for idx in range(len(result)):
    val += result[idx] * mul
    mul -= 1

print(val)