def primeNum(a):
    for i in range(2, a):  # 2부터 a-1까지 모든 수를 확인
        if a % i == 0:
            return False  # a가 i로 나누어 떨어지면 소수가 아님
    return True  # a가 모든 수로 나누어 떨어지지 않으면 소수


def solution(nums):
    cnt = 0  # 소수의 개수를 세기 위한 변수
    brute_force = []  # 가능한 조합의 합을 저장할 리스트

    # 세 수를 모두 더한 후 brute_force 리스트에 저장

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                brute_force.append(nums[i] + nums[j] + nums[k])


    # brute_force 리스트의 각 요소에 대해 소수 여부 확인
    for m in brute_force:
        if primeNum(m) == True:
            cnt += 1  # 소수이면 cnt 변수 증가


    return cnt
