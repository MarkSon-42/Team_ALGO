'''
문제 : 주식가격
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''

def solution(prices):
    n = len(prices)
    answer = [n-1] * n
    
    # 1. 스택에 (초, 값) 으로 쌓아준다.
    stack = []
    
    for idx, price in enumerate(prices):
        # 스택을 순회하면서 가격이 떨어졌다면 그 인덱스에 시간을 넣어준다.
        # 스택의 마지막에 들어온애만 체크하면됨. 그 밑에 있는 애들은 어차피 해당 가격보다 낮은 가격이기 때문에
        while stack and stack[-1][1] < price:
            temp = stack.pop()
            index, p = temp[0], temp[1]
            answer[index] -= index
        stack.append((idx, price))
    
    return answer