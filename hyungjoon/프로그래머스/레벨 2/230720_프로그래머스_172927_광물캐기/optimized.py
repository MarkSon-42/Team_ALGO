'''
문제 : 광물 캐기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172927
'''
from collections import deque
def solution(picks, minerals):

    answer = 0
    tiredList = [[1,1,1],[5,1,1],[25,5,1]]
    connectionDict = {
        "diamond":0,
        "iron" : 1,
        "stone" : 2
    }
    info = []
    minerals = minerals[:5 * sum(picks)]
    q = deque(minerals)
    while q:
        howManyDig = 0
        usedDia, usedIron, usedStone = 0,0,0
        while howManyDig < 5:
            howManyDig += 1
            mineral = q.popleft()
            usedDia += tiredList[0][connectionDict[mineral]]
            usedIron += tiredList[1][connectionDict[mineral]]
            usedStone += tiredList[2][connectionDict[mineral]]
            if not q:
                break
        info.append([usedDia,usedIron,usedStone])
    info.sort(key = lambda x : [x[2],x[1],x[0]])

    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer

    return answer

# 반례
print(solution(	[1, 1, 0], ["stone", "stone", "iron", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]))