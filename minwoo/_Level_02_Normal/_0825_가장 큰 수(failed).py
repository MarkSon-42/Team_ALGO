from itertools import combinations


# 가장 큰 수를 찾아내자.
# 요소 10만에 대해서 효율적으로 짜야 통과할 수 있을 듯
# numbers 연속으로 사용한 문자열 조합 -> 정렬해서 리턴?
# 통과 안될수도.
# 원소가 "0 이상" <- 0 input주의해야
def solution(numbers):
    answer = ''
    n = len(numbers)
    for i in range(n):
        numbers[i] = str(numbers[i])

    tmp = combinations(numbers, 4)

    return tmp

# 6 10 2 -> 조합수 6개
# combinations?
