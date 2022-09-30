import sys

max = 0
maxIdx = 0

for idx in range(9):
    N = int(sys.stdin.readline().rstrip())
    if N >= max:
        max = N
        maxIdx = idx

print(max)
print(maxIdx+1)