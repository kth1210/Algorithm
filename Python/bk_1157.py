import sys

W = sys.stdin.readline().rstrip().upper()
WL = list(set(W))
cnt = []

for i in WL:
    count = W.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(WL[cnt.index(max(cnt))])