from collections import deque

def max_safe_areas(N, arr):
    def bfs(x, y, h):
        q = deque()
        q.append((x, y))
        v[x][y] = 1

        while q:
            x, y = q.popleft()
            # 상, 하, 좌, 우 네 방향을 검사
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 이렇게 튜플로 가능
                nx, ny = x + i, y + j
                # 배열 범위 내에 있고, 방문하지 않았으며, 물 높이보다 높을 때만 진행 -> 조건 한방에 처리
                if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and arr[nx][ny] > h:
                    q.append((nx, ny))
                    v[nx][ny] = 1

    ans = 0
    for h in range(100):  # 물 높이를 0부터 99까지 반복해서 검사
        v = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                # 방문하지 않았고, 물 높이보다 높은 지점에서 BFS 실행
                if v[i][j] == 0 and arr[i][j] > h:
                    bfs(i, j, h)
                    cnt += 1
        # 최대 안전 지역 수 업데이트
        ans = max(ans, cnt)
    return ans

N = int(input())  # 배열 크기 입력
arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 값 입력

result = max_safe_areas(N, arr)  # 최대 안전 지역 수 계산
print(result)  # 결과 출력
