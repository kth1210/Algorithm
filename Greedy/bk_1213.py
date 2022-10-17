import sys

str = list(sys.stdin.readline().rstrip())

# 알파뱃의 개수 저장
alphabet_cnt = [0 for _ in range(27)]
result_half = ""

# 홀수인 알파뱃의 개수, 알파뱃 저장
odd_cnt = 0
odd_idx = 0

for alpha in str:
    alphabet_cnt[ord(alpha) - 65] += 1

for i in range(27):
    if alphabet_cnt[i] % 2 != 0:
        odd_cnt += 1
        odd_idx = i
    
    # 알파뱃의 개수의 절반만큼 저장, 홀수라면 절반 - 1
    cnt = alphabet_cnt[i] // 2
    for _ in range(cnt):
        result_half += chr(i + 65)

# 홀수인 알파뱃이 2개 이상
if odd_cnt > 1:
    print("I'm Sorry Hansoo")
# 홀수인 알파뱃이 하나면 중간에 출력
elif odd_cnt == 1:
    result_center = chr(odd_idx + 65)
    print(result_half + result_center + result_half[::-1])
else:
    print(result_half + result_half[::-1])