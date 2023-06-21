def solution(s):
    answer = ''
    
    strToNum = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    
    temp = ''
    for i in s:
        # 숫자면 answer에 더해주고 넘어감
        if i.isdigit():
            if temp in strToNum:
                answer += str(strToNum[temp])
                temp = ''
            answer += i
        else:
            if temp in strToNum:
                answer += str(strToNum[temp])
                temp = i
            else:
                temp += i
    
    # 마지막에 한번 체크
    if temp in strToNum:
        answer += str(strToNum[temp])
    
    return int(answer)

solution("one4seveneight")