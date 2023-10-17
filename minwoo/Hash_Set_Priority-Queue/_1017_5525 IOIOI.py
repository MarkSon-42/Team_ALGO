# 'IOI'를 찾으면 된다.

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

answer, cnt, i = 0, 0, 0

while i <= (m - 2):
    if s[i:i + 3] == 'IOI':  # IOI 발견시
        i += 2  # IO건너뛰고 찾아야하니 인덱스 조정
        cnt += 1  # IOI패턴의 개수
        if cnt == n:  # IOI패턴의 개수가 곧 원하는 Pn   ,  n = 2 -> 'IOIOI'
            answer += 1
            cnt -= 1  # 다시 cnt 감소시켜서 IOI 검색

    else:
        i += 1
        cnt = 0

print(answer)