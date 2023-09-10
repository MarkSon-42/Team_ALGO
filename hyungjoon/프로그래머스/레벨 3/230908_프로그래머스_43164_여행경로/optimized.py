'''
문제 : 여행경로
난이도 : 레벨 3
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
소요시간 : 1시간 30분
'''
from collections import defaultdict

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)
        # 사용하고 그래프에 다시 넣어줘야됨, 길이 끊겼다면 다시 return 해주는 부분인데 이거 좀 이해가 안감 ㅠ
        graph[key].insert(idx, country)

        if ret:
            return ret

def solution(tickets):
    answer = []

    graph = defaultdict(list)
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer
print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))