'''
문제 : 실패율
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''
def solution(N, stages):
    answer = []
    
    # 0. 스테이지:실패율 map 생성
    clearMap = {}
    # 총 도전자 수
    totalPlayer = len(stages)

    # 2. 스테이지별 실패율 구하기
    for i in range(1, N+1):
        # 2-1. 핵심. O(N)으로 돌기 위해 for문 한번만 돌려준다.
        # 1층부터 올라가기 때문에, 1층을 도전하고 있는 사람(1명)을 빼주면, 2층을 도전하거나, 클리어한 사람은 최소 7명이라는 뜻이다.
        # 따라서, 전체길이를 업데이트 해가면서 구하면 O(N)으로 실패율을 구할 수 있다.
        
        tryPlayer = stages.count(i)
        # 런타임에러 자꾸 나서 체크해보니까 0으로 나누는 케이스에서 에러남
        if tryPlayer > 0 :
            perOfFail = tryPlayer / totalPlayer
            clearMap[i] = perOfFail
            totalPlayer -= tryPlayer
        else:
            clearMap[i] = 0

    temp = sorted(clearMap.items(), key=lambda x:x[1], reverse=True)

    for i in temp:
        answer.append(i[0])

    return answer