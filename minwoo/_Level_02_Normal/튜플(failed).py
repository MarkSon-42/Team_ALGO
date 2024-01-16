# 순서 있음

# s의 길이는 5 이상 1,000,000 이하

# s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수

# 배열의 길이가 1 이상 500 이하인 경우만 입력

def solution(s):
    answer = []

    # 일단 s는 문자열이니 맨 양끝 {}를 제외하고, 계속 {}를 기준으로 나누자.

    for i in range(1, len(s) - 1):
        if s[i] == '{':
            continue
        if int(s[i]):
            if s[i + 1] == ',':
                answer.append(int(s[i]))

    # s = list(s)
    # # 리스트로 바로 변환 가능하네?

    return s