'''
문제 : 피보나치 수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12945
'''
def solution(n):
    # 걍 배열 선언해서 풀기.. 내키진않음
    # n번쨰 피보나치 수 % 1234567 한것을 배열에 직접 넣어준다.
    answer = [1, 1]
    for i in range(2, n):
        answer.append((answer[-2] + answer[-1]) % 1234567)
    return answer[-1]

solution(3)