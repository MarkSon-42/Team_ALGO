# deque를 이용한 BFS(Breath First Search) 구현
    # step 1. 탐색을 시작할 노드를 큐에 삽입하고 방문 처리
    # step 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    # step 3. 'step 2'의 과정을 더 이상 수행할 수 없을 때까지 반복


from collections import deque

# bfs 
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# 2차원 맵 정보
graph=[
  [], # 0번 노드 비우기
  [2,3,8], # 1번 노드와 연결된 노드(들)
  [1,7], # 2번 노드와 연결된 노드(들)
  [1,4,5], # 3번 노드와 연결된 노드(들)
  [3,5], # 4번 노드와 연결된 노드(들)
  [3,4], # 5번 노드와 연결된 노드(들)
  [7], # 6번 노드와 연결된 노드(들)
  [2,6,8], # 7번 노드와 연결된 노드(들)
  [1,7] # 8번 노드와 연결된 노드(들)
]


# 방문 정보
# False는 '방문하지 않음', True는 '방문 완료'를 나타냄
# (8 + 1)은 총 노드 개수 + 인덱스 0
visited = [False] * (8 + 1)


# bfs 호출
bfs(graph, 1, visited)


## 1 2 3 8 7 4 5 6
