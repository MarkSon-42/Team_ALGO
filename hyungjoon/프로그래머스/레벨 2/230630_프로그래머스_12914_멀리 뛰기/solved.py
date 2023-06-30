'''
문제 : N개의 최소공배수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12953
'''
def solution(n):
    answer = [1, 2]
    # 1일떄 1
    # 2일때 2
    # 3일때 3
    # 4일때 5
    # 5일때 8

    # 경우의 수가 피보나치임
    for i in range(2, n):
        answer.append(answer[i-2] + answer[i-1])
    
    return answer[n-1] % 1234567

solution(4)