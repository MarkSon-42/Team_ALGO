'''
문제 : 피보나치 수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12945
'''
def recursion(n):
    if n < 3:
        return 1
    return recursion(n-2) + recursion(n-1)

def solution(n):
    
    return recursion(n) % 1234567