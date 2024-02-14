# https://www.youtube.com/watch?v=PnXovk2JtU4

# "스카피"는 이전에 각 손님들이 주문할 때
# 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만
# 코스요리 메뉴 후보에 포함

from itertools import combinations


def solution(orders, course):
    answer = []

    max_list = [0] * (max(course) + 1)

    temp = [{} for _ in range(max(course) + 1)]

    for i in range(len(orders)):
        order = sorted(orders[i])

        for j in range(2, max(course) + 1):
            combi = list(combinations(order, j))
            for k in range(len(combi)):

                key = ''.join(combi[k])
                if key in temp[j]:
                    temp[j][key] += 1
                    if temp[j][key] > max_list[j]:
                        max_list[j] = temp[j][key]
                else:
                    temp[j][key] = 1

    for num in course:
        for key, value in temp[num].items():
            if value >=2 and value == max_list[num]:
                answer.append(key)
    answer.sort()

    return answer