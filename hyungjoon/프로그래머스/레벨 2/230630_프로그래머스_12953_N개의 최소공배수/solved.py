'''
문제 : N개의 최소공배수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12953
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    answer = arr[0]
    
    for i in range(len(arr) - 1):
        # 1. 두 수의 최대공약수를 구하고
        temp = gcd(answer, arr[i+1])
        # 2. (현재까지의 수들의 최소공배수 * 다음 수) / (다음 수와의 최대공약수) 해주면됨
        answer = answer * arr[i+1] / temp
    
    return answer