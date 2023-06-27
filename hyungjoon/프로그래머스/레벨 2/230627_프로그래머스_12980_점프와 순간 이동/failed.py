'''
문제 : 점프와 순간 이동
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''
import sys

def solution(n):
    ans = 0
    # 1. 10억이라 완탐이 안되니 수를 줄여보자
    # 2. 건전지는 최소 1임
    # 이게 top-down DP인가..?
    
    # 현재까지 온 거리 * 2 * 2 한게 n보다 크다면
    # 그 자리에서 점프를 하는게 더 효율적이다.
    for i in range(n):
        if i == 0:
            ans += 1
            continue
            
        if i*2 == n:
            return ans
        
        if i*2*2 + ans > n:
            ans += 1
            continue
        else:
            i *= 2

    return ans