'''
문제 : 연속 부분 수열 합의 개수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''
def solution(elements):
    answer = 0
    n = len(elements)
    
    elements = elements + elements[:-1]
    print(elements)
    
    # 처음 나온 수가 다시 중복되진 않는거같다. ex) 7 9 1 1 4 (7) x
    # 7 9 1 1 7 9 1 -> 길이가 짝수인 수열은 홀수가, 짝수인건 홀수가 된다.
    # 7 9 1 1 4 7 9 1 1 로 만들어준 다음에, 이 배열에서 길이가 5인 친구들을 구하자
    
    # 1. 길이가 1부터 n인 배열까지 구한다.
    # for i in range(n):
    #     for j in elements:
    # 이건 아닌거같음, 시초날거같다.
            
    
    
    
    return answer