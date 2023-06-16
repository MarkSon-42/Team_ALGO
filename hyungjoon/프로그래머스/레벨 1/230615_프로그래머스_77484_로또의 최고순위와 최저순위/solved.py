'''
문제 : 로또의 최고순위와 최저순위
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77484
'''
def solution(lottos, win_nums):
    answer = []
    
    # 1. 일치번호 수 : 등수 의 map 선언
    winner = {
        0:6,
        1:6,
        2:5,
        3:4,
        4:3,
        5:2,
        6:1
    }
    
    # 2. 최소, 최대로 일치하는 것을 판별할 cnt 선언
    minCnt, maxCnt = 0, 0
    
    # # 배열을 정렬시켜서 일치하는 수가 먼저 계산되고, 모르는 번호를 나중에 계산하도록 한다.
    # lottos.sort(reverse=True)
    # win_nums.sort(reverse=True)
    
    # 3. 만약 수가 존재한다면, 각각 cnt에 1씩 더해준다.
    # 근데 최소만 구한다음에, 0이 다 맞는 경우가 이제 최대잖음? 그럼 0 개수만큼 더해주면 끝아님?
    for i in lottos:
        if i in win_nums:
            minCnt += 1
            maxCnt += 1
        elif i == 0:
            maxCnt += 1
    
    answer = [winner[maxCnt], winner[minCnt]]
    return answer