# t초 동안 붕대 감으면서, 1초마다 x만큼 회복 - > 반복문

# t초 연속으로 붕대감기 성공하면 y만큼 추가 회복

# 최대 체력이 존재 -> 조건문

# 붕대감기 도중에 공격 당하면 기술 취소, 연속 성공 시간이 0으로 초기화 -> 조건문

# 공격으로 0이하 되면 죽음 -> -1리턴

# 반례를 못찾겠다.

def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    curr_t, curr_h = 0, health
    continuity = 0
    total_time = attacks[len(attacks) - 1][0]
    while curr_t <= total_time and attacks:
        curr_t += 1
        if attacks[0][0] == curr_t:
            curr_h -= attacks[0][1]
            continuity = 0
            if curr_h <= 0:
                return -1
            del attacks[0]
        else:
            curr_h += x
            continuity += 1
            if curr_h > health:
                curr_h = health
            if continuity == t:
                curr_h += y
                if curr_h > health:
                    curr_h = health

    return curr_h




# 정확성 93.3

# 테스트 14번이 오답.. 반례가 무엇이 있을까..?

# 아마 조건문 순서에 어딘가 실수가 있는?

# 문제 실행흐름이랑 구현한 실행흐름이 달라서 그런거 같은데
# 그냥 아예 다시 풀어보자..

# 1 1 1
# 1
# 1
# 1 1

# 다 1일때?
