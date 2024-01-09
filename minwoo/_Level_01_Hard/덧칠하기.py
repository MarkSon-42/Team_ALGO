def solution(n, m, section):
    answer = 0
    while section:
        left = section[0]
        right = section[0] + m
        while section and section[0] < right:
            del section[0]
        answer += 1
    return answer


solution(8, 4, [2, 3, 6])


def solution_2(n, m, section):
    answer = 0
    while len(section) > 0:
        temp = section[0] + m
        while len(section) != 0 and temp > section[0]:
            section.pop(0)
        answer += 1

    return answer