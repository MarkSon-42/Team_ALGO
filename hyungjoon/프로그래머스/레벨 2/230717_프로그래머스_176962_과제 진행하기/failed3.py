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
    for i in range(len(sortedPlans)):
        # 현재 과제
        Aname, Astart, Aplaytime = sortedPlans[i][0], sortedPlans[i][1], sortedPlans[i][2]
        # 마지막 과제는 stack에 넣어서 후처리 진행
        if i == len(sortedPlans) - 1:
            stack.append([Aname, Aplaytime])
            break
        # 다음 과제 시작시간
        Bstart = sortedPlans[i+1][1]
        
        # 다음 과제 전까지 수행이 가능하면 현재 과제 수행 이후 스택과제 수행
        if t + Aplaytime <= Bstart:
            t += Aplaytime
            answer.append(Aname)
            # 만약 현재 과제를 끝냈는데, 바로 다음과제를 해야되면 다음 과제 수행단계로 넘어간다.
            if t <= Bstart:
                continue
            # 가능한 시간동안 while문 계속 돌려줘야됨
            able = Bstart - (Astart + Aplaytime)
            while able != 0 and stack:
                Sname, Splaytime = stack[-1][0], stack[-1][1]
                # 다음 과제 전까지 스택과제 수행이 가능한가?
                if Splaytime <= able:
                    answer.append(Sname)
                    stack.pop()
                    t += Splaytime
                    able -= Splaytime
                else:
                    # 아니라면, 진행도만 업데이트 해주기
                    stack[-1][1] -= (Bstart - t)
                    t += (Bstart - t)
                    able = 0
                    break
        else:
            # 4-1. 못끝낸다면 현재시간 갱신해주고 stack에 넣기
            stack.append([Aname, Aplaytime-(Bstart-t)])
            t += (Bstart-t)
            
    # 5. stack에 남아있는 친구들 정리
    while stack:
        answer.append(stack[-1][0])
        stack.pop()
            
    
    return answer

print(solution([["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]))