'''
문제 : 다음 큰 숫자
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12911
'''
def solution(n):
    cntN = format(n, 'b').count('1')
    
    for i in range(n+1, 1000001):
        cntI = format(i, 'b').count('1')
        if cntI == cntN:
            return i
        
solution(78)
    