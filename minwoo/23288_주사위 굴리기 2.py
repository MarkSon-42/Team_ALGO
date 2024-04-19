# 함수 구현부는 쉬운데.. 주사위 처리가 겁나 헷갈린다

def bfs(si, sj, val):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        cx, cy = q.pop(0)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = cx + dx, cy + dy
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == val:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d1, d2, d3, d4, d5, d6 = 1, 2, 3, 4, 5, 6
dr = 1
cx = cy = answer = 0

for _ in range(K):
    ni, nj = cx + dx[dr], cy + dy[dr]
    if 0 <= ni < N and 0 <= nj < M:
        cx, cy = ni, nj
    else:
        dr = (dr + 2) % 4
        cx, cy = cx + dx[dr], cy + dy[dr]

    if dr == 0:
        d2, d1, d5, d6 = d1, d5, d6, d2
    elif dr == 1:
        d6, d4, d1, d3 = d3, d6, d4, d1
    elif dr == 2:
        d2, d1, d5, d6 = d6, d2, d1, d5
    else:
        d6, d4, d1, d3 = d4, d1, d3, d6

    answer += bfs(cx, cy, arr[cx][cy]) * arr[cx][cy]

    if d6 > arr[cx][cy]:
        dr = (dr + 1) % 4
    elif d6 < arr[cx][cy]:
        dr = (dr - 1) % 4

print(answer)
