def timeToMin(string):
    h, m = map(int, string.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []
    plans = [(subject, timeToMin(start), int(runningT)) for subject, start, runningT in plans]
    plans.sort(key = lambda x : x[1])

    for i in range(len(plans)):
        stk = []
        nowSubjectName = plans[i][0]
        if (i == len(plans) - 1): # 가장 늦게 시작하는 과제의 경우, 무조건 asnwer에 저장
            answer.append(nowSubjectName)
            if (len(stk) > 0): # 만약 plans의 마지막 요소를 검사했는데, stk이 비어있지 않다면 top부터 싹 다 answer로 넣어 줌
                while (len(stk) > 0):
                    answer.append(stk[-1][0])
                    stk.pop()
        else:
            whenNowEnd = plans[i][1] + plans[i][2]
            whenNextStart = plans[i + 1][1]

            if (whenNowEnd == whenNextStart) :
                answer.append(nowSubjectName)
                break;

            elif whenNowEnd > whenNextStart:
                stk.append([nowSubjectName, whenNowEnd - whenNextStart])

            else:
                answer.append(nowSubjectName)
                if len(stk) > 0 and (stk[-1][1] <= whenNextStart - whenNowEnd): # stk.isEmpty() == False도 됨
                    while (whenNextStart - whenNowEnd) - stk[-1][1] >= 0:
                        answer.append(nowSubjectName)
                        stk.pop()
                    if (whenNextStart - whenNowEnd) < stk[-1][1]:
                        stk[-1][1] -= whenNextStart - whenNowEnd
                elif len(stk) > 0 and (whenNextStart - whenNowEnd < stk[-1][1]):
                    stk[-1][1] -= whenNextStart - whenNowEnd
    return answer;
