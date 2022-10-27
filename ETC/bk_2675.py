import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S= sys.stdin.readline().split()
    resultList = []

    for idx in range(len(S)):
        for _ in range(int(R)):
            resultList.append(S[idx])
    resultString = "".join(resultList)
    
    print(resultString)