'''
문제 : 짝지어 제거하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12973
'''
def solution(s):
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    return 0 if stack else 1

solution('abba')