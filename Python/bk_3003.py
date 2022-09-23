import sys

N = list(map(int, sys.stdin.readline().split()))

chess = [1, 1, 2, 2, 2, 8]

for idx in range(len(chess)):
    print(chess[idx] - N[idx], end = ' ')