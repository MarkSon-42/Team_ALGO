'''
문제 : 과제 진행하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''
def timeToMinute(t):
    t = t.split(':')
    return int(t[0])*60 + int(t[1])

def solution(plans):
    answer = []
    # 0. 시간 계산은 모두 분으로 통일시켜서 진행한다.
    # 1. 도중에 멈춘 과제를 처리해줄 stack을 생성한다.
    stack = []
    # 2. plans 배열을 시작순으로 정렬해준 sortedPlans 에 넣어준다.(NlogN)
    sortedPlans = []
    for i in plans:
        name, start, playtime = i[0], timeToMinute(i[1]), int(i[2])
        sortedPlans.append([name, start, playtime])
    sortedPlans.sort(key=lambda x:x[1])
    # 현재 시간을 의미하는 t 를 첫 과제의 시작시간으로 초기화해준다.
    t = sortedPlans[0][1]

    # 3. for문을 돌면서, a과제를 하다가 b과제를 해야되면 stack에 넣어준다.
    for i in range(len(sortedPlans)-1):
        # 현재 과제
        Aname, Astart, Aplaytime = sortedPlans[i][0], sortedPlans[i][1], sortedPlans[i][2]
        # 다음 과제
        Bname, Bstart, Bplaytime = sortedPlans[i+1][0], sortedPlans[i+1][1], sortedPlans[i+1][2]
        # 3-1. 만약 기존 과제가 남아있다면 해당 과제 먼저 수행
        while stack:
            Sname, Splaytime = stack[-1][0], stack[-1][1]
            # 3-2. 다음 과제 전까지 수행이 불가하면 시간 업데이트만 진행, 끝낼 수 있다면 pop
            if t+Splaytime <= Bstart:
                answer.append(Sname)
                stack.pop()
                t += Splaytime
            else:
                stack[-1] -= (Bstart-t)
                t += Bstart-t
                break
        # 4. 만약, 현재 과제를 다음 과제 전까지 끝낼 수 있다면 정답에 넣어주기
        # 마지막 과제 처리를 어캄 ㅠ?
        if t + Aplaytime <= Bstart:
            t += Aplaytime
            answer.append(Aname)
            
    
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))