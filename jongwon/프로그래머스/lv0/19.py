# 점의 위치 구하기

def solution(dot):
    dot = [dot[0], dot[1]]
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot [0] < 0 and dot[1] < 0:
        answer = 3
    else:
        answer = 4
    return answer