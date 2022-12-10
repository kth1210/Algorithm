import sys

arr_A = []
sum_A = 0
arr_B = []
sum_B = 0

for _ in range(10):
    arr_A.append(int(sys.stdin.readline().rstrip()))

for _ in range(10):
    arr_B.append(int(sys.stdin.readline().rstrip()))

arr_A.sort(reverse = True)
arr_B.sort(reverse = True)

for idx in range(3):
    sum_A += arr_A[idx]
    sum_B += arr_B[idx]

print(sum_A)
print(sum_B)