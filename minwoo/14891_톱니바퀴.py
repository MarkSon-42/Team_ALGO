from collections import deque

# 톱니바퀴 모양이면 원형큐를 구현해야 하나?? deque쓰면 될듯

gears = [deque(map(int, input().rstrip())) for _ in range(4)]

k = int(input())

for _ in range(k):
    num, dr = map(int, input().split())

    if dr == 1:
        if gears[num - 1][2] != gears[num][6]:
            gears[num - 1].pop()
            gears[num - 1].appendleft()
            # ... ???

# 이렇게 일일이 구현하느거 맞나?

    else:
        pass


# 왼 톱니의 2번 인덱스와 오른 톺니의 6번 인덱스를 비교해야 함.


# https://yeon-code.tistory.com/75

# 참고해서 다시.

