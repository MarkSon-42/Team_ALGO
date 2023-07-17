def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
    answer = []
    while plans: # "answer"에 있는 각 계획의 시작 시간과 비교하여 해당 시간 이후에 시작하는 계획이라면, 해당 계획의 시작 시간을 더하고 시간이 겹치는 경우를 처리합니다.
        x = plans.pop()
        for idx, val in enumerate(answer):
            if val[0] > x[1]:
                answer[idx][0] += x[2]
        answer.append([x[1] + x[2], x[0]])
    answer.sort() # "answer"를 시간 순서대로 정렬합니다.

    return list(map(lambda x: x[1], answer))

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))

