'''
문제 : 의상
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''
def solution(clothes):
    answer = 1
    dic = {}
    
    for cloth, cType in clothes:
        if cType not in dic:
            dic[cType] = [cloth]
        else:
            dic[cType].append(cloth)
    
    
    # (a+1)(b+1)(c+1) 전개하면
    # abc + ab+ ac+ bc+ a+b+c+1
    # abc가 있는 항의 의미가 abc를 선택한 경우의 수라는 의미
    
    for i in dic.values():
        answer *= len(i) + 1
    
    return answer - 1