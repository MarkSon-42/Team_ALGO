def solution(arr):
    answer = 0
    lcm = 1
    for item in arr:
        lcm = LCM(lcm, item)    
    return lcm

# 최대공약수 구하기
def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 구하는 법
# a * b = GCD * LCM
def LCM(a, b):
    return a * b // GCD(a, b)