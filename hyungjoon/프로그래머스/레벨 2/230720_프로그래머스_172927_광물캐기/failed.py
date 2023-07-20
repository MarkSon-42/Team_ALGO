'''
문제 : 광물 캐기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172927
'''
from collections import deque
def solution(picks, minerals):
    answer = 0
    
    # 다이아/철/돌 을 캐는데 필요한 피로도, 다이아/철/돌 순임
    tired = { 'diamond' : [1, 5, 25], 
              'iron'    : [1, 1, 5],
              'stone'   : [1, 1, 1] }
    
    # 1. 한번 사용한 곡괭이는 끝까지 쓴다.
    # 2. 모든 광물을 캐거나, 사용할 곡괭이가 없을 때까지 광물을 캔다.
    # 3. 종류에 상관없이 5개를 캔 후엔 사용불가
    
    # 광물을 5개 단위로 묶은 다음에, 그걸 다이아/철/돌 곡괭이로 캤을 때 최소값을 가진 애로 구해준다.
    # 단, 이 때 소모된 피로도가 동일하다면 등급이 낮은 곡괭이가 우선순위가 된다.
    
    minerals = deque(minerals)
    
    while minerals and sum(picks) > 0:
        # 5개씩 작업할 리스트를 생성해준다.
        workList = []
        while len(workList) < 5:
            if minerals:
                workList.append(minerals.popleft())
            else:
                break

        # 곡괭이별 소모되는 피로도, 곡괭이가 있는 경우에만 넣어준다.
        tiredDic = {}
        if picks[0] > 0:
            tiredDic['dia'] = 0
        if picks[1] > 0:
            tiredDic['iron'] = 0
        if picks[2] > 0:
            tiredDic['stone'] = 0

        # 값이 같을 때 우선순위, 값이 낮을수록 우선순위가 낮다. picks에서 바로 쓰기 위함임.
        priority = { 'dia' : 0,
                     'iron' : 1,
                     'stone' : 2}

        # 곡괭이별로 5개를 캤을 때 피로도가 얼마나 소모되는지 계산한다.
        for i in workList:
            if 'dia' in tiredDic:
                tiredDic['dia'] += tired[i][0]
            if 'iron' in tiredDic:
                tiredDic['iron'] += tired[i][1]
            if 'stone' in tiredDic:
                tiredDic['stone'] += tired[i][2]
        
        # 최소 피로도값을 구한다.
        minValue = min(tiredDic.values())
        # 최소 피로도가 여러개라면, 비교를 위해서 tempList를 생성해준다.
        tempList = []
        for key, value in tiredDic.items():
            if value == minValue:
                tempList.append(key)

        # 최종적으로 사용되는 곡괭이
        finalPick = ''

        # 최솟값이 겹치는 친구들이 있다면, 우선순위 처리를 해준다.
        if len(tempList) != 1 and tempList:
            temp = []
            for i in tempList:
                temp.append([i, priority[i]])
            # 우선순위가 높은 순서로 정렬, priority 딕셔너리의 숫자가 높을수록 우선순위가 높기때문에, 내림차순으로 정렬한다.
            temp.sort(key=lambda x:x[1], reverse=True)
            finalPick = temp[0][0]
        else:
            finalPick = tempList[0]
        
        answer += tiredDic[finalPick]
        picks[priority[finalPick]] -= 1
    
    return answer

# 반례
print(solution(	[1, 1, 0], ["stone", "stone", "iron", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]))