'''
문제 : 괄호 회전하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76502
'''
from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    for i in range(len(s)):
        # 대, 중, 소괄호 판별해줄 스택
        big, mid, small = [], [], []
        flag = True
        for j in range(len(s)):
            # 열리는 괄호를 넣어준다.
            if s[j] == '[':
                big.append(s[j])
            elif s[j] == '{':
                mid.append(s[j])
            elif s[j] == '(':
                small.append(s[j])
            else:
                # 닫히는 괄호가 나올 때 해당 스택이 비어있다면 False
                if (s[j] == ']' and not big) or \
                   (s[j] == '}' and not mid) or \
                   (s[j] == ')' and not small):
                    flag = False
                    break
        if flag:
            answer += 1
        temp = s.popleft()
        s.append(temp)
    
    return answer
# 반례 ([{)}]
solution('{{{')