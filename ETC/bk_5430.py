import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    isError = False
    command = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    temp = sys.stdin.readline().rstrip()
    temp = temp[1:-1]
    arr = temp.split(',')
    pointer_C = 0
    pointer_L = 0
    pointer_R = len(arr) - 1

    for C in command:
        if C == 'R':
            if pointer_C == pointer_L:
                pointer_C = pointer_R
            elif pointer_C == pointer_R:
                pointer_C = pointer_L
        elif C == 'D':
            if N == 0:
                isError = True
                break
            else:
                if pointer_C == pointer_R:
                    pointer_C -= 1
                    pointer_R -= 1
                    N -= 1
                elif pointer_C == pointer_L:
                    pointer_C += 1
                    pointer_L += 1
                    N -= 1
    
    if isError:
        print("error")
    else:
        print('[',end = '')
        
        if pointer_C == pointer_L:
            for idx in range(pointer_L, pointer_R + 1):
                print(arr[idx],end = '')
                if idx != pointer_R:
                    print(',',end = '')
        elif pointer_C == pointer_R:
            for idx in range(pointer_R, pointer_L - 1, -1):
                print(arr[idx],end = '')
                if idx != pointer_L:
                    print(',',end = '')
        print(']')
