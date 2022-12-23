import sys

X = sys.stdin.readline().rstrip()

if X[0] == '0':
    if X[1] == 'x':
        print(int(X, 16))
    else:
        print(int(X, 8))
else:
    print(int(X))