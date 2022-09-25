import sys

N = int(sys.stdin.readline().rstrip())
num = []
sum = 0

for _ in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()

first = num.pop()
if not num:
    sum += first

if first < 0:
    num.append(first)
    num.sort(reverse=True)
    first = num.pop()


while num:

    second = num.pop()

    if first > 0:
        if second > 0:
            if first == 1 or second == 1:
                sum += first + second
            else:
                sum += first * second
            
            if num:
                first = num.pop()
                if not num:
                    sum += first

                if first < 0:
                    num.append(first)
                    num.sort(reverse=True)
                    first = num.pop()

        elif second == 0:
            sum += first
            first = second
        else:
            sum += first
            if num:
                num.append(second)
                num.sort(reverse=True)
                first = num.pop()
            else:
                sum += second
    elif first == 0:
        if second == 0:
            first = second
        elif second < 0:
            if num and len(num) % 2 != 0: 
                num.append(second)
                num.sort(reverse=True)
                first = num.pop()
            else:
                sum += first * second
    else:
        sum += first * second

        if num:
            first = num.pop()
            if not num:
                sum += first

print(sum)