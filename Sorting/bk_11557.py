import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = []

    for _ in range(N):
        S, L = sys.stdin.readline().split()
        arr.append((S, int(L)))
    
    arr.sort(key = lambda x : -x[1])
    print(arr[0][0])