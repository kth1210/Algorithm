import sys

T = int(sys.stdin.readline())
Button = [300, 60,  10]
result = [0, 0, 0]

for i in range(len(Button)):
    result[i] = T // Button[i]
    T %= Button[i]

if T != 0:
    print("-1")
else:
    print("%d %d %d" %(result[0], result[1], result[2]))