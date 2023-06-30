def solution(n):
    answer = 0
    
    # 2의 개수
    count_2 = n // 2
    result = 0
    
    # 짝수인 경우
    if n % 2 == 0:
        for i in range(count_2 + 1):
            result += nCr(count_2 + i, count_2 - i) % 1234567
    # 홀수인 경우
    else:
        for i in range(count_2 + 1):
            result += nCr(count_2 + 1 + i, count_2 - i) % 1234567
    
    return int(result) % 1234567

# 7번부터 코드가 틀림

# def nCr(n, r):
#     result = 1
#     for i in range(r):
#         result = (result * (n - i) / (r - i)) % 1234567
#     return result % 1234567


# 오버플로우가 발생하는 것 같아 nCr 함수 코드 변경
def nCr(n, r):
    numerator = 1
    denominator = 1
    
    for i in range(r):
        numerator *= (n - i) % 1234567
        denominator *= (i + 1) % 1234567
        
    return numerator // denominator