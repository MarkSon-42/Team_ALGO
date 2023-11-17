# 아니 힌트는 대체 왜 준거지..?

# 2 * 2 케이스를 빼주는 아이디어로 푸는게 아닌거 같은데

# "넴모"가 2x2 배열에 다 있지 않도록 가능한 모든 배치를 만들면서 개수를 세는걸로 생각

import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

# 1-index
Map = [[0 for _ in range(M + 1)] for __ in range(N + 1)]
answer = 0


def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return

    y = cnt // M + 1
    x = cnt % M + 1

    dfs(cnt + 1)  # 현재 위치에 넴모가 없다고 놓고 그 다음 부분 보는 dfs()
    if Map[y - 1][x] == 0 or Map[y][x - 1] == 0 or Map[y - 1][x - 1] == 0:  # 만약 놓을 수 있는 곳이라면
        Map[y][x] = 1
        dfs(cnt + 1)
        Map[y][x] = 0


dfs(0)
print(answer)


# ...????????????