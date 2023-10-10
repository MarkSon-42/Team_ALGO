# 참고 : https://ho-log.tistory.com/18

# 숫자가 겁나 크다
# "표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다."
# 메모리를 신경써야 할것같은 느낌.

# 이게 우선순위 큐 기본문제
# 우선순위큐를 아직 모른다.

import heapq

N = int(input())
h = []
# 먼저 한번 상위 n 개를입력을 받아 놓고 상위 n를 해준다.
for n in map(int, input().split()):
    heapq.heappush(h, n)

# 두번째 열부터 입력을 받는데
for _ in range(1, N):
    # 바로 받고 빼준다.
    # n = 5
    for n in map(int, input().split()):
        # 넣어주고
        heapq.heappush(h, n)

        # 바로바로 빼줘서 상위 n 개만 놔눈다. 메모리 초과가 안난다.
        print(heapq.heappop(h))

print(heapq.heappop(h))
