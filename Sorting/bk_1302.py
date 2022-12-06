import sys

N = int(sys.stdin.readline().rstrip())
dic = {}

for _ in range(N):
    temp = sys.stdin.readline().rstrip()

    if temp not in dic:
        dic[temp] = 1
    else:
        dic[temp] += 1

sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(sorted_dic[0][0])