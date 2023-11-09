# 여러개의 입력이라 해놓고 하나의 입력예제만 준것도 낚시..

# 1. 단위를 잘 읽어야 한다. 센치미터~나노미터
# 2. 여러개의 입력케이스인데 t가 없다? -> try-catch문

# mid가 필요없단느것 ok

# 여러개의 입력 -> 이것 때문에 try-catch  : 옛날문제 + 외국문제라 매우 생략된게 많다?

# 그리고 정답 중복처리문제는 정렬로 이미 해결된다.

import sys

input = sys.stdin.readline



while True:
    try:
        x = int(input().rstrip()) * 10_000_000
        n = int(input().rstrip())
        i, j = 0, n - 1
        flag = True
        lego = [int(input().rstrip()) for _ in range(n)]
        lego.sort()
        while i < j:
            if x == lego[i] + lego[j]:
                print("yes {} {}".format(lego[i], lego[j]))
                flag = False
                break
            elif x < lego[i] + lego[j]:
                j -= 1
            else:
                i += 1
        if flag:
            print("danger")
    except:
        break


