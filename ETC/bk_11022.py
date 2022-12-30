import sys

N = int(sys.stdin.readline().rstrip())

for idx in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(idx, a, b, a+b))