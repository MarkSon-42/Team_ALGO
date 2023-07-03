'''
문제 : 귤 고르기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138476
'''
from itertools import combinations

def solution(k, tangerine):
    answer = 0
    
    # 1. 크기별로 몇개가 들어있는지 dic을 만들어준다.
    tanDic = {}
    for i in tangerine:
        if i not in tanDic:
            tanDic[i] = 1
        else:
            tanDic[i] += 1
            
    temp = combinations(tanDic, 2)
    print(temp)
    
    return answer