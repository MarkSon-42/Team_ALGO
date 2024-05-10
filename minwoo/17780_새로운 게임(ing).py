# 문제 요소 하나하나를 잘 읽어보고, 놓치지 않아야 한다.
#
# 다음은 규칙과, 흘려 버릴 수 있는 요소들을 정리

# 삼성 식 빡구현 문제인데..

# 말의 이동 : 1번부터 k번말 순서대로 이동함. 1번 움직이고 2번 움직이고..

# 1. 이동하고자 하는 칸이 흰색인 경우 : 그대로 감. 뒤집지 않음.


# 2. 이동하고자 하는 칸이 빨간색인 경우  : 말 쌓인걸 반대로 뒤집는다. 다른말이 있으면 그 위에 뒤집은채로 올린다.


# 3. 이동하고자 하는 칸이 파란색인 경우  : 이동 방향을 반대로 바꾸고  좌 -> 우  , 상 -> 하 한칸 이동. 방향 반대로 하고 가는 칸도 파란색이면 이동하지 않음.

#  게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력

# K 번째 말 :
#  h[i][0] -> 행 번호
#  h[i][1] -> 열 번호
#  h[i][2] -> 이동 방향
# k번까지 이동 찍을때마다 카운트를 늘려준다.
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')  # 6번 예제를 보면서 디버깅하면서 구현 진행


N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(1, N + 1)]
horse_info = [list(map(int, input().split())) for i in range(1, K + 1)]
horse = deque()  # 말 스택.. 이 아니라 큐로 해야 하는거 아닌가?
# [A,B,C] [D,E] -> DEABC
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# 1~k번말을 알파멧으로 매겨줘야함?
# 좌표당말의정보를 3차원 배열로 다루는게 맞나..? 머리 터지는




# 1 -> right
# 2 -> left
# 3 -> up
# 4 -> down

answer = 0

# 말들을 겹치게 올리는건 어떻게 해야 하는..? stack?

while True:
    for i in range(1, K + 1):  # 턴을 계속 반복하면서 루프 끝나면 카운트
        horse.appendleft()
        horse_pos = [horse_info[i][0], horse_info[i][1]]
        dr = horse_info[i][2]

        # ...

        # if matrix[]
