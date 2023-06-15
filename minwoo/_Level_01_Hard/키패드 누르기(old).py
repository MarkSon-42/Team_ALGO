# 키패드 한칸은 거리 1, 대각선 거리같은거 없음
# 조건문 처리
# 거리가 가깝다, 멀다,
# 거리가 같다 -> == 'left' ? =='right'
# *, # 은 따로 다룰게 아니라 그냥 숫자로 바꿔야 할듯?
# 0도 바꿔버려야 함. 0 때문에 조건 더늘어남.
# 1 2 3 4 5 6 7 8 9  ->  10 11 12
#                        *  0   #
def solution(numbers, hand):
    answer = ''
    r_location = 12
    l_location = 10

    for i in numbers:

        if i == 1 or i == 4 or i == 7:

            answer += 'L'
            l_location = i

        elif i == 3 or i == 6 or i == 9:

            answer += 'R'
            r_location = i

        else:

            if i == 0:
                i = 11
            left_tmp = abs(l_location - i)
            right_tmp = abs(r_location - i)

            left_dist = (left_tmp // 3) + (left_tmp % 3)
            right_dist = (right_tmp // 3) + (right_tmp % 3)  # 일단, 좌로부터, 우로부터 거리를 구해준다.
            if left_dist == right_dist:
                if hand == 'right':
                    answer += 'R'
                    r_location = i
                else:
                    answer += 'L'
                    l_location = i
            elif left_dist < right_dist:
                answer += 'L'
                l_location = i
            else:
                answer += 'R'
                r_location = i
    return answer