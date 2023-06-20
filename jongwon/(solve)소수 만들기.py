def check(a, b, c): # 소수 판별
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 :
            return False 
    return True 

def solution(nums):
    result = 0
    for i in range(0, len(nums) - 2): # 삼중 반복문으로 숫자들 중 3개 뽑는 로직 구현
        for j in range(i+1, len(nums) - 1): 
            for k in range(j+1, len(nums)): 
                if check(nums[i], nums[j], nums[k]): # 뽑은 숫자들의 합을 소수 판별해서 true 이면 result 1증가
                    result += 1
    return result


from itertools import combinations
import math

def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0
    for x in combinations(nums, 3):
        if is_prime_number(sum(x)):
            answer += 1

    return answer

    