import sys

width = []
height = []
cut = []
result = []

W, H = map(int, sys.stdin.readline().split())
width.append(W)
height.append(H)

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    c, n = map(int, sys.stdin.readline().split())

    if c == 0:
        height.append(n)
    elif c == 1:
        width.append(n)

height.sort()
width.sort()

preW = 0
preH = 0

for curW in width:
    calW = curW - preW
    for curH in height:
        calH = curH - preH
        result.append(calW * calH)
        preH = curH
    preW = curW
    preH = 0

result.sort(reverse = True)
print(result[0])