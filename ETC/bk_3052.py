import sys

result = {}

for _ in range(10):
    N = int(sys.stdin.readline().rstrip())

    N %= 42

    if N not in result:
        result[N] = 1
    else:
        result[N] += 1

print(len(result))