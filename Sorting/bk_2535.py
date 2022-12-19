import sys

N = int(sys.stdin.readline().rstrip())
arr = []
check = {}
cnt = 0

for _ in range(N):
    cn, sn, gr = map(int, sys.stdin.readline().split())
    arr.append((cn, sn, gr))

arr.sort(key = lambda x : x[2], reverse = True)

for idx in range(N):
    if arr[idx][0] in check:
        check[arr[idx][0]] += 1
    else:
        check[arr[idx][0]] = 1
    
    if check[arr[idx][0]] > 2:
        continue
    else:
        print(arr[idx][0], arr[idx][1])
        cnt += 1

        if cnt == 3:
            break