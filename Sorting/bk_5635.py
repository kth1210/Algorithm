import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    n, d, m, y = sys.stdin.readline().split()
    arr.append((n, int(d), int(m), int(y)))

arr.sort(key = lambda x : (x[3], x[2], x[1]))

print(arr[N-1][0])
print(arr[0][0])