'''
문제 : 유기농 배추
링크 : https://www.acmicpc.net/problem/1012
소요시간 : 15분
'''
from collections import deque
t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(t):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(m)] for __ in range(n)]

    def bfs(r, c):
        # 방문처리 (visited 안쓰기)
        graph[r][c] = 0
        q = deque([(r, c)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nr, nc = x + dx[i], y + dy[i]

                # 범위 밖 제외
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if graph[nr][nc] == 0:
                    continue

                if graph[nr][nc] == 1:
                    # 방문처리
                    graph[nr][nc] = 0
                    q.append((nr, nc))


    for _ in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                # bfs를 돌면서 배추가 인접한 곳을 모두 0으로 만들어줌
                bfs(i, j)
                # bfs 작업이 끝나면 배추흰지렁이 한마리 추가
                answer += 1
    print(answer)