import sys

N = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().split()))
score.sort(reverse=True)
S = 0

for idx in range(0, N):
    S += score[idx] / score[0] * 100

print(S / N)