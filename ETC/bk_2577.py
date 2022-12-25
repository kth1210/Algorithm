import sys

result = {}

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

R = A * B * C

for t in str(R):
    if t not in result:
        result[t] = 1
    else:
        result[t] += 1

for n in range(10):
    if str(n) not in result:
        print("0")
    else:
        print(result[str(n)])