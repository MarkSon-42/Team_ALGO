'''
문제 : 햄버거 만들기
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133502
'''
# 1. 그냥 스택으로..풀면될듯?

def solution(ingredient):
    answer = 0
    
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[len(stack)-4] == 1 and \
                stack[len(stack)-3] == 2 and \
                stack[len(stack)-2] == 3 and \
                stack[len(stack)-1] == 1:
                answer += 1
                del stack[len(stack)-4:len(stack)]
    
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])