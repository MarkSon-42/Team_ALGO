'''
문제 : H_Index
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''
def solution(citations):
    answer = 0
    n = len(citations)
    
    # 정렬을 해서, 중위값을 정하고, 조건에 따라 좌우 인덱스 이동?
    # 0 1 2 2 3 4 5 6
    # 이 경우는 h = 3, l = 4, r = 4
    # 이러면 H_Index가 높은 상태니까, 낮춰줘야됨
    # 반대로 H_Index가 낮은 상태라면, 높여줘야됨
    # 0 1 1 1 1 4 5 6
    # 이걸 예시로 들어보자. 
    # h = 1, l = 4, r = 4 
    
    citations.sort()
    start = n//2
    
    while True:
        h = citations[start]
        # h번 이하로 인용된 논문들과 이상 인용된 논문들
        l, r = len(citations[:start]), len(citations[start:])
        if r >= h and l <= h:
            answer = h
            break

        if l > h:
            start -= 1
    
    return answer