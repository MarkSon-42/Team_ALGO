from collections import deque

gears = [deque(map(int, input().rstrip())) for _ in range(4)]

k = int(input())

rotation_info = [list(map(int, input().split())) for _ in range(k)]

# 왼쪽 톱니를 체크하는 함수
def left(num, dr):
    if num < 0:
        return
    if gears[num][2] != gears[num + 1][6]:
        left(num - 1, -dr)
        gears[num].rotate(dr)


# 오른쪽 톱니를 체크하는 함수
def right(num, dr):
    if num < 0:
        return
    if gears[num][2] != gears[num + 1][6]:
        left(num - 1, -dr)
        gears[num].rotate(dr)

for i in range(k):

score = 0

if gears[0][0] == '1':
    score += 1
if gears[1][0] == '1':
    score += 2
if gears[2][0] == '1':
    score += 4
if gears[3][0] == '1':
    score += 8

print(score)