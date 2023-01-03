import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(i):
        print("", end=" ")
    for k in range(i, N):
        print("*", end="")
    print()