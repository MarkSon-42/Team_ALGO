'''
문제 : 크레인 인형뽑기 게임
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64061
'''
from collections import deque

def solution(board, moves):
    answer = 0
    # [0~4][0] 이 1번위치, [0~4][1]이 2번위치 이런식으로 인형이 배치된 것을 유념하자.
    # 1. 번호별로 스택을 만들어주고, 그 스택대로 작업해주는게 편할것같다.
    crain = {}
    basket = []
    
    for i in range(len(board)):
        temp = deque()
        for j in range(len(board)):
            # j행 i열에 있는 애들을 appendleft 해준다. 위치별로 스택을 만들어주는 과정임.
            if board[j][i] != 0:
                temp.appendleft(board[j][i])
        if i+1 not in crain:
            crain[i+1] = temp
    
    # 2. moves에 있는 번호대로 pop 해준다.
    for i in moves:
        # n번 위치에서 뽑은 인형을 바구니에 넣어준다.
        if len(crain[i]) > 0:
            doll = crain[i].pop()
            basket.append(doll)
        while len(basket) > 1 and basket[-2] == basket[-1]:
            basket.pop()
            basket.pop()
            answer += 2
    
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])