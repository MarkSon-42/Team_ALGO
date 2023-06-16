'''
문제 : 다트 게임
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17682
'''

def solution(dartResult):
    answer = 0
    
    # 영역별 점수를 정의해준다.
    scoreMap = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    
    # 점수를 계산해줄 스택을 선언해준다.
    stack = []
    # 10은 for문 돌때 1인지 0인지 10인지 판별이 안되니까 a로 바꿔줌
    dartResult = dartResult.replace('10', 'a')
    
    for i in dartResult:
        # 1. 스택에 계산할 점수를 넣어준다.
        if i == 'a':
            stack.append(10)
        # 1-2. 그냥 숫자는 바로 넣어주기
        elif i.isdigit():
            stack.append(int(i))
        # 2. 보너스 점수는 이전 점수를 pop해서 계산해준다.
        elif i == 'S' or i == 'D' or i == 'T':
            num = stack.pop()
            stack.append( num ** scoreMap[i])
        # 3. 옵션을 계산해준다.
        else:
            if i == '#':
                stack[-1] = stack[-1] * -1
            elif i == '*':
                num = stack.pop()
                # 첫번째 스타상인지 확인한다. 첫번째 스타상이 아니라면 직전 점수를 2배 해준다.
                if stack:
                    stack[-1] = stack[-1] * 2
                # 첫번째 스타상이면 걍 2배 곱해준다.
                stack.append( num * 2)
    answer = sum(stack)
    
    return answer

solution(	"1D2S#10S")