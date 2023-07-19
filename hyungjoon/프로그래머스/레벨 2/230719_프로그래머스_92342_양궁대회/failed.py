'''
문제 : 양궁대회
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''

from itertools import combinations_with_replacement as combi

def solution(n, info):
    answer = []
    
    '''
    1. 같은 점수에 맞춘 갯수가 a(어피치), b(라이언) 이라면, a >= b 라면 어피치, 아니라면 라이언
    2. 총점이 a >= b 라면 어피치, 아니면 라이언
    3. 화살 개수 * 점수 가 아님, 몇개를 맞추던 그 점수 하나만 얻는거임
    4. 가장 큰 점수차로 우승할 수 있는 방법이 여러개면, 가장 낮은 점수를 더 많이 맞힌 경우를 return
    4-1. 그게 여러개면 그 다음 낮은수로 비교
    # info 길이가 11이니까 완탐 될거같음
    '''

    
    # 0~10점까지 n개 중복조합으로 뽑고, 라이언 점수 할당해주기
    for combinated in combi(range(11), n):
        score = [0] * 11
        print(combinated)
        # 라이언 점수 할당해주기
        for i in combinated:
            score[10-i] += 1
            
        # 어피치, 라이언 점수
        a, l = 0, 0
        for index, i, j in enumerate(zip(info, score)):
            # 둘다 못맞췄으면 패스
            print(index, i)
            if i == j == 0:
                continue
    
    
    
    if not answer:
        answer = [-1]
    
    return answer

print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))