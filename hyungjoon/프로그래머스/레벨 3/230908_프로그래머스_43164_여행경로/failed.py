'''
문제 : 여행경로
난이도 : 레벨 3
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
소요시간 : 1시간 30분
'''
def solution(tickets):
    answer = []
    
    # 숫자가 아니라 문자열이므로, 맵으로 인접행렬(그래프) 표현
    route = {}
    for a, b in tickets:
        if a not in route:
            # 목적지b와 방문여부를 의미하는 False
            route[a] = [[b, False]]
            # 1. 자기 자신을 재방문할 때는 넘어가야 함
            # 2. 처음시작할때 구분하기 위하는 용도로 사용
            route[a].append([a, True])
        else:
            route[a].append([b, False])
        # 알파벳순으로 방문하려면 기존에 저장된 그래프를 한번 정렬시켜주면 이후엔 추가작업 없어도됨
        route[a].sort(key=lambda x:x[0])
        
    def dfs(v):
        answer.append(v)
        print('현재 방문한 공항 : ' + v)
        if v in route:
            for idx, i in enumerate(route[v]):
                depart, visited = i[0], i[1]
                # visited를 의미, 해당 공항을 방문한게 아니라면 dfs 실행
                if not visited:
                    # 방문처리 여기서 해주기
                    route[v][idx][1] = True
                    dfs(depart)
                
    dfs('ICN')
    
    return answer
print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))