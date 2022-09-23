import sys

N = sys.stdin.readline().rstrip()

count_0 = len(N.split('10'))
count_1 = len(N.split('01'))

if N[0] == '1':
    count_0 -= 1
    count_1 += 1
else:
    count_0 += 1
    count_1 -= 1

if count_0 <= count_1:
    print(count_0)
else:
    print(count_1)