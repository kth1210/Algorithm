import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    P = sys.stdin.readline().rstrip()

    if P[1] == '=':
        print("skipped")
    else:
        R = list(map(int, P.split("+")))
        print(R[0] + R[1])