'''
문제 : 타겟 넘버
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, numbers[0]))
    q.append((0, -numbers[0]))
    while q:
        idx, temp = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append((idx, temp + numbers[idx]))
            q.append((idx, temp - numbers[idx]))
        else:
            if temp == target:
                answer += 1
    
    return answer
