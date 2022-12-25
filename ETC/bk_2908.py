import sys

A, B = sys.stdin.readline().split()

A = list(A)
B = list(B)
A.reverse()
B.reverse()

A = int("".join(A))
B = int("".join(B))

if A > B:
    print(A)
else:
    print(B)