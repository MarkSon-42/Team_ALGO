'''
문제 : 점프와 순간 이동
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''
def solution(n):
    ans = 0
    
    # 진짜 그냥 단순하게 생각해보자
    # 나눠 떨어지면 순간이동, 나눠서 안떨어지면 점프
    while n > 0:
        if n % 2 == 1:
            ans += 1
        n = n//2

    return ans