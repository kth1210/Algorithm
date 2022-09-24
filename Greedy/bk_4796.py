import sys

case = []

while True:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break
    else:
        case.append((L, P, V))

for i in range(len(case)):
    temp = case[i][2] % case[i][1]
    if temp > case[i][0]:
        temp = case[i][0]
        
    result = (case[i][2] // case[i][1] * case[i][0]) + temp
    print("Case %d: %d" % (i + 1, result))