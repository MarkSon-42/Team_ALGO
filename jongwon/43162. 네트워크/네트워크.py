def solution(n, computers):
    
    # 깊이 우선 탐색 함수 정의
    def dfs(x):
        visited[x] = True  # 현재 노드를 방문했음을 표시
        for i in range(n):  # 모든 노드를 순회
            if not visited[i] and computers[x][i]:  # 방문하지 않았고, 현재 노드와 연결되어 있으면
                dfs(i)  # 해당 노드로 이동하여 재귀적으로 탐색
    
    answer = 0  # 네트워크 개수를 저장할 변수 초기화
    
    visited = [False for _ in range(n)]  # 방문 여부를 나타내는 리스트 초기화
    for i in range(n):  # 모든 컴퓨터를 순회하며
        if not visited[i]:  # 방문하지 않은 컴퓨터에 대해서
            dfs(i)  # DFS 탐색을 통해 연결된 모든 컴퓨터를 방문하고
            answer += 1  # 네트워크 개수를 1 증가시킵니다.
    
    return answer  # 최종적인 네트워크 개수를 반환합니다.

