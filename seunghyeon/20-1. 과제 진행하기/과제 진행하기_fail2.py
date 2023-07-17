# 간단한 회고
  # fail1 코드에 비해 훨씬 가독성이 올라가고 간결해짐
  # 알맞은 결과를 출력하기는 하나 매우 많은 테스트 케이스에서 시간 초과가 남

def timeToMin(string):
    h, m = map(int, string.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []
    plans = [(subject, timeToMin(start), int(runningT)) for subject, start, runningT in plans]
    plans.sort(key=lambda x: x[1])

    stk = []

    for i in range(len(plans)):
        # 가장 마지막 과제의 경우
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            if len(stk) > 0:
                while len(stk) > 0:
                    answer.append(stk[-1][0])
                    stk.pop()

        # 첫 번째 과제 ~ 마지막 직전 과제까지의 경우
        else:
            time = plans[i + 1][1] - plans[i][1]
            subject, runningT = plans[i][0], plans[i][2]

            # 다음 과제 시작시각 전까지 현재 과제를 못 끝내는 경우
            if runningT > time:
                stk.append([subject, runningT - time])

            # 다음 과제 시작 시각에 딱 맞춰 현재 과제를 끝낸 경우
            elif runningT == time:
                answer.append(subject)

            # 다음 과제 시작 시각 전에 현재 과제를 끝내고 시간이 남은 경우
            else:
                answer.append(subject)
                time = runningT
                stkLen = len(stk)
                while time > 0:
                    if stkLen > 0 and stk[-1][1] <= time:
                        answer.append(stk[-1][0])
                        time -= stk[-1][1]
                        stk.pop()
                        stkLen -= 1
                if stkLen > 0:
                    stk[-1][1] -= time

    return answer
