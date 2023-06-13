'''
문제 : 신규 아이디 추천
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72410
'''

import re

def solution(new_id):
    answer = ''
    
    # 1단계
    answer = new_id.lower()

    # 2단계
    answer = re.sub(r'[^0-9a-z-_.]', '', answer)
    
    # 3단계
    while answer.count('..') > 0:
        answer = answer.replace('..', '.')
    
    # 4단계
    answer = delPointStartOrEnd(answer)
    
    # 5단계
    if answer == '':
        answer += 'a'
        
    # 6단계
    if len(answer) >= 16:
        answer = list(answer)
        del answer[15:]
        answer = ''.join(answer)
        answer = delPointStartOrEnd(answer)
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer

def delPointStartOrEnd(s):
    s = list(s)
    if s[0] == '.':
        s[0] = ''
    if s[len(s)-1] == '.':
        s[len(s)-1] = ''
    
    return ''.join(s)

print(solution("=.="))