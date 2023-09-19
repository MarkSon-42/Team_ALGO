# 그림그렸다
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

train_seat = [[0] * 20 for i in range(n)]  # 기차 좌석 초기화

seat_loc = 0

for i in range(n):
    instructions = list(map(int, input().split()))
    if instructions[0] == '1':  # x번째 좌석에 태우기
        train_seat[i+1][instructions[2]] = 1
    if instructions[0] == '2':  # x번쨰 좌석 사람 하차
        train_seat[i + 1][instructions[2]] = 0
    if instructions[0] == '3':  # 승객 모두 한칸씩 뒤로 (배열 오른쪽으로 이동)
        pass
    if instructions[0] == '4':  # 승객 모두 한칸씩 앞으로 이동 ( 배열 왼쪽으로 이동 )
        pass

# print(train_seat)

