def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        temp = ''
        # 공백이면 공백 추가해주기
        if i == '':
            temp = ' '
        # 숫자면 소문자 처리만
        elif i[0].isdigit():
            temp = i.lower()
        # 숫자가 아니라면 첫글자 대문자처리 + 뒤에 소문자처리한 문자열 병합
        elif not i[0].isdigit():
            temp = i[1:].lower()
            temp = i[0].upper() + temp
        answer.append(temp)
    
    return ''.join(answer)

print(solution("adg   3eag   "))

# temp = 'Adg 3eag   '
# temp = temp.split(' ')
# print(temp)