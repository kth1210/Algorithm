import sys

H, M = map(int, sys.stdin.readline().split())

if M < 45:
    H -= 1
    M = 60 + (M - 45)
else:
    M -= 45

if H < 0:
    H = 23
    
print(H, M)