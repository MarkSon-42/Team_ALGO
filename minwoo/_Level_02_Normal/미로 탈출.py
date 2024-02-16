

from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])
    r, c, distance = 0, 0, 0  # 시작 위치, 이동 거리 초기화
    dr = [-1, 1, 0, 0]  # 이동 방향: 상, 하, 좌, 우
    dc = [0, 0, -1, 1]
    path = deque()  # 경로를 저장할 큐 생성
    visited = [[False for _ in range(cols)] for _ in range(rows)]  # 방문 여부 저장할 리스트 초기화
    opened = False  # 특정 지점을 방문하여 큐와 방문 여부 리스트 초기화할지 여부 초기화

    # 시작 위치 (S) 찾기
    for i, row in enumerate(maps):
        if 'S' in row:
            j = row.index('S')
            r, c, distance = i, j, 0
            visited[i][j] = True  # 시작 위치 방문 여부 체크

    # BFS 탐색 시작
    while True:
        for i in range(4):
            x = [r + dr[i], c + dc[i]]  # 다음 위치 계산
            if 0 <= x[0] < rows and 0 <= x[1] < cols and not visited[x[0]][x[1]] and maps[x[0]][x[1]] != 'X':
                path.append([x[0], x[1], distance + 1])  # 큐에 다음 위치 추가
                visited[x[0]][x[1]] = True  # 다음 위치 방문 여부 체크

        if len(path) != 0:
            r, c, distance = path.popleft()  # 큐에서 다음 위치 가져오기
        else:
            distance = -1  # 경로가 없는 경우
            break

        if not opened and maps[r][c] == 'L':  # L 지점에 처음 도착한 경우
            opened = True  # L 지점 방문 체크
            visited = [[False for _ in range(cols)] for _ in range(rows)]  # 방문 여부 리스트 초기화
            visited[r][c] = True  # L 지점 방문 체크
            path = deque()  # 경로 큐 초기화
            path.append([r, c, distance])  # L 지점부터 다시 BFS 탐색 시작

        if opened and maps[r][c] == 'E':  # E 지점에 도착한 경우
            break

    return distance  # E 지점까지의 최단 거리