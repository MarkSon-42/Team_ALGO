'''
문제 : 둘만의 암호
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/155652
'''
def solution(s, skip, index):
    answer = ''
    
    for i in s:
        # 1. 아스키코드로 푸는게 코드가 깔끔하게 나온다, 아스키코드로 변환해주자
        # 1-1. index만큼 점프해주는데, 도중에 skip에 해당하는 문자가 있으면 그만큼 index +1 해준다.
        cnt = 0
        for j in skip:
            if ord(j) > ord(i) and ord(j) < ord(i) + index:
                cnt += 1
        
        temp = index + cnt
        
        # 2. index만큼 뒤에 있는 수를 찾아준다, z를 넘어가면 a로 돌아와야한다.
        if ord(i) + temp > ord('z'):
            t = chr(ord(i) + temp - 26)
        else:
            t = chr(ord(i) + temp)
        answer += t
    
    return answer

solution('aukks',"wbqd",5)

