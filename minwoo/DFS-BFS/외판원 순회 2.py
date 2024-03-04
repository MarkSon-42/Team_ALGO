# 문제 좋네
# CS 최적화 문제중 대표적 문제들
# 배낭, 스케줄링, MST, 최단경로, 외판원, 빈 패킹, 네트워크 플로우

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

# 파라미터가 많은 딱히 좋은 함수는 아니지만, 코드가 매우 간결해졌다.
# 코드는 통과하지만 여러가지 제출버전 중에 가장 효율이 구림..
def dfs(depth, now, start, sum, answer):
    if depth == n and now == start:
        return min(answer, sum)
    for i in range(n):
        if not visited[i] and w[now][i] > 0:  # 방문하지 않았고, 다른 노드로의 경로가 존재한다면
            visited[i] = True
            answer = dfs(depth + 1, i, start, sum + w[now][i], answer)
            visited[i] = False  # 다른 경로도 탐색해야 하므로 재귀를 나올때 False로 업데이트
    return answer

print(dfs(0,0,0,0, float('inf')))