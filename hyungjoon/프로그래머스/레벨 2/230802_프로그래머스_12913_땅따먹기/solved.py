'''
문제 : 땅따먹기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12913
'''
def solution(land):
    answer = 0
    n = len(land)
    # 1. 그냥... 이전 합으로 비교하면서 풀기? 시초각인데
    for i in range(1, n):
        for j in range(4):
            land[i][j] = land[i][j] + max(land[i-1][:j] + land[i-1][j+1:])
    answer = max(land[n-1])

    return answer