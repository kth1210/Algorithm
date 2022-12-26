import sys

N, C = map(int, sys.stdin.readline().split())
position = []

for _ in range(N):
    position.append(int(sys.stdin.readline().rstrip()))

position.sort()

short, long = 1, position[-1] - position[0]

if C == 2:
    print(long)
else:
    result = 0

    while (short <= long):
        count = 1
        last_install = position[0]
        
        interval = (short + long) // 2

        for p in position:
            if p - last_install >= interval:
                count += 1
                last_install = p

        if count < C:
            long = interval - 1
        else:
            result = interval
            short = interval + 1
    print(result)