import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    name, kor, eng, mat = sys.stdin.readline().split()
    arr.append((name, int(kor), int(eng), int(mat)))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for idx in range(N):
    print(arr[idx][0])