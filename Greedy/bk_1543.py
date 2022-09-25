import sys

S = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()

arr = S.split(C)

print(len(arr) - 1)