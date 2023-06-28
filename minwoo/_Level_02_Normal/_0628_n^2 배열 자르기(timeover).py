# 시간초과 날것을 뻔히 알지만.. 그래도 시도한 흔적 남기기용

def solution(n, left, right):
    answer = []

    for i in range(n):
        for j in range(n):
            answer.append(max(i + 1, j + 1))

    return answer[left:right + 1]