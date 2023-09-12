# 프로그래머스에 이름만 같은 문제가 있다 ( 문제는 아예 다름 )
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
A, B, C, M = map(int, input().split())

ftg = 0
work = 0

for i in range(24):
    if ftg+A <= M:  # 피로도에 여유가 있을 시
        ftg = ftg+A
        work += B
    else:  # 과로했을 때
        if ftg-C >= 0:  #  피로도 0 넘으면 안됨.
            ftg = ftg-C
        else:  # 피로도 0 보다 작을시
            ftg = 0

print(work)