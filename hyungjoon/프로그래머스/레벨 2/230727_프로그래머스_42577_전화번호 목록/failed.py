'''
문제 : 전화번호 목록
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''
def solution(phone_book):
    dic = {}
    
    # 1. 길이별로 dic에 저장해준다.
    for i in phone_book:
        n = len(i)
        if n not in phone_book:
            dic[n] = [i]
        else:
            dic[n].append(i)
    
    # 2. 자신보다 길이가 같거나 낮은 dic만 탐색해준다.
    for i in phone_book:
        for key, value in dic.items():
            if key <= len(i):
                if i[:key] in value:
                    return False
    
    return True