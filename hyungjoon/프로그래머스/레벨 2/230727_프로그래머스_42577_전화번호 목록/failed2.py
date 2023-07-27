'''
문제 : 전화번호 목록
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''
def solution(phone_book):
    dic = {}
    # 1. 길이별로 idx와 i를 dic에 저장해준다.
    for idx, i in enumerate(phone_book):
        n = len(i)
        if n not in dic:
            dic[n] = [(idx, i)]
        else:
            dic[n].append((idx, i))
    
    # 2. 자신보다 길이가 같거나 낮은 dic만 탐색해준다.
    for idx, i in enumerate(phone_book):
        for n, value in dic.items():
            if n <= len(i):
                for j in value:
                    if i[:n] == j[1] and idx != j[0]:
                        return False
    
    return True
print(solution(["123","456","789"]))