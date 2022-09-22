import sys

N = sys.stdin.readline().rstrip()
sum = 0

for i in range(len(N)):
    sum += int(N[i])

if sum % 3 != 0 or "0" not in N:
    print("-1")
else:
    result = "".join(sorted(N, reverse=True))
    print(result)
