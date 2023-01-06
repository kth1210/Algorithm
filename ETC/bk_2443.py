import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(i):
        print(" ", end="")
    for k in range(i+1, N):
        print("*", end="")
    print("*", end="")
    for l in range(i+1, N):
        print("*", end="")
    print()