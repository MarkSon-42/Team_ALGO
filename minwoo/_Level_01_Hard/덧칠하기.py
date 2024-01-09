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
