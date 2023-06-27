def solution(n):
    ans = 0
    
    # 홀수는 짝수의 마지막 이동에서 1번을 더 이동해야함
    # 짝수는 2로 나누다가 2로 나누어 떨어지지 않는 값의 (예시 : 3) 이동값을 출력하면됨
    # 재귀함수?
    
    # 2진법 변환했을 때 1의 갯수만큼 건전지 소비하는듯?
    bin_num = str(bin(n))
    # bin_num = bin_num.replace("0b", "")
    ans = bin_num.count("1")

    return ans