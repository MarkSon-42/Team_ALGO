'''
문제 : 뉴스 클러스터링
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17677
'''
import re
def solution(str1, str2):
    answer = 0
    str1Arr, str2Arr = [], []
    # 1. 정규식을 활용해서 영문자가 아니면 해당 쌍은 다중집합 원소에 포함시키지 않는다.
    for i in range(len(str1)-1):
        tempStr = str1[i] + str1[i+1]
        tempStr = tempStr.lower()
        tempStr = re.sub('[^a-zA-Z]','',tempStr)
        if len(tempStr) == 2:
            str1Arr.append(tempStr)
    
    for i in range(len(str2)-1):
        tempStr = str2[i] + str2[i+1]
        tempStr = tempStr.lower()
        tempStr = re.sub('[^a-zA-Z]','',tempStr)
        if len(tempStr) == 2:
            str2Arr.append(tempStr)
    
    # 둘 다 비어있으면 65536 return
    if not str1Arr and not str2Arr:
        return 65536
    
    # 2. 교집합은 min, 합집합은 max 이다.
    gyo, hap = [], []
    
    # 요소 계산을 위해 set해준다.
    set1, set2 = set(str1Arr), set(str2Arr)
    
    # 교집합 만들어주는 작업
    for i in set1:
        if i in set2:
            c1, c2 = str1Arr.count(i), str2Arr.count(i)
            cnt = min(c1, c2)
            for j in range(cnt):
                gyo.append(i)
                
    # 합집합 만들어주는 작업
    for i in set1:
        # set1에 있는 요소가 set2에도 있으면, 둘 중 더 갯수가 많은 요소만큼 append 해준다.
        if i in set2:
            c1, c2 = str1Arr.count(i), str2Arr.count(i)
            cnt = max(c1, c2)
            for j in range(cnt):
                hap.append(i)
        # set1에만 있다면 set1의 i 요소 갯수만큼만 append 해준다.
        else:
            for j in range(str1Arr.count(i)):
                hap.append(i)
                
    # 위 작업을 거치면 set2에만 있는 애들은 계산할 수 없게된다. 따라서 set2에만 있는 애들을 합집합 요소로 넣어준다.
    for i in set2:
        if i not in set1:
            for j in range(str2Arr.count(i)):
                hap.append(i)
    
    answer = len(gyo) / len(hap)
    
    return int(answer * 65536)