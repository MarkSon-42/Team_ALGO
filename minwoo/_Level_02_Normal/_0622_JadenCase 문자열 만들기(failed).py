# 문자라면, 공백을 기준으로 upper()를 해주자.

def solution(s):
    answer = ''
    for i in s:
        if i == 0 and s[0].isalpha():
            s[0].upper()
        elif s[i] == ' ' and s[i+1].isalpha():
            s[i+1].upper()
    return s

#   |
#   |      ... 아래처럼 저렇게 풀고싶었음.
#   v


def Jaden_Case(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)

