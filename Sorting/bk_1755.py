import sys

M, N = map(int, sys.stdin.readline().split())
C = N - M + 1
number = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
arr = []

for idx in range(M, N + 1):
    temp = []
    num = str(idx)
    for n in num:
        temp.append(number[n])
    arr.append([' '.join(temp), idx])

arr.sort()

for i in range(C // 10):
    print(i)
    for j in range(10):
        print(arr[i*10 + j][1], end=' ')
    print()

for j in range(C - C % 10, C):
    print(arr[j][1], end = ' ')
print()