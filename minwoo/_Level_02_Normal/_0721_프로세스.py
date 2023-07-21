# 아니 왜 우선순위가 큰 자연수대로 의미부여가 되어있는지...

def solution(priorities, location):
    # 몇 번째 실행인걸 알면 되기에 answer를 count로 보면 됨.
    answer = 0
    while True:
        most_pri = max(priorities)
        # 만약 프로세스가 큐의 가장 높은 우선 순위보다 낮은 경우, 다시 큐에 넣음.
        if priorities.pop(0) < most_pri:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                return answer
            location -= 1

