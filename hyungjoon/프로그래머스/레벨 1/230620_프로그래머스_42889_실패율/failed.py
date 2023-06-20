'''
문제 : 실패율
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''
def solution(N, stages):
    answer = []
    
    # 0. 스테이지, 실패율 로 answer 배열 만들어준다.
    for i in range(1, N+1):
        answer.append([i, 0])
    
    # 1. 스테이지별로 실패율을 구한다.
    for i in range(1, N+1):
        # 1-1. 해당 스테이지를 클리어한사람과, 도전중인 사람, 총 도전 플레이어
        clearPlayer = 0
        tryPlayer = 0
        totalPlayer = 0
        for j in stages:
            # 1-2. 마지막 스테이지 클리어 한 사용자 체크
            if j > N and i == N:
                totalPlayer += 1
                clearPlayer += 1
            elif i == j:
                tryPlayer += 1
                totalPlayer += 1
            elif j > i:
                clearPlayer += 1
                totalPlayer += 1
        # 실패율 계산
        perOfFail = tryPlayer / totalPlayer
        # i번째 스테이지의 실패율 입력
        answer[i-1][1] = perOfFail
        
    answer.sort(key=lambda x:-x[1])

    # 찐 정답 배열
    aanswer = []
    for i in answer:
        aanswer.append(i[0])

    return aanswer

solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3])

