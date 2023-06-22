def solution(s):
    answer = []
    s = s.split()
    for i in s:
        temp = i.lower()
        if not i[0].isdigit():
            # 인덱스를 직접 수정하면 에러가 발생한다.
            temp[0] = i[0].upper()
        answer.append(temp)
    
    return ' '.join(answer)

solution("3people unFollowed me")