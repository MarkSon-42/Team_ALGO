# 문제명 : 멋쟁이 숫자
# 숫자로만 이루어진 문자열 s가 있습니다. (0 <=  s.length < 1,000)
# 아래의 조건을 모두 만족하는 숫자를 '멋쟁이 숫자'라고 합니다.
#
# [조건]
# 1. 길이가 3인 s의 substring을 10진수로 읽은 숫자이다.
# 2. 각 자리의 숫자가 모두 같다.
#
# 구현사항
# 문자열s를 입력받아 멋쟁이 숫자를 리턴하는 함수를 만들어주세요.
#
# 만약, 멋쟁이 숫자가 여러 개 존재하는 경우에는 가장 큰 수를 리턴합니다.
# 만약, 가장 큰 멋쟁이 숫자가 000이라면 0을 리턴합니다.
# 만약, 멋쟁이 숫자가 존재하지 않다면 -1을 리턴합니다.
# 예시 문제
# 예시 1
#
# 입력: s = “12223”
# 출력: 222
# 예시 2
#
# 입력: s = “111999333”
# 출력: 999
# 설명: 111, 333, 999 3가지가 존재하고 999가 제일 크므로 999를 리턴합니다.
# 예시 3
#
# 입력: s = “123”
# 출력: -1

def solution(s):
    cool_numbers = set()
    for i in range(len(s) - 2):
        substring = s[i:i+3]
        if substring[0] == substring[1] == substring[2]:
            cool_numbers.add(int(substring))
    if not cool_numbers:
        return -1
    return max(cool_numbers)
