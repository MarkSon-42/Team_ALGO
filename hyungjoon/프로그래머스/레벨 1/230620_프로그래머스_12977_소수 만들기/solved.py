'''
문제 : 소수 만들기
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''
import math

def solution(nums):
    answer = 0
    
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                answer += 1 if isPrime(sum([nums[i], nums[j], nums[k]])) else 0

    return answer

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True