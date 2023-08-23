'''
문제 : 택배상자
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''
from collections import deque

def solution(order):
    answer = 0
    
    # 보조 컨테이너 = 스택
    # 메인 컨테이너 = 큐
    
    sub = deque()
    main = deque([0] * len(order))
    n = len(order)
    
    # order
    # 4, 3, 1, 2, 5
    # 4는 4번째 상자를 1번째로 트럭에 실어야 한다. 를 의미
    # 3은 3번째 상자를 2번째로 트럭에 실어야 한다. 를 의미
    # 5, 4, 3, 2, 1
    
    # 배달되어야 하는 박스 순서
    # 3, 4, 2, 1, 5
    # 5번 상자가 1번째로 
    # 4번 상자가 2번째로
    # 그래서 1, 2, 3, 4, 5

    # 1. 메인 컨테이너에서 순서를 도출한다.
    # 2. 메인 컨테이너에서 원하는 수가 있다면, 나올때까지 pop을 한다.
    # 2-1. 메인 컨테이너에 원하는 수가 없다면, 서브컨테이너에서 나올때까지 pop을 한다.
    # 원하는 수가 있는지 찾는건 map을 사용하자.
    # sub에선 del로 아예 날려버리는거고, main에선 sub로 옮겨주는거임

    mainMap, subMap = {}, {}

    for i in range(n):
        main[order[i]-1] = i+1
        mainMap[order[i]] = 1

    for i in range(1, n+1):
        if i in mainMap:
            while True:
                t = main.popleft()
                if t == i:
                    answer += 1
                    break
                else:
                    sub.append(t)
                    subMap[i] = 1
                    del mainMap[t]
        elif i == sub[-1]:
            sub.pop()
            answer += 1
        else:
            break
    return answer
print(solution([4, 3, 1, 2, 5]))