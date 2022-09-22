import sys

S = int(sys.stdin.readline().rstrip())
N = 0
i = 1

while S > 0:
    S -= i
    i += 1
    N += 1

if S == 0:
    print(N)
elif S < 0:
    print(N-1)
