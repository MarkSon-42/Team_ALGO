# 그림그렸다
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

train_seat = [[0] * 20 for i in range(n)]  # 기차 좌석 초기화


for i in range(1, m + 1):  # 명령 개수만큼 반복문
    instructions = list(map(int, input().split()))
    if instructions[0] == '1':  # x번째 좌석에 태우기
        train_seat[i][instructions[2]] = 1

    if instructions[0] == '2':  # x번쨰 좌석 사람 하차
        train_seat[i][instructions[2]] = 0



    if instructions[0] == '3':  # 승객 모두 한칸씩 뒤로 (배열 오른쪽으로 이동)
        if train_seat[i][20] == '1':
            train_seat[i][20] = 0  # 맨 끝 사람은 하차 처리
        #  모든 사람을 한방에 뒤로 한칸씩 이동하는 방법 없나?
        for j in range(1, 20):  # 맨 끝자리 20은 위 조건문에서 따로 처리함
            if train_seat[i][j] == 1:
                train_seat[i][j+1] = 1
            else:
                train_seat[i][j] = 0
                train_seat[i][j+1] = 0

    if instructions[0] == '4':  # 승객 모두 한칸씩 앞으로 이동 ( 배열 왼쪽으로 이동 )
        if train_seat[i][1] == '1':
            train_seat[i][1] = 0  # 맨 앞 사람은 하차 처리
        for j in range(2, 21):  # 맨 끝자리 1은 위 조건문에서 따로 처리함
            if train_seat[i][j] == 1:
                train_seat[i][j-1] = 1
            else:
                train_seat[i][j] = 0
                train_seat[i][j-1] = 0

print(train_seat)

